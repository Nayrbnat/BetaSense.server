from fastapi import FastAPI
from mangum import Mangum

import betasense
from betasense.src.routes import register_routes
from betasense.src.middleware.cors import setup_cors

# Create FastAPI app
app = FastAPI()

# Setup CORS and routes
setup_cors(app)
register_routes(app)

# Root endpoint for health check
@app.get("/")
def read_root():
    return {"message": "BetaSense API is running", "status": "ok"}

# Mangum handler for Vercel serverless
handler = Mangum(app)
