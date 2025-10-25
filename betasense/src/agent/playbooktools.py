from pathlib import Path
import sys
from typing import List, Dict, Any

from agents import function_tool

project_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(project_root))
import betasense
from prompts.industryplaybooks import *
from prompts.perspectiveplaybooks import (
    LONG_TERM_VALUE_INVESTOR_PLAYBOOK,
    SHORT_TERM_SWING_TRADE_PLAYBOOK,
    MERGER_ARBITRAGE_PLAYBOOK,
    CARVE_OUTS_PLAYBOOK,
    GROWTH_INVESTOR_PLAYBOOK,
    CIGAR_BUTT_PLAYBOOK,
)


@function_tool
def retrieve_playbook(playbook_name: str) -> str:
    """
    Choose the right playbook based on the playbook name.

    Available playbook_name args:
    - long_term_value_investor
    - short_term_swing_trade
    - merger_arbitrage
    - carve_outs
    - growth_investor
    - net_net_cigar_butt

    Returns:
        The playbook content.
    """
    if playbook_name == "long_term_value_investor":
        return LONG_TERM_VALUE_INVESTOR_PLAYBOOK
    elif playbook_name == "short_term_swing_trade":
        return SHORT_TERM_SWING_TRADE_PLAYBOOK
    elif playbook_name == "merger_arbitrage":
        return MERGER_ARBITRAGE_PLAYBOOK
    elif playbook_name == "carve_outs":
        return CARVE_OUTS_PLAYBOOK
    elif playbook_name == "growth_investor":
        return GROWTH_INVESTOR_PLAYBOOK
    elif playbook_name == "net_net_cigar_butt":
        return CIGAR_BUTT_PLAYBOOK