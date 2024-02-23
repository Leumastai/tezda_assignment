from flask_restful import Api, Resource
from flask import Blueprint, jsonify

from resources.recommender_resources import PostItemID

class Home(Resource):
    def get(self):
        return jsonify({
            "message": "Tezda Video Recommender API"})

recc_blueprint = Blueprint(
    "recc_blueprint", __name__
)

api = Api(recc_blueprint)

api.add_resource(PostItemID, "/get_recommendation")
api.add_resource(Home, "/")
