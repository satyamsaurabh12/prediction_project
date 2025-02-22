from pymongo.mongo_client import MongoClient
import pandas as pd
import json
from urllib.parse import quote_plus
username = "shashank"
password = "PGA@xe6uq7hQ-sB"  # Contains special characters

encoded_password = quote_plus(password)

uri = f"mongodb+srv://{username}:{encoded_password}@cluster0.hndf4.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

client = MongoClient(uri, tls=True, tlsAllowInvalidCertificates=True)

# create database name and collection name
DATABASE_NAME= "dataset"
COLLECTION_NAME = "waferfault"
df = pd.read_csv(r"C:\Users\satyam saurabh\Downloads\Sensor_project\notebooks\wafer_23012020_041211.csv")
df = df.drop("Unnamed: 0",axis =1)
json_record = list(json.loads(df.T.to_json()).values())



