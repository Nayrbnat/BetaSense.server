from pathlib import Path
import sys
import traceback
import asyncio
import json

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

project_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(project_root))
import betasense
from agent.entry import run_agent


router = APIRouter()


@router.post("/chat")
async def chat(session_id: str, user_input: str):
    return await run_agent(session_id, user_input)