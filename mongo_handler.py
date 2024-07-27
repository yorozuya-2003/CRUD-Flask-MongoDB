from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(
    host="db",
    port=27017,
    username=os.getenv('MONGO_INITDB_ROOT_USERNAME'),
    password=os.getenv('MONGO_INITDB_ROOT_PASSWORD'),
    authSource="admin",
)