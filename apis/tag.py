from db import db
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas import TagSchema, TagDetailsSchema, TagDeleteSchema
from models import Tag, Store, Item
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("tags", __name__, url_prefix="/api/tag", description="operations on tags")


@blp.route("/<int:store_id>")
class TagCreateGetDeleteApi(MethodView):
    @staticmethod
    @blp.response(200, TagDetailsSchema(many=True))
    def get(store_id):
        store = Store.query.get_or_404(store_id)
        return store.tags.all()

    @staticmethod
    @blp.arguments(TagSchema)
    @blp.response(201, TagSchema)
    def post(data, store_id):
        if Tag.query.filter(Tag.store_id == store_id, Tag.name == data["name"]).first():
            abort(400, message="tag already exists")

        tag = Tag(**data, store_id=store_id)
        try:
            db.session.add(tag)
            db.session.commit()
        except IntegrityError:
            abort(400, message="tag name already exists")
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return tag

    @staticmethod
    @blp.response(204, description="delete a tag", example={"message": "tag deleted"})
    @blp.alt_response(404, description="if the tag is not exists", example={"tag_not_found": "tag not exists"})
    @blp.alt_response(500, description="if any error exists on the server")
    def delete(tag_id):
        tag = Tag.query.get_or_404(tag_id)
        try:
            db.session.delete(tag)
            db.session.commit()
            return {"message": "tag deleted"}
        except SQLAlchemyError as e:
            abort(500, message=str(e))





@blp.route("/<int:item_id>/<int:tag_id>")
class TagAddRemoveToItemApi(MethodView):

    @staticmethod
    @blp.response(201, TagSchema)
    def post(item_id, tag_id):
        tag = Tag.query.get_or_404(tag_id)
        item = Item.query.get_or_404(item_id)
        item.tags.add(tag)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            return abort(500, message=str(e))
        return tag

    @staticmethod
    @blp.response(204, TagDeleteSchema)
    def delete(item_id, tag_id):
        tag = Tag.query.get_or_404(tag_id)
        item = Item.query.get_or_404(item_id)
        item.tags.remove(tag)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            return abort(500, message=str(e))
        return {"message": "tag removed", "tag": tag, "item": item}