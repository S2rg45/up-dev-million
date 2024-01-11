# Path: test/test_routers.py
# Compare this snippet from app/main.py:
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
#
# # Importing routes
#
# from .services.change_price.routes import change_route
# from .services.create_property.routes import create_route
# from .services.image_property.routes import image_routes
#
# # Creating FastAPI instance
# app = FastAPI(title="Million API",
#               description="API for Million",
#               version="1.0.0")
#
# # CORS
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_property():
    response = client.post("/million/create_property/", 
                            json={
                                    "owner": {
                                        "name": "Jaun Caminloi",
                                        "address":  "132432",
                                        "photo": "field",
                                        "birthday": "2001/01/01"
                                    },
                                    "property": {
                                        "name": "agosto 20",
                                        "address": "carrera 71 --2s",
                                        "price": "1000000",
                                        "codeInternal": "1",
                                        "year": "2020/01/02"
                                    },
                                    "property_image": {
                                        "file": "/jpg",
                                        "enabled": True
                                    },
                                    "property_trace": {
                                        "dateSale": "",
                                        "name": "",
                                        "value": "",
                                        "tax": ""
                                }
                            })
    assert response.status_code == 200
    assert response.json() == {"result":"Created"}


def test_create_property_error():
    response = client.post("/million/create_property/", 
                            json={
                                    "owner": {
                                        "name": "1222",
                                        "address":  "Carrera",
                                        "photo": "",
                                        "birthday": "2001/01/01"
                                    },
                                    "property": {
                                        "name": "Juan Camilo",
                                        "address": "carrera 71 --2s",
                                        "price": "1000000",
                                        "codeInternal": "123",
                                        "year": "2020/01/02"
                                    },
                                    "property_image": {
                                        "file": "/jpg",
                                        "enabled": True
                                    },
                                    "property_trace": {
                                        "dateSale": "",
                                        "name": "",
                                        "value": "",
                                        "tax": ""
                                }
                            })
    
    assert response.status_code == 422
    assert response.json() == {
                                    "detail": [
                                        {
                                            "type": "string_too_short",
                                            "loc": [
                                                "body",
                                                "owner",
                                                "photo"
                                            ],
                                            "msg": "String should have at least 3 characters",
                                            "input": "",
                                            "ctx": {
                                                "min_length": 3
                                            },
                                            "url": "https://errors.pydantic.dev/2.4/v/string_too_short"
                                        }
                                    ]
                                }


def test_change_price():
    response = client.post("/million/change_price/", 
                            json={"property_owner": 
                            {"name": "luis Hamilton",
                                "address": "Carere"},
                                "change_price_property": 
                            {"name": "aranjuez", 
                                "address": "carrera 71 --2s",
                                "price": "124"}
                            })
    assert response.status_code == 200
    assert response.json() == {"result":"Change price property successfully"}


def test_change_price_error():
    response = client.post("/million/change_price/", 
                            json={"property_owner": 
                            {"name": "",
                                "address": "Carere"},
                                "change_price_property": 
                            {"name": "aranjuez", 
                                "address": "carrera 71 --2s",
                                "price": "124"}
                            })
    assert response.status_code == 422
    assert response.json() == {
                                "detail": [
                                    {
                                        "type": "string_too_short",
                                        "loc": [
                                            "body",
                                            "property_owner",
                                            "name"
                                        ],
                                        "msg": "String should have at least 3 characters",
                                        "input": "",
                                        "ctx": {
                                            "min_length": 3
                                        },
                                        "url": "https://errors.pydantic.dev/2.4/v/string_too_short"
                                    }
                                ]
                            }
    
    
def test_image_property_fail():
    response = client.post("/million/image_property/", 
                            json={"property_owner": 
                            {"name": "luis Hamilton",
                                "address": "Carere"},
                                "property_image": 
                            {"file": "/jpg",
                                "enabled": True}
                            })
    assert response.status_code == 404
    assert response.json() ==  {'detail': 'Not Found'} 








