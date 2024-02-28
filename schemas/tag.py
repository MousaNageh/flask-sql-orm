from marshmallow import Schema, fields
from schemas.store import StoreSchema
from schemas.item import ItemSchema

class TagSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)


class TagDetailsSchema(TagSchema):
    store_id = fields.Integer(dump_only=True)
    store = fields.Nested(StoreSchema())
    items = fields.Nested(ItemSchema(many=True))


class TagDeleteSchema(Schema):
    message = fields.Str()
    tag = fields.Nested(TagSchema())
    item = fields.Nested(ItemSchema())