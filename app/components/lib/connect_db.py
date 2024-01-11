from pymongo import MongoClient
import motor.motor_asyncio
from ...config.settings import config

# --------------------------------------------------------------------------------
# Class ConnectionDb donde se obtiene la conexión a la base de datos
class ConnectionDb:
    def __init__(self, host=config["local"]["connection"], db_name=config["local"]["db"]):
        # Establecer conexión a MongoDB
        self.client = MongoClient(host)
        self.db = self.client[db_name]

    # --------------------------------------------------------------------------------
    # Method close_connection
    def close_connection(self):
        self.client.close()


    # se otiene todos los datos de la colección
    def get_collection_data(self, collection_name):
        collection = self.db[collection_name]
        return collection.find({})
    

    # se obtiene un dato especifico de la colección
    def get_specific_data(self, query, collection_name):
        collection = self.db[collection_name]
        return collection.find_one(query)
    

    # se obtiene un dato especifico de la colección y se actualiza
    def get_data_and_update(self, query, update_query ,collection_name):
        collection = self.db[collection_name]
        return collection.find_one_and_update(query, {"$set": update_query})
    

    # Se obtienen todas las coleccion de la base de datos
    def get_all_collections(self):
        return self.db.list_collection_names()


    # se inserta un dato en la colección
    def insert_data_collection(self, data, collection_name):
        insert_data = self.db[collection_name].insert_one(data)
        return insert_data
    