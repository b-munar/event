from marshmallow import Schema, fields
from schemas.event_schema import EventSerializeSchema

class SportmenDeserializeSchema(Schema):
    event_id = fields.UUID()
    amount = fields.Integer()

class SportmenSerializeSchema(Schema):
    id = fields.UUID()
    event_id = fields.UUID()
    event = fields.Nested(EventSerializeSchema)
    # service = fields.Dict()