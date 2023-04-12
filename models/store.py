from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship(
        "ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")  # lazy="dynamic" no se cargan los items hasta que nosotros le digamos
    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")
