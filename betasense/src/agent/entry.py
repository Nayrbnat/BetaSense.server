from pathlib import Path
import sys
import json

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
from agent.generaltools import (
    emit_thinking_process,
    emit_finding_summary,
)


load_dotenv()


agent = Agent(
    name="Financial Analyst Agent",
    instructions=SYSTEM_PROMPT,
    tools=[
        emit_thinking_process,
        emit_finding_summary,

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
            if event.type == "run_item_stream_event" and hasattr(event, 'item'):
                if event.item.type == "tool_call_item":
                    if event.item.raw_item.name == "emit_thinking_process":
                        args = json.loads(event.item.raw_item.arguments)
                        print("[THINKING PROCESS]: ", args["thinking_process"])
                    elif event.item.raw_item.name == "emit_finding_summary":
                        args = json.loads(event.item.raw_item.arguments)
                        print("[FINDING SUMMARY]: ", args["finding_summary"])
                    else:
                        print("[TOOL CALL]: ", event.item.raw_item.name)

        return


# To test only - delete this when front-end is connected
if __name__ == "__main__":
    INPUT = "What about revenue share for different products over the past few years - for different business lines, and give overall analysis"

    import asyncio
    session_id = "test-session"
    user_input = INPUT
    asyncio.run(run_agent(session_id, user_input))