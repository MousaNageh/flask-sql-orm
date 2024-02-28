from marshmallow import Schema, fields




class StoreSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)


