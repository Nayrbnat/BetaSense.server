from fastapi import FastAPI
from .chatapi import router as chatapi_router

def register_routes(app: FastAPI):
    app.include_router(chatapi_router)