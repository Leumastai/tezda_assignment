import os
import sys
import logging
from dotenv import load_dotenv


## Logging
logFormatter = logging.Formatter(fmt="%(asctime)s:%(name)s:%(levelname)s:%(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# console handle
consleHandle = logging.StreamHandler()
consleHandle.setLevel(logging.INFO)
consleHandle.setFormatter(logFormatter)
logger.addHandler(consleHandle)

# file handler
fileHandler = logging.FileHandler(filename="info.log", mode="a+")
fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

# error handler
errorHandler = logging.FileHandler(filename="error.log", mode="a+")
errorHandler.setLevel(logging.ERROR)
errorHandler.setFormatter(logFormatter)
logger.addHandler(errorHandler)


## .env
dotenv_path = "backend/.env"
load_dotenv(dotenv_path)


## Secrets
access_id = os.environ.get("access_id")
secret_access_key = os.environ.get("secret_access_key")
campaign_arn = os.environ.get("campaign_arn")


config_params_dict = {
    "ACCESS_KEY_ID" : access_id,
    "SECRET_ACCESS_KEY" : secret_access_key,
    "CAMPAIGN_ARN" : campaign_arn,
}
