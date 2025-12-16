from fastapi import Request
from fastapi.responses import JSONResponse
from starlette import status

from app.domain.exceptions import base



def already_exists_handler(_: Request, e: base.AlreadyExistsError) -> JSONResponse:
    return JSONResponse(content={"message": str(e)}, status_code=status.HTTP_409_CONFLICT)

def not_found_handler(_: Request, e: base.NotFoundError) -> JSONResponse:
    return JSONResponse(content={"message": str(e)}, status_code=status.HTTP_404_NOT_FOUND)

def auth_error_handler(_: Request, exc: base.AuthError):
    return JSONResponse(content={"detail": str(exc)}, status_code=status.HTTP_401_UNAUTHORIZED)