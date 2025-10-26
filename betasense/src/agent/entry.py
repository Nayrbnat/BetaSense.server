from pathlib import Path
import sys
import json

from dotenv import load_dotenv
from agents import Agent, Runner, trace
from agents.extensions.memory.sqlalchemy_session import SQLAlchemySession

project_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(project_root))
import betasense
from betasense.src.prompts.systemprompt import SYSTEM_PROMPT
from betasense.src.auth.clients import sqlalchemy_client
from betasense.src.agent.browsertools import control_browser
from betasense.src.agent.backendtools import (
    search_web,
    earnings_transcript,
    investor_presentation,
    press_release,
    financial_news,
    expert_transcripts,
    euromonitor,
    financials,
    file_10k,
    sell_side_research,
    comparable_multiples,
    insider_transactions,
    alternative_data,
    current_ownership,
    performance_analysis,
    segments,
    short_interests,
    street_consensus,
    supply_chain_analysis,
)
from betasense.src.agent.playbooktools import (
    retrieve_perspective_playbook, 
    retrieve_industry_playbook
)
from betasense.src.agent.generaltools import (
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

        control_browser,

        retrieve_perspective_playbook,
        retrieve_industry_playbook,
        
        search_web,
        financial_news,
        earnings_transcript,
        investor_presentation,
        press_release,
        expert_transcripts,
        euromonitor,
        financials,
        file_10k,
        sell_side_research,
        comparable_multiples,
        insider_transactions,
        alternative_data,
        current_ownership,
        performance_analysis,
        segments,
        short_interests,
        street_consensus,
        supply_chain_analysis,
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
            session=session,
            max_turns=25,
        )

        print("Streaming agent events...")

        async for event in result.stream_events():
            if event.type == "run_item_stream_event" and hasattr(event, 'item'):
                if event.item.type == "tool_call_item":
                    if event.item.raw_item.name == "emit_thinking_process":
                        args = json.loads(event.item.raw_item.arguments)
                        output = {
                            "type": "thinking",
                            "content": args["thinking_process"],
                            "tool": "emit_thinking_process"
                        }
                        print(output)
                        yield output
                    elif event.item.raw_item.name == "emit_finding_summary":
                        args = json.loads(event.item.raw_item.arguments)
                        output = {
                            "type": "finding",
                            "content": args["finding_summary"],
                            "tool": "emit_finding_summary"
                        }
                        print(output)
                        yield output
                        return
                    elif event.item.raw_item.name == "control_browser":
                        args = json.loads(event.item.raw_item.arguments)
                        output = {
                            "type": "browser_action",
                            "content": {
                                "panel": args["panel"],
                                "action": args["action"]
                            },
                            "tool": "control_browser"
                        }
                        print(output)
                        yield output
                    else:
                        output = {
                            "type": "tool_call",
                            "content": event.item.raw_item.name,
                            "tool": event.item.raw_item.name
                        }
                        print(output)
                        yield output