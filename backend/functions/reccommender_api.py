

from backend.functions.utils import aws_connection
from backend.config.settings import config_params_dict


client = aws_connection()

def get_recommendations(user_id: str, num_resulst: int = 25):
    recommendations = client.get_recommendations(
        campaignArn = config_params_dict['CAMPAIGN_ARN'],
        userId = user_id,
        numResults = num_resulst)
    
    item_ids = [items['itemId'] for items in recommendations['itemList']]
    
    return item_ids


if __name__ == "__main__":
    user_id = "22e7ff9d170ec82d8209abe6379a7d80"
    print (get_recommendations(user_id))
    





