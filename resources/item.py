from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
# Todos los errores de SQLAlchemy heredan de este error
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", __name__, description="Operations on items")


@blp.route("/item/<int:item_id>")
class Item(MethodView):
    # Decorate main success response, pasa lo que retornemos por ItemSchema,
    @jwt_required()
    @blp.response(200, ItemSchema)
    def get(self, item_id):  # Endpoint to get an item
        # Query available with Flask-SQLAlchemy and not with VAnilla SQLAlchemy
        item = ItemModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):  # Endpoint to delete an item
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted."}

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    # Si existe se actualiza y si no existe se crea para mantener la idempotencia
    def put(self, item_data, item_id):  # Endpoint to update an item
        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)

        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/item")
class ItemList(MethodView):
    @jwt_required()
    @blp.response(200, ItemSchema(many=True))
    def get(self):  # Endpoint to get all items
        return ItemModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):  # Endpoint to create an item
        # item_data contains JSON which is the validated fields that Scheme requested
        # Unpack item_data and pass it as keyword arguments
        item = ItemModel(**item_data)

        try:
            db.session.add(item)  # Not written to db file
            db.session.commit()  # Written on db file
        except SQLAlchemyError:
            abort(500, message="An error ocurred while inserting the item.")

        return item, 201
