from fastapi import FastAPI

from noio.api.router import v1


api = FastAPI()

api.include_router(router=v1, prefix="/api/v1")
