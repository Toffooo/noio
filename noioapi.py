from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from noio.api.router import v1


api = FastAPI()
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
api.include_router(
    router=v1,
    prefix="/api/v1"
)
