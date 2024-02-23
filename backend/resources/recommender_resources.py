from marshmallow import ValidationError
from flask_restful import Resource
from flask import request
from typing import *


from backend.resources.payloads import PostPayloadSchema
from backend.config.settings import logger

class PostItemID(Resource):
    def post(self):

        from backend.functions.main import execute
        try:
            req_data = request.get_json()
            data = PostPayloadSchema().load(req_data)

            user_id = data.get("user_id")

            rec_urls = execute(user_id)

            response = {
                "s3_url": rec_urls,
                "status": "success",
                "message": "Post successfully uploaded",
            }

            return response, 200

        except ValidationError as reason:
            logger.exception(f"Exception occured :--: \n\t{reason}")
            return {"status": False,
                     "message": reason.messages_dict if not isinstance(reason.messages, list) else reason.messages,
                       "data": None}, 400
        except Exception as reason:
            logger.exception(f"Exception occured :--: \n\t{reason}")
            return {"status": False, "message": str(reason)}, 500


