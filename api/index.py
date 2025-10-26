import sys
import os
from pathlib import Path

# Add parent directory to path so we can import betasense module
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Also add the betasense directory itself
betasense_path = project_root / "betasense"
if betasense_path.exists():
    sys.path.insert(0, str(betasense_path))

from fastapi import FastAPI
from mangum import Mangum

from betasense.src.routes import register_routes
from betasense.src.middleware.cors import setup_cors

# Create FastAPI app
app = FastAPI(title="BetaSense API", version="1.0.0")

# Setup CORS and routes
setup_cors(app)
register_routes(app)

# Root endpoint for health check
@app.get("/")
def read_root():
    return {
        "message": "BetaSense API is running",
        "status": "ok",
        "endpoints": {
            "chat": {
                "path": "/chat",
                "method": "POST",
                "description": "Chat endpoint for BetaSense agent",
                "required_fields": ["session_id", "user_input", "password"]
            }
        }
    }

# Mangum handler for Vercel serverless
handler = Mangum(app, lifespan="off")
