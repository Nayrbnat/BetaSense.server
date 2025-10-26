"""
BetaSense API - Vercel Serverless Entry Point
"""
import sys as _sys
from pathlib import Path as _Path

# Add parent directory to path so we can import betasense module
_project_root = _Path(__file__).parent.parent
_sys.path.insert(0, str(_project_root))

# Import FastAPI and setup app
from fastapi import FastAPI as _FastAPI
from betasense.src.routes import register_routes
from betasense.src.middleware.cors import setup_cors

# Create FastAPI app
app = _FastAPI(title="BetaSense API", version="1.0.0")

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

# Lazy import Mangum only when handler is called
# This prevents Vercel's inspection from finding Mangum class
def handler(event, context):
    """Vercel serverless function handler."""
    from mangum import Mangum
    asgi_handler = Mangum(app, lifespan="off")
    return asgi_handler(event, context)
