from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile
from database import engine, Base
import models, schemas, crud
from dependencies import get_db, get_current_user, require_role
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from auth import create_access_token
from datetime import timedelta
from dotenv import load_dotenv
import os
from reportlab.pdfgen import canvas
from io import BytesIO
from fastapi.responses import StreamingResponse

load_dotenv()
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

app = FastAPI(title="Inclusive Learning Platform - Auth & Core APIs")

# Create DB tables
Base.metadata.create_all(bind=engine)

# --- Auth endpoints ---
@app.post("/auth/register", response_model=schemas.UserRead)
def register(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = crud.create_user(db, user_in)
    # by default assign "student" role if exists
    #role = crud.get_role_by_name(db, "student")
    #if role:
    #    crud.add_role_to_user(db, user, role)
    return user

@app.post("/auth/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentials")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/auth/me", response_model=schemas.UserRead)
def me(user = Depends(get_current_user)):
    return user

# --- Roles management (admin) ---
@app.post("/roles/", response_model=schemas.RoleRead, dependencies=[Depends(require_role("admin"))])
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    existing = crud.get_role_by_name(db, role.name)
    if existing:
        raise HTTPException(status_code=400, detail="Role already exists")
    return crud.create_role(db, role)

@app.get("/roles/", response_model=list[schemas.RoleRead], dependencies=[Depends(require_role("admin"))])
def list_roles(db: Session = Depends(get_db)):
    return crud.list_roles(db)

# --- Assign role to user (admin) ---
@app.post("/roles/assign", dependencies=[Depends(require_role("admin"))])
def assign_role_to_user(email: str, role_name: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    role = crud.get_role_by_name(db, role_name)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    user = crud.add_role_to_user(db, user, role)
    return {"message": f"Role {role_name} assigned to {email}"}

# --- Institutions ---
@app.post("/institutions/", response_model=schemas.InstitutionRead, dependencies=[Depends(require_role("admin"))])
def create_institution(inst: schemas.InstitutionCreate, db: Session = Depends(get_db)):
    return crud.create_institution(db, inst)

@app.get("/institutions/", response_model=list[schemas.InstitutionRead], dependencies=[Depends(get_current_user)])
def get_institutions(db: Session = Depends(get_db)):
    return crud.list_institutions(db)

# --- Students ---
@app.post("/students/", response_model=schemas.StudentRead, dependencies=[Depends(require_role("admin"))])
def create_student(s: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, s)

@app.get("/students/", response_model=list[schemas.StudentRead], dependencies=[Depends(get_current_user)])
def get_students(db: Session = Depends(get_db)):
    return crud.list_students(db)

# --- Quizzes & assignments ---
@app.post("/quizzes/", response_model=schemas.QuizRead, dependencies=[Depends(require_role("admin"))])
def create_quiz(q: schemas.QuizCreate, db: Session = Depends(get_db)):
    return crud.create_quiz(db, q)

@app.post("/assignments/", response_model=schemas.AssignmentRead, dependencies=[Depends(require_role("teacher"))])
def assign_quiz(a: schemas.AssignmentCreate, db: Session = Depends(get_db)):
    return crud.assign_quiz(db, a)

@app.post("/assignments/{assignment_id}/grade", response_model=schemas.AssignmentRead, dependencies=[Depends(require_role("teacher"))])
def grade_assignment(assignment_id: int, score: int, db: Session = Depends(get_db)):
    assignment = crud.grade_assignment(db, assignment_id, score)
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return assignment

# --- Reports (generate PDF) ---
@app.post("/reports/", response_model=schemas.ReportRead, dependencies=[Depends(require_role("admin"))])
def create_report(r: schemas.ReportCreate, db: Session = Depends(get_db)):
    return crud.create_report(db, r)

@app.get("/reports/{report_id}/pdf", dependencies=[Depends(require_role("admin"))])
def get_report_pdf(report_id: int, db: Session = Depends(get_db)):
    report = db.query(models.Report).filter(models.Report.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    # generate PDF in memory
    buffer = BytesIO()
    c = canvas.Canvas(buffer)
    c.setFont("Helvetica", 14)
    c.drawString(50, 800, report.title)
    textobject = c.beginText(50, 770)
    textobject.setFont("Helvetica", 11)
    for line in report.content.splitlines():
        textobject.textLine(line)
    c.drawText(textobject)
    c.showPage()
    c.save()
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="application/pdf", headers={"Content-Disposition": f"attachment; filename=report_{report_id}.pdf"})

# --- Helper: bootstrap roles endpoint (for first run) ---
@app.post("/bootstrap/roles")
def bootstrap_roles(db: Session = Depends(get_db)):
    existing = db.query(models.Role).count()
    if existing > 0:
        return {"message": "Roles already present"}
    roles = [
        {"name": "admin", "description": "Administrator"},
        {"name": "teacher", "description": "Docente / Profesor"},
        {"name": "student", "description": "Estudiante"},
        {"name": "support", "description": "Profesional de apoyo"},
        {"name": "coordinator", "description": "Coordinador institucional"},
    ]
    created = []
    for r in roles:
        created.append(crud.create_role(db, schemas.RoleCreate(**r)))
    return {"created": [c.name for c in created]}
