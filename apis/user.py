from db import db
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas import UserSchema
from models import User
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
blp = Blueprint("users", __name__, url_prefix="/api/user", description="operations on tags")


@blp.route("")
class Register(MethodView):
    @staticmethod
    @blp.arguments(UserSchema)
    @blp.response(201, description="user created successfully", example={"message": "user created"})
    def post(data):
        try:
            data["password"] = pbkdf2_sha256.hash(data["password"])
            user = User(**data)
            db.session.add(user)
            db.session.commit()
            return {"message": "user created"}, 201
        except IntegrityError:
            abort(400, message="username already exists")
        except SQLAlchemyError as e:
            abort(400, message=str(e))


@blp.route("/login")
class Login(MethodView):
    @staticmethod
    @blp.arguments(UserSchema)
    @blp.response(200, description="user login in successfully", example={"access": "<access_token>",
                                                                         "refresh":"<refresh_token>"})
    @blp.alt_response(408, description="if not valid credentials")
    def post(data):
        user = User.query.filter(User.username == data["username"]).first()
        if user and pbkdf2_sha256.verify(data["password"], user.password):
            identity = {"id": user.id, "username": user.username}
            access = create_access_token(identity=identity)
            refresh = create_refresh_token(identity=identity)

            return {
                "access": access,
                "refresh": refresh
            }, 200

        abort(408, message="not valid credentials")


@blp.route("/profile")
class Login(MethodView):

    @staticmethod
    @jwt_required()
    @blp.response(200, UserSchema)
    def get():
        current_user_identity = get_jwt_identity()
        user_id = current_user_identity.get("id")
        username = current_user_identity.get("username")
        return {"id": user_id, "username": username}


@blp.route("/refresh")
class Refresh(MethodView):
    @staticmethod
    @jwt_required(refresh=True)
    @blp.response(200, description="get access token from refresh token", example={"access": "<access_token>"})
    def get():
        current_user_identity = get_jwt_identity()
        access = create_access_token(identity=current_user_identity)
        return {"access": access}
