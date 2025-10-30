from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, JSON, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from config.database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    institution_id = Column(UUID(as_uuid=True), ForeignKey("institutions.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    profile = relationship("LearningProfile", back_populates="student", uselist=False)
    records = relationship("AcademicRecord", back_populates="student")

class LearningProfile(Base):
    __tablename__ = "learning_profiles"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"))
    learning_style = Column(String(100))
    preferences = Column(JSON)
    ai_feedback = Column(JSON)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    student = relationship("Student", back_populates="profile")

class AcademicRecord(Base):
    __tablename__ = "academic_records"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"))
    subject = Column(String(120))
    score = Column(Integer)
    observation = Column(Text)
    date = Column(DateTime, default=datetime.utcnow)
    student = relationship("Student", back_populates="records")

class AIOutput(Base):
    __tablename__ = "ai_outputs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    record_id = Column(UUID(as_uuid=True), ForeignKey("academic_records.id"))
    model_version = Column(String(50))
    prediction = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
