from pathlib import Path
import sys
from typing import List, Dict, Any

from agents import function_tool

project_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(project_root))
import betasense


@function_tool
def tool_1(args) -> str:
    # TODO: Bryan to write docstring below:
    # NOTE: Don't overkill this - here should be brief and straight to the point -
    # heavy lifting of prompt engineering should be done in the system prompt
    """
    Use this tool to do xxx:

    Args:
        arg 1: Arg 1 description
        arg 2: Arg 2 description
        ...

    Returns:
        e.g. a List of xxx
    """
    # TODO: Rui Kai to write the script below:
    pass


# TODO: Bryan to add more tools here