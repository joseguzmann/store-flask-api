from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    # dump_only: el dato solo se puede definir durante la serializacion para devolver al front
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)  # Required in both ends
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
