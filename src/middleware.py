from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import time
import logging
from .config import version

logger = logging.getLogger("uvicorn.access")
logger.disabled = True


def register_middleware(app: FastAPI):

    @app.middleware("http")
    async def custom_logging(request: Request, call_next):
        start_time = time.time()

        response = await call_next(request)
        processing_time = time.time() - start_time

        message = f"{request.client.host}:{request.client.port} - {request.method} - {
            request.url.path} - {response.status_code} completed after {processing_time}s"

        print(message)
        return response

    # @app.middleware("http")
    # async def missing_auth_header (request: Request, call_next):
    #     print(request.url.path)
    #     if not "Authorization" in request.headers and request.url.path != f"/api/{version}/docs":
    #         return JSONResponse(
    #             status_code=status.HTTP_401_UNAUTHORIZED,
    #             content={"message": "Missing Authorization header"},
    #         )
    #     return await call_next(request)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["localhost", "127.0.0.1",
                       "bookly-api-dc03.onrender.com", "0.0.0.0"],
    )
