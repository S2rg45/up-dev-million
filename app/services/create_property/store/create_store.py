
from ....components.lib.connect_db import ConnectionDb
from ....config.settings import config



class CreateProperty:

    def __init__(self):
        self.client = ConnectionDb()


    def table_property(self, data):
        try:
            name_collection = config["local"]["collection_property"]
            insert_data = self.client.insert_data_collection(data, name_collection)
        except Exception as e:
            print(e)
            return False
        return True


    def table_property_trace(self, data):
        try:
            name_collection = config["local"]["collection_property_trace"]
            insert_data = self.client.insert_data_collection(data, name_collection)
        except Exception as e:
            print(e)
            return False
        return True


    def table_property_image(self, data):
        try:
            name_collection = config["local"]["collection_property_image"]
            insert_data = self.client.insert_data_collection(data, name_collection)
        except Exception as e:
            print(e)
            return False
        return True


    def table_owner(self, data):
        try:
            name_collection = config["local"]["collection_owner"]
            insert_data = self.client.insert_data_collection(data, name_collection)
        except Exception as e:
            print(e)
            return False
        return True


