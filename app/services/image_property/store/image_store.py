
from ....components.lib.connect_db import ConnectionDb
from ....config.settings import config


# --------------------------------------------------------------------------------
# Class ImageProperty
class ImageProperty:

    def __init__(self):
        self.client = ConnectionDb()

    # obtener datos del id de la propiedad
    def table_property(self, data):
        try:
            name_collection = config["local"]["collection_property"]
            data_property = self.client.get_specific_data(data, name_collection)
        except Exception as e:
            print(e)
            return False
        return data_property


    # Actualizar la fecha dentro de la colección 
    def table_property_image(self, data, update_data):
        try:
            name_collection = config["local"]["collection_property_image"]
            insert_data = self.client.get_data_and_update(data, update_data, name_collection)
        except Exception as e:
            print(e)
            return False
        return True


    # obtener el id del Owner
    def table_owner(self, data):
        try:
            name_collection = config["local"]["collection_owner"]
            data_owner = self.client.get_specific_data(data, name_collection)
        except Exception as e:
            return e
        return data_owner


