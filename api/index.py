"""
BetaSense API - Vercel Serverless Entry Point
"""

# Global app instance - initialized on first request
_app_instance = None

def _get_app():
    """Initialize FastAPI app lazily."""
    global _app_instance
    if _app_instance is None:
        import sys
        from pathlib import Path
        
        # Add parent directory to path
        project_root = Path(__file__).parent.parent
        sys.path.insert(0, str(project_root))
        
        from fastapi import FastAPI
        from betasense.src.routes import register_routes
        from betasense.src.middleware.cors import setup_cors
        
        # Create FastAPI app
        _app_instance = FastAPI(title="BetaSense API", version="1.0.0")
        
        # Setup CORS and routes
        setup_cors(_app_instance)
        register_routes(_app_instance)
        
        # Root endpoint for health check
        @_app_instance.get("/")
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
    
    return _app_instance

# Vercel serverless function handler
def handler(event, context):
    """Vercel serverless function handler."""
    from mangum import Mangum
    app = _get_app()
    asgi_handler = Mangum(app, lifespan="off")
    return asgi_handler(event, context)
