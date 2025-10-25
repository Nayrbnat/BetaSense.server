from pathlib import Path
import sys

from dotenv import load_dotenv
from agents import Agent, Runner, trace

project_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(project_root))
import betasense
from prompts.systemprompt import SYSTEM_PROMPT
from agent.browsertools import tool_1 as browser_tool_1
from agent.backendtools import tool_1 as backend_tool_1
from agent.playbooktools import tool_1 as playbook_tool_1


load_dotenv()


agent = Agent(
    name="Browser agent",
    instructions=SYSTEM_PROMPT,
    tools=[
        browser_tool_1,
        backend_tool_1,
        playbook_tool_1,
    ]
)


async def run_agent(session_id: str, user_input: str):
    
    with trace(workflow_name=f"betasense-agent-{session_id}"):
        result = Runner.run_streamed(
            starting_agent=agent,
            input=user_input,
        )