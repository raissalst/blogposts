import datetime
import pymongo
from app.exc.wrong_keys_error import WrongKeysError
from app.exc.not_found_error import NotFoundError
import os

database_name = os.getenv("DATABASE")
database_collection = os.getenv("DATABASE_COLLECTION")

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client[database_name]

class Post:

    def __init__(
        self, title: str, author: str, tags: list[str], content: str
    ) -> None:
        self.id = self.increment_id()
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()
        self.title = str(title).title()
        self.author = str(author).title()
        self.tags = tags if type(tags) == list else self.not_list_type()
        self.content = str(content).capitalize()

    
    def not_list_type(self):
        raise NotListTypeError
    
    def increment_id(self):
        posts_list = list(db.get_collection(database_collection).find())
        return posts_list[-1]["id"] + 1 if len(posts_list) != 0 else 1

    def new_post(self):
            db.get_collection(database_collection).insert_one(self.__dict__)

    # @staticmethod
    # def serialize_posts(data):
    #     if type(data) is list:
    #         for post in data:
    #             post.update({"_id": str(post["_id"])})
    #     elif type(data) is Post:
    #         data._id = str(data._id)
    #     elif type(data) is dict:
    #         data.update({"_id": str(data["_id"])})   

    @staticmethod
    def get_posts():
        posts_list = db.get_collection(database_collection).find()
        return posts_list

    @staticmethod
    def delete_post(id):
        deleted_post = db.get_collection(database_collection).find_one_and_delete({"id": id})
        return deleted_post
    
    @staticmethod
    def filter_post(id):
        filtered_post = db.get_collection(database_collection).find_one({"id": id})

        if filtered_post != None:
            del filtered_post["_id"]
            return filtered_post
        else:
            raise NotFoundError
    
    @staticmethod
    def update_post(id, data):

        data["updated_at"] = datetime.datetime.utcnow()
        updated_post = db.get_collection(database_collection).find_one_and_update({"id": id}, {"$set": data}, return_document=True)
        
        return updated_post

    @classmethod
    def check_keys_received(cls, received_keys: list):
        array_of_wrong_keys = []
        array_of_valid_keys = os.getenv('VALID_KEYS').split(",")

        for key in received_keys:
            if key not in array_of_valid_keys:
                array_of_wrong_keys.append(key)
        
        return array_of_wrong_keys