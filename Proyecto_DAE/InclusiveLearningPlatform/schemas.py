from pydantic import BaseModel, EmailStr
from typing import List, Optional
import datetime

# Roles
class RoleCreate(BaseModel):
    name: str
    description: Optional[str] = None

class RoleRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    class Config:
        orm_mode = True

# User
class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    is_active: bool
    roles: List[RoleRead] = []
    class Config:
        orm_mode = True

# Auth
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Institution / Student
class InstitutionCreate(BaseModel):
    name: str
    address: Optional[str] = None

class InstitutionRead(BaseModel):
    id: int
    name: str
    address: Optional[str] = None
    class Config:
        orm_mode = True

class StudentCreate(BaseModel):
    user_id: int
    institution_id: int
    enrollment: Optional[str] = None

class StudentRead(BaseModel):
    id: int
    user_id: int
    institution_id: int
    enrollment: Optional[str] = None
    class Config:
        orm_mode = True

# Quiz / Assignment
class QuizCreate(BaseModel):
    title: str
    description: Optional[str] = None

class QuizRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    class Config:
        orm_mode = True

class AssignmentCreate(BaseModel):
    quiz_id: int
    student_id: int

class AssignmentRead(BaseModel):
    id: int
    quiz: QuizRead
    student_id: int
    status: Optional[str] = None
    score: Optional[int] = None
    class Config:
        orm_mode = True

# Report generation
class ReportCreate(BaseModel):
    title: str
    content: str

class ReportRead(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime.datetime
    class Config:
        orm_mode = True
