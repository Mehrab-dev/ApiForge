
from fastapi import Request
from fastapi.responses import JSONResponse

from typing import cast


from app.shared.exceptions.exceptions import AppException



async def app_exception_handler(
    request: Request,
    exc: Exception
) -> JSONResponse:
    exc = cast(AppException, exc)
    return JSONResponse(
        status_code=exc.status_code,
        content= {
            "detail" : exc.message
        }
    )