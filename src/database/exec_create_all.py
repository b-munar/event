from src.database.base import Base
from src.database.engine import engine

from src.models.event_model import EventModel

table_objects = [EventModel.__table__]

if __name__ == "__main__":
    Base.metadata.create_all(
        bind = engine(), 
        tables=table_objects,
        checkfirst=True
    )