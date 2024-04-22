from sqlalchemy import Column, String, Date
from src.database.base import Base
from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

class EventModel(Base):
    __tablename__ = 'event'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user = Column(UUID(as_uuid=True), nullable=False)
    titulo = Column(String(), nullable=False)
    fecha = Column(Date, nullable=False)
    hora = Column(String(), nullable=False)
    description = Column(String())
    location = Column(String())