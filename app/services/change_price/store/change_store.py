
from ....components.lib.connect_db import ConnectionDb
from ....config.settings import config


class ChangePrice:

    def __init__(self):
        self.client = ConnectionDb()


    def table_owner(self, data):
        try:
            name_collection = config["local"]["collection_owner"]
            data_owner = self.client.get_specific_data(data, name_collection)
        except Exception as e:
            return e
        return data_owner


    def table_property_price(self, data, update_data):
        try:
            name_collection = config["local"]["collection_property"]
            insert_data = self.client.get_data_and_update(data, update_data, name_collection)
        except Exception as e:
            print(e)
            return False
        return True


    


