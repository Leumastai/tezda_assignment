from backend.functions.reccommender_api import get_recommendations
from backend.functions.utils import items_mapper

def execute(user_id):

    item_ids = get_recommendations(user_id)
    s3_vids_url = items_mapper(item_ids)

    return s3_vids_url

