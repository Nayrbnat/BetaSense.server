from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def setup_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:1000",
            "http://localhost:2000",
            "http://localhost:3000",
            "http://localhost:4000",
            "http://localhost:5000",
            "http://localhost:6000",
            "http://localhost:7000",
            "http://localhost:8000",
            "http://localhost:9000",
            "http://localhost:10000",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )