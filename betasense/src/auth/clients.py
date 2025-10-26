import os
from uuid import uuid4

from dotenv import load_dotenv
from openai import AsyncOpenAI
from sqlalchemy.ext.asyncio import create_async_engine
import httpx


load_dotenv(".env")


def openai_client():
    return AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def sqlalchemy_client():
    return create_async_engine(
        os.getenv("SUPABASE_DATABASE_URL"),
        connect_args={
            "prepared_statement_name_func": lambda: f"__asyncpg_{uuid4()}__",
            "statement_cache_size": 0
        }
    )

def newsdata_client():
    """
    NewsData.io API client for fetching financial news and market data.
    API Docs: https://newsdata.io/documentation
    """
    api_key = os.getenv("NEWSDATA_API_KEY")
    if not api_key:
        raise ValueError("NEWSDATA_API_KEY not found in environment variables")
    
    return {
        "api_key": api_key,
        "base_url": "https://newsdata.io/api/1",
        "client": httpx.AsyncClient(
            headers={"X-ACCESS-KEY": api_key},
            timeout=30.0
        )
    }