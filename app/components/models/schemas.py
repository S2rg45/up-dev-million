from pydantic import BaseModel, Field
from typing import Optional

class Owner(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    address: str = Field(..., min_length=3, max_length=50)
    photo: str = Field(..., min_length=3, max_length=50)
    birthday: str = Field(..., min_length=3, max_length=50)


class Property(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    address: str = Field(..., min_length=3, max_length=50)
    price: str = Field(..., min_length=3, max_length=50)
    codeInternal: str = Field(..., max_length=10)
    year: str = Field(..., min_length=3, max_length=50)


class PropertyImage(BaseModel):
    file: Optional[str] = None
    enabled: bool 


class PropertyTrace(BaseModel):
    dateSale: str 
    name: str 
    value: str 
    tax: str 


class PropertyImageOwner(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    address: str = Field(..., min_length=3, max_length=50)


class PropertyImageProperty(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    address: str = Field(..., min_length=3, max_length=50)


class PropertyChangeOwner(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    address: str = Field(..., min_length=3, max_length=50)


class PropertyChangePrice(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    address: str = Field(..., min_length=3, max_length=50)
    price: str = Field(..., min_length=3, max_length=50)


