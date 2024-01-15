from fastapi import Header, APIRouter, status, HTTPException, Response, Depends
import json
from fastapi.responses import JSONResponse

#Importar los modelos
from ....components.models.schemas import Property, PropertyTrace, PropertyImage, Owner
#Importar los servicios
from ..service.create_service import CreateService
#Importar la clase de validacion del token
from ....components.security.validate_token import OAuth2PasswordBearerWithCookie

#implementacion de la ruta
router = APIRouter(prefix="/million",
                   tags=["Million"])

#instancia de la clase
create_service = CreateService()
#instancia de la clase
oauth2_scheme = OAuth2PasswordBearerWithCookie()

#endpoint para crear una propiedad
@router.post('/create_property/',
             response_model_exclude_unset=True, 
             status_code=200)
async def property(owner: Owner, 
                   property: Property,
                   property_image: PropertyImage, 
                   property_trace: PropertyTrace, 
                   current_access = Depends(oauth2_scheme.validate_token)) -> JSONResponse:
    """
    This function is used for create property
    :return: json response with create property   
    """
    try:
        #request
        
        request = {
            "owner": owner,
            "property": property,
            "property_image": property_image,
            "property_trace": property_trace
        }
        #crear el propietario
        id_owner = create_service.create_owner(dict(request.get("owner"))) 
        #crear la propiedad
        id_property = create_service.create_property(dict(request.get("property")), id_owner)
        #crear la imagen y la traza de la propiedad
        create = create_service.create_property_image(dict(request.get("property_image")), id_property)
        #crear la traza de la propiedad
        response = create_service.create_property_trace(dict(request.get("property_trace")), id_property)
        #response
        return JSONResponse(content={"result":"Created"})
    except Exception as e:
        #response Exception
        print(e)
        raise HTTPException(status_code=400,detail=str(e)) from e  
