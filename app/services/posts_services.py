import pymongo
import os

database_name = os.getenv("DATABASE")
database_collection = os.getenv("DATABASE_COLLECTION")

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client[f"{database_name}"]

def increment_id():
    posts_list = list(db.get_collection(database_collection).find())
    return posts_list[-1]["id"] + 1 if len(posts_list) != 0 else 1