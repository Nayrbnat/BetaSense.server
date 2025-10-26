from pathlib import Path
import sys
from typing import List, Dict, Any

from agents import function_tool

project_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(project_root))
import betasense
from betasense.src.prompts.industryplaybooks import (
    TMT_PLAYBOOK,
    INDUSTRIALS_PLAYBOOK,
    CONSUMER_DISCRETIONARY_PLAYBOOK,
    CONSUMER_STAPLES_PLAYBOOK,
    ENERGY_PLAYBOOK,
    FINANCIALS_PLAYBOOK,
    HEALTH_CARE_PLAYBOOK,
    MATERIALS_PLAYBOOK,
    UTILITIES_PLAYBOOK,
)
from betasense.src.prompts.perspectiveplaybooks import (
    LONG_TERM_VALUE_INVESTOR_PLAYBOOK,
    SHORT_TERM_SWING_TRADE_PLAYBOOK,
    MERGER_ARBITRAGE_PLAYBOOK,
    CARVE_OUTS_PLAYBOOK,
    GROWTH_INVESTOR_PLAYBOOK,
    CIGAR_BUTT_PLAYBOOK,
    ACTIVIST_INVESTOR_PLAYBOOK,
)


@function_tool
def retrieve_perspective_playbook(playbook_name: str) -> str:
    """
    Choose the right perspectives playbook based on the playbook name.

    Available playbook_name args:
    - long_term_value_investor
    - short_term_swing_trade
    - merger_arbitrage
    - carve_outs
    - growth_investor
    - net_net_cigar_butt
    - activist_investor

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
    elif playbook_name == "activist_investor":
        return ACTIVIST_INVESTOR_PLAYBOOK
    else:
        return f"Playbook '{playbook_name}' not found. Available playbooks: long_term_value_investor, short_term_swing_trade, merger_arbitrage, carve_outs, growth_investor, net_net_cigar_butt, activist_investor"
    

@function_tool
def retrieve_industry_playbook(industry_name: str) -> str:
    """
    Choose the right industry playbook based on the industry name.

    Available industry_name args:
    - tmt (Technology, Media & Telecommunications)
    - industrials
    - consumer_discretionary
    - consumer_staples
    - energy
    - financials
    - health_care
    - materials
    - utilities

    Returns:
        The playbook content.
    """
    if industry_name == "tmt":
        return TMT_PLAYBOOK
    elif industry_name == "industrials":
        return INDUSTRIALS_PLAYBOOK
    elif industry_name == "consumer_discretionary":
        return CONSUMER_DISCRETIONARY_PLAYBOOK
    elif industry_name == "consumer_staples":
        return CONSUMER_STAPLES_PLAYBOOK
    elif industry_name == "energy":
        return ENERGY_PLAYBOOK
    elif industry_name == "financials":
        return FINANCIALS_PLAYBOOK
    elif industry_name == "health_care":
        return HEALTH_CARE_PLAYBOOK
    elif industry_name == "materials":
        return MATERIALS_PLAYBOOK
    elif industry_name == "utilities":
        return UTILITIES_PLAYBOOK
    else:
        return f"Industry playbook '{industry_name}' not found. Available industries: tmt, industrials, consumer_discretionary, consumer_staples, energy, financials, health_care, materials, utilities"