import urllib.parse
import os

AWS_S3_BUCKET_NAME = "wafer-fault"
MONGO_DATABASE_NAME = "dataset"
MONGO_COLLECTION_NAME = "waferfault"

TARGET_COLUMN = "quality"

# Encode the username and password properly
username = urllib.parse.quote_plus("shashank")
password = urllib.parse.quote_plus("PGA@xe6uq7hQ-sB")

MONGO_DB_URL = f"mongodb+srv://{username}:{password}@cluster0.hndf4.mongodb.net/?retryWrites=true&w=majority"

MODEL_FILE_NAME = ""
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder = "artifacts"
