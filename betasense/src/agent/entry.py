from pathlib import Path
import sys
import json
from typing import Callable, Awaitable, Dict, Any

from dotenv import load_dotenv
from agents import Agent, Runner, trace
from agents.extensions.memory.sqlalchemy_session import SQLAlchemySession

project_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(project_root))
import betasense
from prompts.systemprompt import SYSTEM_PROMPT
from auth.clients import sqlalchemy_client
from agent.browsertools import *
from agent.backendtools import (
    search_web,
    earnings_transcript,
    investor_presentation,
    press_release,
    expert_transcripts,
    euromonitor,
    financials,
    file_10k,
    sell_side_research,
    comps,
    insider_transactions,
    insider_ownership,
    performance_based_compensation,
)
from agent.playbooktools import (
    retrieve_perspective_playbook, 
    retrieve_industry_playbook
)


load_dotenv()


agent = Agent(
    name="Browser agent",
    instructions=SYSTEM_PROMPT,
    tools=[
        retrieve_perspective_playbook,
        retrieve_industry_playbook,
        
        search_web,
        earnings_transcript,
        investor_presentation,
        press_release,
        expert_transcripts,
        euromonitor,
        financials,
        file_10k,
        sell_side_research,
        comps,
        insider_transactions,
        insider_ownership,
        performance_based_compensation,
    ]
)


async def run_agent(
        session_id: str, 
        user_input: str
    ):
    engine = await sqlalchemy_client()
    session = SQLAlchemySession(
            engine=engine,
            session_id=session_id,
        )
    with trace(workflow_name=f"betasense-agent-{session_id}"):
        result = Runner.run_streamed(
            starting_agent=agent,
            input=user_input,
            session=session
        )

        async for event in result.stream_events():
            print(event) #TODO: Stream with front-end

        return result.final_output
    

if __name__ == "__main__":
    import asyncio
    session_id = "test-session"
    user_input = "Tell me about Apple's latest 10-K filing - top line revenue?"
    asyncio.run(run_agent(session_id, user_input))