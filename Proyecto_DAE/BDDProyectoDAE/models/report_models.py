from sqlalchemy import Column, String, Enum, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import uuid
from config.database import Base

class Dataset(Base):
    __tablename__ = "datasets"
    id = Column(UUID(as_uuid=True), primary_key = True, default = uuid.uuid4)
    name = Column(String(100))
    schema = Column(JSON)
    created_at = Column(DateTime, default = lambda: datetime.now(timezone.utc))
    reports = relationship("Reports", back_populates="datasets")

class Report(Base):
    __tablename__ = "reports"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(150))
    type = Column(Enum("pdf", "csv", "json", name = "report_type"))
    generated_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    dataset_id = Column(UUID(as_uuid=True), ForeignKey("datasets.id"))
    created_at = Column(DateTime, default = lambda: datetime.now(timezone.utc))
    dataset = relationship("Dataset", back_populates="reports")

class ExportLog(Base):
    __tablename__ = "export_logs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    report_id = Column(UUID(as_uuid=True), primary_key=True)
    format = Column(String(20))
    path = Column(String(255))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))