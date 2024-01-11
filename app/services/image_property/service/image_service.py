from datetime import datetime

#instancia de la clase
from ..store.image_store import ImageProperty
from .upload_service import UpdateImageBucket

#clase para el servicio
class ImageService:
    def __init__(self):
        self.store = ImageProperty()


    #obtener el id del propietario
    def get_data_owner(self, data):
        try:
            return  self.store.table_owner(data)
        except Exception as e:
            print(e)
            return False
        
        
    #obtener el id propiedad
    def get_data_property(self, data, id_owner):
        try:
            data["IdOwner"] = id_owner
            return self.store.table_property(data)
        except Exception as e:
            print(e)
            return False
        

    #actualizar la imagen de la propiedad
    def update_images_bucket(self, data_property, file):
        try:
            #actualizar la imagen de la propiedad dentro del bucket de AWS
            files = UpdateImageBucket.handle_file_upload(file)
            if files:
                update_date = {"file": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                #actualizar la fecha de la imagen dentro de la base de datos
                return self.store.table_property_image(data_property, update_date)
        except Exception as e:
            print(e)
            return False