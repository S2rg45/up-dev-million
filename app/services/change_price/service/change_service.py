from datetime import datetime


from ..store.change_store import ChangePrice
from ....config.settings import config



class ChangePriceService:
    def __init__(self):
        self.store = ChangePrice()


    def get_data_owner(self, data):
        try:
            return  self.store.table_owner(data)
        except Exception as e:
            print(e)
            return False
        
    
    def update_price_property(self, data_property, id_owner):
        try:
            data_property["IdOwner"] = id_owner
            new_price =  {"price": data_property.get("price")}
            del data_property["price"]

            return self.store.table_property_price(data_property, new_price)
        except Exception as e:
            print(e)
            return False