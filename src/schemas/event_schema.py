from marshmallow import Schema, fields

class EventDeserializeSchema(Schema):
    titulo = fields.String()
    fecha = fields.String()
    hora = fields.String()
    description = fields.String()
    location = fields.String()

class EventSerializeSchema(Schema):
    id = fields.UUID()
    titulo = fields.String()
    fecha = fields.String()
    hora = fields.String()
    description = fields.String()
    location = fields.String()