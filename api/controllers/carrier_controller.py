from fastapi import APIRouter, Query
from typing import Optional, List

# Schemas
from api.schemas.carrier_schemas import Carrier

# Repositories
from api.repositories import carrier_repository

# Utils
from api.utils.city_utils import extract_city_name

# Constants
from api.constants.error_constants import (
    INVALID_TOP_CARRIERS_QUERY_ERROR,
    TOP_CARRIERS_BY_DIRECTION_GETTING_ERROR,
)

router = APIRouter(prefix="/carriers", tags=["Carriers"])


@router.get("/top-by-direction", response_model=Optional[List[Carrier]])
def getTopCarriersByDirection(from_city: str = Query(None), to_city: str = Query(None)):
    if not from_city or not to_city:
        INVALID_TOP_CARRIERS_QUERY_ERROR.raise_exception()
    
    from_city_name = extract_city_name(from_city)
    to_city_name = extract_city_name(to_city)

    try:
        return carrier_repository.get_top_carriers_by_direction(from_city_name, to_city_name)
    except Exception as e:
        TOP_CARRIERS_BY_DIRECTION_GETTING_ERROR.raise_exception(exception=e)
