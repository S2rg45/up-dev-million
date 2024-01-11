from fastapi import Header, APIRouter, HTTPException, File, UploadFile
import json
from fastapi.responses import JSONResponse

from ....components.models.schemas import PropertyImageOwner, PropertyImageProperty
from ..service.image_service import ImageService


router = APIRouter(prefix="/million")
image_service = ImageService()


@router.post('/update_image/')
async def image(property_owner: PropertyImageOwner,
                image_property: PropertyImageProperty,
                file: UploadFile = File(...)) -> JSONResponse:
    """
    This function is used to get the image of the property
    :return: result of add images in bucket   
    """
    try:
        request = {
            "property_owner": property_owner,
            "image_property": image_property
        }

        data_owner = image_service.get_data_owner(dict(request.get("property_owner")))
        data_property = image_service.get_data_property(dict(request.get("image_property")), data_owner.get("IdOwner"))
        image_service.update_images_bucket({"IdProperty": data_property}, file)
    except OSError as e:
        raise HTTPException(status_code=400, detail="Exception")     
    return  JSONResponse(content={"result": "Updated images in bucket"}, 
                        status_code=200)