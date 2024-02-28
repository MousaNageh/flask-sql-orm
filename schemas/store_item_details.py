from schemas.item import ItemSchema
from schemas.store import StoreSchema
from marshmallow import fields


class StoreDetailSchema(StoreSchema):
    items = fields.Nested(StoreSchema(many=True), many=True, dump_only=True)


class ItemDetailSchema(ItemSchema):
    store_id = fields.Integer(dump_only=True)
    store = fields.Nested(StoreSchema(), dump_only=True)
