from fastapi import Header, APIRouter, HTTPException, File, UploadFile, Depends
import json
from fastapi.responses import JSONResponse

from ....components.models.schemas import PropertyChangeOwner, PropertyChangePrice
from ..service.change_service import ChangePriceService
from ....components.security.validate_token import OAuth2PasswordBearerWithCookie

#implementacion de la ruta
router = APIRouter(prefix="/million")
#instancia de la clase
image_service = ChangePriceService()
#instancia de la clase
oauth2_scheme = OAuth2PasswordBearerWithCookie()

#endpoint para cambiar el precio de una propiedad
@router.post('/change_price/',
             response_model_exclude_unset=True, 
             status_code=200)
async def image(property_owner: PropertyChangeOwner,
                change_price_property: PropertyChangePrice,
                current_access = Depends(oauth2_scheme.validate_token)) -> JSONResponse:
    """
    This function is used to change price property
    :return: update price property  
    """
    try:
        #request
        request = {
            "property_owner": property_owner,
            "change_price_property": change_price_property
        }
        #obtener el id del propietario
        data_owner = image_service.get_data_owner(dict(request.get("property_owner")))
        #actualizar el precio de la propiedad
        data_property = image_service.update_price_property(dict(request.get("change_price_property")), data_owner.get("IdOwner"))
        #response
        return  JSONResponse(content={"result": "Change price property successfully"})   
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400,detail=str(e)) from e
         