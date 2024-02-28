from db import db
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas import StoreSchema, StoreDetailSchema
from models import Store
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import subqueryload

blp = Blueprint("stores", __name__, url_prefix="/api/store", description="operations on stores")


@blp.route("/")
class StoreCreateUpdateApi(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return Store.query.all()

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, data):
        store = Store(**data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(500, message="server error")
        return store


@blp.route("/<int:store_id>")
class StoreGetDeleteApi(MethodView):

    @staticmethod
    @blp.response(200, StoreDetailSchema)
    def get(store_id):
        return Store.query.options(subqueryload(Store.items)).get_or_404(store_id)

    @staticmethod
    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def put(data, store_id):
        store = Store.query.get_or_404(store_id)
        store.name = data["name"]
        store.description = data["description"]
        db.session.add(store)
        db.session.commit()
        return store

    @staticmethod
    @blp.response(204)
    def delete(store_id):
        store = Store.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
