from fastapi import Header, APIRouter, HTTPException, File, UploadFile
import json
from fastapi.responses import JSONResponse

from ....components.models.schemas import PropertyChangeOwner, PropertyChangePrice
from ..service.change_service import ChangePriceService


router = APIRouter(prefix="/million")
image_service = ChangePriceService()


@router.post('/change_price/',
             response_model_exclude_unset=True, 
             status_code=200)
async def image(property_owner: PropertyChangeOwner,
                change_price_property: PropertyChangePrice) -> JSONResponse:
    """
    This function is used to change price property
    :return: update price property  
    """
    try:
        request = {
            "property_owner": property_owner,
            "change_price_property": change_price_property
        }

        data_owner = image_service.get_data_owner(dict(request.get("property_owner")))
        data_property = image_service.update_price_property(dict(request.get("change_price_property")), data_owner.get("IdOwner"))
        return  JSONResponse(content={"result": "Change price property successfully"})   
    except Exception as e:
        raise HTTPException(status_code=400,content={"result": "Fail change price property"} ,detail="Exception") from e    
         