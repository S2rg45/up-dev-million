import uuid
#importar la clase para crear la propiedad
from ..store.create_store import CreateProperty

#clase para el servicio
class CreateService:

    def __init__(self):
        self.store = CreateProperty()


    #crear la propiedad
    def create_property(self, data, id_owner: uuid.UUID):
        try:
            data_property = data
            id_property = uuid.uuid4().hex
            data_property["IdOwner"] = id_owner
            data_property["IdProperty"] = id_property
            self.store.table_property(data_property)
            return id_property
        except Exception as e:
            print(e)
            return False
        

    #crear la traza de la propiedad
    def create_property_trace(self, data, id_property: uuid.UUID):
        try:
            data_property_trace = data
            id_property_trace = uuid.uuid4().hex
            data_property_trace["IdPropertyTrace"] = id_property_trace
            data_property_trace["IdProperty"] = id_property
            self.store.table_property_trace(data_property_trace)
            return True
        except Exception as e:
            print(e)
            return False


    #crear la imagen de la propiedad
    def create_property_image(self, data, id_property: uuid.UUID):      
        try:
            data_property_image = data
            id_property_image = uuid.uuid4().hex
            data_property_image["IdPropertyImage"] = id_property_image
            data_property_image["IdProperty"] = id_property
            self.store.table_property_image(data_property_image)
            return True
        except Exception as e:
            print(e)
            return False
        

    #crear el propietario
    def create_owner(self, data):
        try:
            data_owner = data
            id_owner = uuid.uuid4().hex
            data_owner["IdOwner"] = id_owner
            self.store.table_owner(data_owner)
            return id_owner
        except Exception as e:
            return False