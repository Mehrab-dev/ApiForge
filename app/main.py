
from fastapi import FastAPI

from app.shared.exceptions.exceptions import AppException
from app.shared.exceptions.exception_handlers import app_exception_handler
from app.core.logging.logging import setup_logging

setup_logging()


app = FastAPI()


app.add_exception_handler(AppException, app_exception_handler)