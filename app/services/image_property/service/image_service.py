from datetime import datetime


from ..store.image_store import ImageProperty
from .upload_service import UpdateImageBucket


class ImageService:
    def __init__(self):
        self.store = ImageProperty()


    def get_data_owner(self, data):
        try:
            return  self.store.table_owner(data)
        except Exception as e:
            print(e)
            return False
        
    
    def get_data_property(self, data, id_owner):
        try:
            data["IdOwner"] = id_owner
            return self.store.table_property(data)
        except Exception as e:
            print(e)
            return False
        
    
    def update_images_bucket(self, data_property, file):
        try:
            files = UpdateImageBucket.handle_file_upload(file)
            if files:
                update_date = {"file": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                return self.store.table_property_image(data_property, update_date)
        except Exception as e:
            print(e)
            return False