from sqlalchemy import Column, String, Enum, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import uuid
from config.database import Base

class Notification(Base):
    __tablename__="notifications"
    id = Column(UUID(as_uuid=True), primary_key = True, default = uuid.uuid4)
    title = Column(String(200))
    message = Column(Text)
    channel = Column(Enum("email", "sms", "push", "inapp", name = "chanel_type"))
    create_at = Column(DateTime, default = lambda: datetime.now(timezone.utc))
    recipients = relationship("Recipient", back_populates = "notification")

class Recipient(Base):
    __tablename__="recipients"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    notification_id = Column(UUID(as_uuid=True), ForeignKey("notifications.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    delivery_stauts = Column(Enum("pending", "sent", "failed", name="delivery_sataus"))
    sent_at = Column(DateTime)
    notification = relationship("Notification", back_populates = "recipients")