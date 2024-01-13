from datetime import datetime

#instancia de la clase
from ..store.login_store import LoginStore
from ....components.security.utils_token import SettingsToken

#clase para el servicio
class LoginService:
    def __init__(self):
        self.store = LoginStore()
        self.settings_token = SettingsToken()

    #validacion de la existencia del usuario
    def login_with_data(self, data):
        try:
            email = {"email": data.get("email")}
            return  self.store.login_email(email)
        except Exception as e:
            print(e)
            return False
        
    #crear nuevo usuario
    def verify_password(self, data, data_db):
        try:
            password = self.settings_token.verify_password(data.get("password"), data_db.get("password"))
            return {"token": self.settings_token.create_access_token(password)}
        except Exception as e:
            print(e)
            return False