from pathlib import Path
import sys
import json

from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

project_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(project_root))
import betasense
from agent.entry import run_agent


router = APIRouter()


class ChatRequest(BaseModel):
    session_id: str
    user_input: str
    password: str


@router.post("/chat")
async def chat(request: ChatRequest):
    print("Received chat request:", request)
    if request.password != "yourmumgay":
        raise HTTPException(status_code=403, detail="Forbidden")
    
    async def event_generator():
        """Generate SSE events from agent stream"""
        print("Starting event generator")
        try:
            async for event_data in run_agent(request.session_id, request.user_input):
                yield f"data: {json.dumps(event_data)}\n\n"
        except Exception as e:
            error_data = {
                "type": "error",
                "content": str(e),
                "status_code": 500
            }
            yield f"data: {json.dumps(error_data)}\n\n"
    
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        }
    )