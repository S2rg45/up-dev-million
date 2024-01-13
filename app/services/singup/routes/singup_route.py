from fastapi import Header, APIRouter, HTTPException, status
import json
from fastapi.responses import JSONResponse

from ....components.models.schemas import UserAuth
from ..service.singup_service import SingUpService

#implementacion de la ruta
router = APIRouter(prefix="/million")
#instancia de la clase
singup_service = SingUpService()

#endpoint para crear un nuevo usuario
@router.post('/singup/',
             response_model_exclude_unset=True, 
             status_code=200)
async def signup(data: UserAuth) -> JSONResponse:
    """
    This function is used to create a new user
    :return: create new user  
    """
    try:
        #request
        request = {
            "user": data
        }
        #validacion de la existencia del usuario
        data_user = singup_service.get_data_user(dict(request.get("user")))
        if data_user is not None:
            print(data_user.get("email"))
            #response
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                content={"result":"User with this email already exist"})  
        #crear un nuevo usuario
        create_user = singup_service.create_new_user(dict(request.get("user")))
        if create_user:
            #response
            return  JSONResponse(content={"result": "Create new user successfully"})   
        #response
        raise HTTPException(status_code=400,detail="Fail create new user")
    except Exception as e:
        #response Exception
        print(e)
        raise HTTPException(status_code=400,detail=str(e)) from e