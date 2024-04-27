from marshmallow import Schema, fields
from src.schemas.event_schema import EventSerializeSchema

class SportmenDeserializeSchema(Schema):
    event_id = fields.UUID()

class SportmenSerializeSchema(Schema):
    id = fields.UUID()
    event_id = fields.UUID()
    event = fields.Nested(EventSerializeSchema)
    # service = fields.Dict()