from marshmallow import Schema, fields


class ItemSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Decimal(required=True)
    store_id = fields.Integer(required=True)


