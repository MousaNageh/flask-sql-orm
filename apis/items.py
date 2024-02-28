from db import db
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas import ItemSchema, ItemDetailSchema
from models import Item
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
blp = Blueprint('items', __name__, url_prefix='/api/item')


@blp.route('/')
class ItemListCreateAPI(MethodView):

    @staticmethod
    @blp.arguments(ItemSchema, location='json')
    @blp.response(201, ItemSchema)
    def post(data):
        try:
            item = Item(**data)
            db.session.add(item)
            db.session.commit()
            return item
        except IntegrityError:
            return abort(400, message='store id not exists')

    @staticmethod
    @blp.response(200, ItemSchema(many=True))
    def get():
        return Item.query.all()

@blp.route('/<int:item_id>')
class ItemListCreateAPI(MethodView):

    @staticmethod
    @blp.arguments(ItemSchema, location='json')
    @blp.response(201, ItemSchema)
    def put(data, item_id):
        item = Item.query.get_or_404(item_id)
        item.name = data.get("name")
        item.price = data.get("price")
        item.description = data.get("description")
        try:
            db.session.add(item)
            db.session.commit()
            return item
        except IntegrityError:
            return abort(400, message='store id not exists')

    @staticmethod
    @blp.response(200, ItemDetailSchema)
    def get(item_id):
        return Item.query.options(joinedload(Item.store)).get_or_404(item_id)
