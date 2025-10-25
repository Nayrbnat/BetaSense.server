from fastapi import FastAPI

import betasense
from routes import register_routes
from middleware.cors import setup_cors


app = FastAPI()


setup_cors(app)
register_routes(app)