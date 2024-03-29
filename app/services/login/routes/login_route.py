
from fastapi import Header, APIRouter, HTTPException, status, Depends
import json
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from ....components.models.schemas import UserLoginAuth
from ..service.login_service import LoginService

#implementacion de la ruta
router = APIRouter(prefix="/million")
#instancia de la clase
login_service = LoginService()

#endpoint para crear un nuevo usuario
@router.post('/login/',
             response_model_exclude_unset=True, 
             status_code=200)
async def login(data: UserLoginAuth) -> JSONResponse:
    """
    This function is used for validate login with user and password
    :return: token 
    """
    try:
        #request
        request = {
            "user": data
        }
        #validacion de la existencia del usuario
        data_user = login_service.login_with_data(dict(request.get("user")))
        if data_user is None:
            #response
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                content={"result":"Incorrect user or password"})  
        #Verificacion de la contraseña
        token = login_service.create_token(dict(request.get("user")), data_user)
        print(token)
        if token:
            #response
            return  JSONResponse(content={"result": token})   
        #response
        raise HTTPException(status_code=400,detail="Fail create")
    except Exception as e:
        #response Exception
        print(e)
        raise HTTPException(status_code=400,detail=str(e)) from e
