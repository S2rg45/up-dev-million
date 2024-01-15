
#instancia de la clase
from ....components.lib.connect_db import ConnectionDb
from ....config.settings import config

#clase para el almacenamiento
class ValidateStore:

    def __init__(self):
        self.client = ConnectionDb()


    #validacion de la existencia del usuario
    def validate_token(self, data):
        try:
            print(data)
            name_collection = config["local"]["collection_users_million"]
            return self.client.get_specific_data(data, name_collection)
        except Exception as e:
            return e



   


    


