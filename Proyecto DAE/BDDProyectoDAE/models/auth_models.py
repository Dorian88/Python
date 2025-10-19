from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Table, Enum, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from config.database import Base

role_permissions = Table(
    "role_permissions", Base.metadata,
    Column("role_id", UUID(as_uuid = True), ForeignKey("roles.id")),
    Column("permission_id", UUID(as_uuid = True), ForeignKey("permissions.id"))
)

class Institution(Base):
    __tablename__ = "institutions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(150), nullable=False)
    domain = Column(String(120), nullable=False, unique=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    users = relationship("User", back_populates="institution")

class Role(Base):
    __tablename__ = "roles"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(200))
    permissions = relationship("Permission", secondary=role_permissions, back_populates="roles")

class Permission(Base):
    __tablename__ = "permissions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), unique=True)
    description = Column(String(255))
    roles = relationship("Role", secondary=role_permissions, back_populates="permissions")

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(150))
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"))
    institution_id = Column(UUID(as_uuid=True), ForeignKey("institutions.id"))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    role = relationship("Role")
    institution = relationship("Institution", back_populates="users")

class Token(Base):
    __tablename__ = "tokens"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    token = Column(Text, nullable=False)
    type = Column(Enum("access", "refresh", name="token_type"))
    expires_at = Column(DateTime)
    revoked = Column(Boolean, default=False)