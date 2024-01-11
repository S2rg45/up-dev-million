from fastapi import Header, APIRouter, status, HTTPException, Response
import json
from fastapi.responses import JSONResponse

from ....components.models.schemas import Property, PropertyTrace, PropertyImage, Owner
from ..service.create_service import CreateService


router = APIRouter(prefix="/million",
                   tags=["Million"])

create_service = CreateService()

@router.post('/create_property/')
async def property(owner: Owner, 
                   property: Property,
                   property_image: PropertyImage, 
                   property_trace: PropertyTrace) -> JSONResponse:
    try:
        request = {
            "owner": owner,
            "property": property,
            "property_image": property_image,
            "property_trace": property_trace
        }
        
        id_owner = create_service.create_owner(dict(request.get("owner"))) 
        id_property = create_service.create_property(dict(request.get("property")), id_owner)
        create_service.create_property_image(dict(request.get("property_image")), id_property)
        create_service.create_property_trace(dict(request.get("property_trace")), id_property)
    except OSError as e:
        raise HTTPException(status_code=400, detail="Exception")
    return JSONResponse(content={"result":"Created"}, 
                    status_code=201)