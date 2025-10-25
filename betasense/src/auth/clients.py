import os
from uuid import uuid4

from dotenv import load_dotenv
from openai import AsyncOpenAI
from sqlalchemy.ext.asyncio import create_async_engine


load_dotenv(".env")


async def openai_client():
    return AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def sqlalchemy_client():
    return create_async_engine(
        os.getenv("SUPABASE_DATABASE_URL"),
        connect_args={
            "prepared_statement_name_func": lambda: f"__asyncpg_{uuid4()}__",
            "statement_cache_size": 0
        }
    )