from pathlib import Path
import sys
from typing import List, Dict, Any

from agents import function_tool

project_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(project_root))
import betasense
from prompts.playbooks import (
    PLAYBOOK_1
)


@function_tool
def tool_1(args) -> str:
    """
    Call this tool once to retrieve the playbook for xxx e.g. how to read a stock market report
    """
    return 