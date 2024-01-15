from fastapi import Header, APIRouter, HTTPException, File, UploadFile, Depends
import json
from fastapi.responses import JSONResponse

#Importar los modelos
from ....components.models.schemas import PropertyImageOwner, PropertyImageProperty
#Importar los servicios
from ..service.image_service import ImageService
#Importar la clase de validacion del token
from ....components.security.validate_token import OAuth2PasswordBearerWithCookie

#implementacion de la ruta
router = APIRouter(prefix="/million")
#instancia de la clase
image_service = ImageService()
#instancia de la clase
oauth2_scheme = OAuth2PasswordBearerWithCookie()

#endpoint para obtener la imagen de una propiedad
@router.post('/update_image/')
async def image(property_owner: PropertyImageOwner,
                image_property: PropertyImageProperty,
                file: UploadFile = File(...),
                current_access = Depends(oauth2_scheme.validate_token)) -> JSONResponse:
    """
    This function is used to get the image of the property
    :return: result of add images in bucket   
    """
    try:
        #request
        request = {
            "property_owner": property_owner,
            "image_property": image_property
        }
        #obtener el id del propietario
        data_owner = image_service.get_data_owner(dict(request.get("property_owner")))
        #actualizar el precio de la propiedad
        data_property = image_service.get_data_property(dict(request.get("image_property")), data_owner.get("IdOwner"))
        #actualizar la imagen de la propiedad
        image_service.update_images_bucket({"IdProperty": data_property}, file)
    except OSError as e:
        #response Exception
        raise HTTPException(status_code=400, detail="Exception")   
    #response  
    return  JSONResponse(content={"result": "Updated images in bucket"}, 
                        status_code=200)