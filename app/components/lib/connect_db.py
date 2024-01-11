from pymongo import MongoClient
import motor.motor_asyncio
from ...config.settings import config


class ConnectionDb:
    def __init__(self, host=config["local"]["connection"], db_name=config["local"]["db"]):
        # Establecer conexión a MongoDB
        self.client = MongoClient(host)
        self.db = self.client[db_name]


    def close_connection(self):
        self.client.close()


    def get_collection_data(self, collection_name):
        collection = self.db[collection_name]
        return collection.find({})
    
    def get_specific_data(self, query, collection_name):
        collection = self.db[collection_name]
        return collection.find_one(query)
    

    def get_data_and_update(self, query, update_query ,collection_name):
        collection = self.db[collection_name]
        return collection.find_one_and_update(query, {"$set": update_query})
    

    def get_all_collections(self):
        return self.db.list_collection_names()


    def insert_data_collection(self, data, collection_name):
        insert_data = self.db[collection_name].insert_one(data)
        return insert_data
    