from marshmallow import Schema, fields

class EventDeserializeSchema(Schema):
    event = fields.String(required=True)

class EventSerializeSchema(Schema):
    id = fields.UUID()
    event = fields.String()
    updateAt = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z')
    createdAt = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z')