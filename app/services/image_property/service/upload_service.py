import boto3
from dataclasses import dataclass, asdict
import aiofiles
from botocore.exceptions import ClientError
from ....config.settings import config


class UpdateImageBucket:
    def __init__(self):
        self.client_s3 = boto3.client('s3', aws_access_key_id=config["local"]["AWS_ACCESS_ID"],
                                      aws_secret_access_key=config["local"]["AWS_ACCESS_KEY"])


    def handle_file_upload(self, files) -> bool:
        """handle file upload
        params: files
        return: Bool"""
        client = self.client_s3
        aws_bucket_name = config["local"]["BUCKET_NAME"]

        for file in files:
            try:
                with aiofiles.open(file.file, "rb") as data:
                    client.upload_fileobj(data, aws_bucket_name, file.filename)
            except ClientError as e:
                return False
        return True
