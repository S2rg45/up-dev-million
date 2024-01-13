from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

#------------------------------------------------------------#
#------------------------ Schemas ---------------------------#
#------------------------------------------------------------#

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


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class DevItem(BaseModel):
    user: str


class User_Process_Files(BaseModel):
    username: str
    email: str  
    password: str


class User_process(BaseModel):
    name: str
    email: str
    password: str
    

class UserAuth(BaseModel):
    username: str
    email: str = Field(..., description="user email")
    password: str = Field(..., min_length=5, max_length=100, description="user password")


class UserLoginAuth(BaseModel):
    email: str
    password: str


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None