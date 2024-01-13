import os
from dotenv import load_dotenv

load_dotenv()

# Configuración de entorno
config = {
  "local": {
    "connection": os.getenv("URI_DB_MONGO_LOCAL"),
    "host": os.getenv("LOCAL_HOST"),
    "port": os.getenv("PORT_DB"),
    "db": os.getenv("DB_NAME"),
    "collection_owner": os.getenv("COLLECTION_OWNER"),
    "collection_property": os.getenv("COLLECTION_PROPERTY"),
    "collection_property_image": os.getenv("COLLECTION_PROPERTY_IMAGE"),
    "collection_property_trace": os.getenv("COLLECTION_PROPERTY_TRACE"),
    "path_bucket": os.getenv("PATH_BUCKET"),
    "AWS_ACCESS_ID": os.getenv("AWS_ACCESS_ID"),
    "AWS_ACCESS_KEY": os.getenv("AWS_ACCESS_KEY"),
    "AWS_REGION": os.getenv("AWS_REGION"),
    "BUCKET_NAME": os.getenv("BUCKET_NAME"),
    "algorithm": os.getenv("ALGORITHM"),
    "jwt_secret_key": os.getenv("JWT_SECRET_KEY"),
    "jwt_refresh_secret_key": os.getenv("JWT_REFRESH_SECRET_KEY"),
    "access_token_expire_minutes": os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"),
    "refresh_token_expire_minutes": os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES"),
    "collection_users_million": os.getenv("COLLECTION_USERS_MILLION"),
  },
  "development": {
    "connection": os.getenv("URI_DB_MONGO_DEV")
  },
  "test": {
    "connection" : os.getenv("URI_DB_MONGO_TEST")
  }
}