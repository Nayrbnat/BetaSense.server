"""
BetaSense API - Vercel Serverless Entry Point
For ASGI apps like FastAPI, export 'app' variable (not 'handler')
"""
import sys
from pathlib import Path

# Add parent directory to path so we can import betasense module
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from fastapi import FastAPI
from betasense.src.routes import register_routes
from betasense.src.middleware.cors import setup_cors

# Create FastAPI app - Vercel will auto-detect this as ASGI
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
