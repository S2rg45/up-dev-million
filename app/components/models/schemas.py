from pydantic import BaseModel
from typing import Optional

class Owner(BaseModel):
    name: str
    address: str
    photo: str
    birthday: str


class Property(BaseModel):
    name: str
    address: str
    price: str
    codeInternal: str
    year: str


class PropertyImage(BaseModel):
    file: Optional[str] = None
    enabled: bool 


class PropertyTrace(BaseModel):
    dateSale: str 
    name: str 
    value: str 
    tax: str 


class PropertyImageOwner(BaseModel):
    name: str
    address: str


class PropertyImageProperty(BaseModel):
    name: str
    address: str


class PropertyChangeOwner(BaseModel):
    name: str
    address: str


class PropertyChangePrice(BaseModel):
    name: str
    address: str
    price: str


