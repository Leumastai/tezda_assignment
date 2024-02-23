from marshmallow import Schema, fields, validate


class PostPayloadSchema(Schema):
    user_id = fields.Str(required=True)