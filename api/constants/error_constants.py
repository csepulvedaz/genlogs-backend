from fastapi import status
from api.schemas.error_schemas import ErrorResponse

# Carrier errors messages
INVALID_TOP_CARRIERS_QUERY_ERROR = ErrorResponse(
    message="Invalid query parameters",
    status_code=status.HTTP_400_BAD_REQUEST,
)
TOP_CARRIERS_BY_DIRECTION_GETTING_ERROR = ErrorResponse(
    message="Error getting top carriers by direction",
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
)


# Data validation errors messages
VALIDATION_ERROR = ErrorResponse(
    message="One or more fields are missing or wrong",
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
)
