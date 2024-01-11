import boto3
from dataclasses import dataclass, asdict
import aiofiles
from botocore.exceptions import ClientError
from ....config.settings import config

# instancia de la clase
class UpdateImageBucket:
    def __init__(self):
        self.client_s3 = boto3.client('s3', aws_access_key_id=config["local"]["AWS_ACCESS_ID"],
                                      aws_secret_access_key=config["local"]["AWS_ACCESS_KEY"])

    # --------------------------------------------------------------------------------
    # Method handle_file_upload
    def handle_file_upload(self, files) -> bool:
        """handle file upload
        params: files
        return: Bool"""
        # client s3 para generar la conexion
        client = self.client_s3
        aws_bucket_name = config["local"]["BUCKET_NAME"]
        # upload file
        for file in files:
            try:
                # upload file
                with aiofiles.open(file.file, "rb") as data:
                    # upload file dentro de un bucket de AWS con las credenciales
                    client.upload_fileobj(data, aws_bucket_name, file.filename)
            except ClientError as e:
                return False
        return True
