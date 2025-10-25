from pathlib import Path
import sys
from typing import List, Dict, Any

from openai import AsyncOpenAI
from agents import function_tool, WebSearchTool

project_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(project_root))
import betasense
from auth.clients import openai_client


client: AsyncOpenAI = openai_client()


@function_tool
def search_web():
    """
    Use this tool to do a general web search and return a text output
    """
    return WebSearchTool()


@function_tool
def earnings_transcript():
    '''
    Use this tool to retrieve earnings transcripts from database and return a text output
    '''
    pass


@function_tool
def investor_presentation():
    '''
    Use this tool to retrieve investor presentations from database and return a text output
    '''
    pass


@function_tool
def press_release():
    '''
    Use this tool to retrieve press releases from database and return a text output
    '''
    pass


@function_tool
def expert_transcripts():
    '''
    Use this tool to retrieve expert transcripts from database and return a text output
    '''
    pass


@function_tool
def euromonitor():
    pass


@function_tool
def financials():
    pass


@function_tool
def file_10k(search_query: str):
    """
    Use this tool to retrieve information from 10-K filings and return a text output
    """
    return client.vector_stores.search(
        vector_store_id="vs_68fd0397638c819188316da0396a4753",
        query=search_query
    )


@function_tool
def sell_side_research():
    pass


@function_tool
def comps():
    pass


@function_tool
def insider_transactions():
    pass


@function_tool
def insider_ownership():
    pass


@function_tool
def performance_based_compensation():
    pass