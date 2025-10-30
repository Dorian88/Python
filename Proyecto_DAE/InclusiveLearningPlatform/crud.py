from sqlalchemy.orm import Session
import models, schemas
from auth import hash_password, verify_password
from typing import Optional

# Roles
def create_role(db: Session, role: schemas.RoleCreate):
    db_role = models.Role(name=role.name, description=role.description)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_role_by_name(db: Session, name: str) -> Optional[models.Role]:
    return db.query(models.Role).filter(models.Role.name == name).first()

def list_roles(db: Session):
    return db.query(models.Role).all()

# Users
def create_user(db: Session, user: schemas.UserCreate):
    hashed = hash_password(user.password)
    db_user = models.User(full_name=user.full_name, email=user.email, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def add_role_to_user(db: Session, user: models.User, role: models.Role):
    user.roles.append(role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

# Institutions & students
def create_institution(db: Session, inst: schemas.InstitutionCreate):
    i = models.Institution(name=inst.name, address=inst.address)
    db.add(i)
    db.commit()
    db.refresh(i)
    return i

def list_institutions(db: Session):
    return db.query(models.Institution).all()

def create_student(db: Session, s: schemas.StudentCreate):
    st = models.Student(user_id=s.user_id, institution_id=s.institution_id, enrollment=s.enrollment)
    db.add(st)
    db.commit()
    db.refresh(st)
    return st

def list_students(db: Session):
    return db.query(models.Student).all()

# Quizzes & assignments
def create_quiz(db: Session, q: schemas.QuizCreate):
    quiz = models.Quiz(title=q.title, description=q.description)
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    return quiz

def assign_quiz(db: Session, a: schemas.AssignmentCreate):
    assignment = models.Assignment(quiz_id=a.quiz_id, student_id=a.student_id)
    db.add(assignment)
    db.commit()
    db.refresh(assignment)
    return assignment

def grade_assignment(db: Session, assignment_id: int, score: int):
    assignment = db.query(models.Assignment).filter(models.Assignment.id == assignment_id).first()
    if assignment:
        assignment.score = score
        assignment.status = "graded"
        db.add(assignment)
        db.commit()
        db.refresh(assignment)
    return assignment

# Reports
def create_report(db: Session, r: schemas.ReportCreate):
    report = models.Report(title=r.title, content=r.content)
    db.add(report)
    db.commit()
    db.refresh(report)
    return report