from sqlalchemy import Column, String, Date, ForeignKey, Integer
from src.database.base import Base
from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped


class EventModel(Base):
    __tablename__ = 'event'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user = Column(UUID(as_uuid=True), nullable=False)
    titulo = Column(String(), nullable=False)
    fecha = Column(Date, nullable=False)
    hora = Column(String(), nullable=False)
    description = Column(String())
    location = Column(String())
    sportmen = relationship("Sportmen")

class Sportmen(Base):
    __tablename__ = 'sportmen'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    event_id = Column(UUID(as_uuid=True), ForeignKey("event.id"), nullable=False)
    sportmen = Column(UUID(as_uuid=True), nullable=False)
    event = relationship("EventModel", back_populates="sportmen", lazy="joined")