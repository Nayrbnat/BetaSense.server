"""
BetaSense API - Vercel Serverless Entry Point
"""
import sys
from pathlib import Path

# Add parent directory to path so we can import betasense module
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

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

# Create Mangum handler for AWS Lambda/Vercel compatibility
_asgi_handler = Mangum(app, lifespan="off")

# Export as 'handler' for Vercel
def handler(event, context):
    """Vercel serverless function handler."""
    return _asgi_handler(event, context)

# Explicitly define what should be exported
__all__ = ["handler", "app"]
