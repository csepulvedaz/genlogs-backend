from fastapi import status
from api.schemas.error_schemas import ErrorResponse

# Data validation errors messages
VALIDATION_ERROR = ErrorResponse(
    message="One or more fields are missing or wrong",
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
)
