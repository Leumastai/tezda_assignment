
import requests
import json

def get_video_recommendations(user_id):
    # urls = ['https://tezda-images.s3.amazonaws.com/shortVideos/0dde45f98279700aa649783b45c391c0.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/0efb5672a1c7e9e0683f31a97eec0bc8.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/1818e44ced0eeaa5676393aa4ce97a91.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/1931bf56b1abc1a9f601b8ba5957fb70.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/1c001092a3b5105d4be173d3a58f5305.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/1c80ab421aaf309cbad642147b4112b5.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/26cbcb970c9963d063f7d587fe7ff5a9.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/41043c99690411d492b458f7c58de15e.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/4b40d87c36793bbf370868135e1a9907.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/58d5743b213dcef8a3d931217ac1c687.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/60d966598e7adf8879a741ab986386bb.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/70ca3b97f22088ee6bc4bc22e734ab79.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/7cbe8001605e39226a03bd7e715e0f5b.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/8314b8d54265ee994dfb3a19e52d8b6c.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/864f69ce13deace55f5dda5c71d4e8a3.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/93eca6b49eb656f26536572e588be8ff.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/98b9503dfe2b76b8bf06e4c787a45034.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/b6151a57fd74de9ee3bd0ca09bb82b45.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/bc53ea46479084e9c70168e374581ad5.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/c2a9bb601fd2f559f67db470202fdd1a.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/c59e9cfffc0cba73c9673131ac270009.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/c5a8744185a281978d31c1575232614c.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/db85c0fbb319209616e48467f5add57a.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/df382b18cef70d0c92131e4cf69efd0c.mp4', 'https://tezda-images.s3.amazonaws.com/shortVideos/ed4c428c6483d7b42dbc82c883095bcc.mp4']

    url = "http://127.0.0.1:5100/get_recommendation"

    payload = json.dumps({"user_id": f"{user_id}"})
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()