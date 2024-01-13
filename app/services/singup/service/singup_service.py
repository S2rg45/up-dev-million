from datetime import datetime

#instancia de la clase
from ..store.singup_store import SingupStore
from ....components.security.utils_token import SettingsToken

#clase para el servicio
class SingUpService:
    def __init__(self):
        self.store = SingupStore()
        self.settings_token = SettingsToken()

    #validacion de la existencia del usuario
    def get_data_user(self, data):
        try:
            email = {"email": data.get("email")}
            return  self.store.validate_email_user(email)
        except Exception as e:
            print(e)
            return False
        
    #crear nuevo usuario
    def create_new_user(self, data):
        try:
            password = self.settings_token.hashed_password(data.get("password"))
            data["password"] = password
            return self.store.create_new_user(data)
        except Exception as e:
            print(e)
            return False