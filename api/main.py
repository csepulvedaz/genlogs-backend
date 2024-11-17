from logging.config import dictConfig

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

# Constants
from api.constants.error_constants import VALIDATION_ERROR

# Routes
from api.controllers.root_controller import router as root_routes

# Config
from api.core.config import (
    app_config,
    logs_config,
)


dictConfig(logs_config)

app = FastAPI(**app_config)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_, exc: RequestValidationError):
    return VALIDATION_ERROR.send(validation_error=exc)


app.include_router(root_routes)
