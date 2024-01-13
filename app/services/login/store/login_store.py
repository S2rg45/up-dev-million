
#instancia de la clase
from ....components.lib.connect_db import ConnectionDb
from ....config.settings import config

#clase para el almacenamiento
class LoginStore:

    def __init__(self):
        self.client = ConnectionDb()


    #validacion de la existencia del usuario
    def login_email(self, data):
        try:
            name_collection = config["local"]["collection_users_million"]
            return self.client.get_specific_data(data, name_collection)
        except Exception as e:
            return e



    #actualizar el precio de la propiedad
    def create_new_user(self, data):
        try:
            name_collection = config["local"]["collection_users_million"]
            return  self.client.insert_data_collection(data, name_collection)
        except Exception as e:
            print(e)
            return False



    


