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


# def retrieve_playbook(playbook_name: str) -> str:
#     """
#     Choose the right playbook based on the user's request.
#     """
#     if playbook_name == "long_term_value_investor":
#         return LONG_TERM_VALUE_INVESTOR_PLAYBOOK
#     elif playbook_name == "short_term_swing_trade":
#         return SHORT_TERM_SWING_TRADE_PLAYBOOK
#     elif playbook_name == "merger_arbitrage":
#         return MERGER_ARBITRAGE_PLAYBOOK
#     elif playbook_name == "carve_outs":
#         return CARVE_OUTS_PLAYBOOK
#     elif playbook_name == "growth_investor":
#         return GROWTH_INVESTOR_PLAYBOOK
#     elif playbook_name == "net_net_cigar_butt":


# TODO: Bryan to add more tools here

"""
Information toolbox:
- search web
- earning transcript #
- investor presentation *
- press release #
- expert transcripts #
- euromonitor
- financials
- 10k *
- sell side research *
- comps
- insider transactions
- insider ownership
- performance-based compensation

Perspective toolbox:
- long term value investor
- short term swing trade
- merger arbitrage
- carve outs
- growth investor
- cigar butt
- activist investor

Industry toolbox:
- TMT
- Industrials
- Consumer Discretionary
- Consumer Staples
- Energy
- Financials
- Health Care
- Industrials
- Materials
- Utilities

Utils toolbox:
- Parse pdf
- Parse excel
- Read image
- Think...
"""