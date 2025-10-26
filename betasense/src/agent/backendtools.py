from pathlib import Path
import sys
from typing import List, Dict, Any

from openai import AsyncOpenAI
from agents import function_tool, WebSearchTool

project_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(project_root))
import betasense
from auth.clients import openai_client, newsdata_client


client: AsyncOpenAI = openai_client()
news_client = newsdata_client()


@function_tool
def search_web():
    """
    Use this tool to do a general web search and return a text output
    """
    return WebSearchTool()


@function_tool
def earnings_transcript(search_query: str):
    """
    Use this tool to retrieve earnings transcripts from database and return a text output
    """
    return client.vector_stores.search(
        vector_store_id="vs_68fe0635411881919e3112029cca1fba",
        query=search_query
    )


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


# @function_tool
async def financial_news(
    query: str,
    country: str = "us",
    category: str = "business",
    language: str = "en"
) -> Dict[str, Any]:
    """
    Use this tool to retrieve real-time financial news from NewsData.io API.
    
    Args:
        query: Search keywords (e.g., company name, ticker, sector)
        country: Country code (default: 'us')
        category: News category - business, top, technology, etc.
        language: Language code (default: 'en')
    
    Returns:
        Dict containing news articles with title, description, link, pubDate, source
    
    Example:
        financial_news(query="Tesla TSLA", category="business")
        financial_news(query="Federal Reserve interest rates", country="us")
    """
    try:
        async with news_client["client"] as client:
            params = {
                "q": query,
                "country": country,
                "category": category,
                "language": language
            }
            response = await client.get(f"{news_client['base_url']}/news", params=params)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": f"Failed to fetch news: {str(e)}"}


@function_tool
def expert_transcripts(search_query: str):
    '''
    Use this tool to retrieve expert transcripts from database and return a text output
    '''
    return client.vector_stores.search(
        vector_store_id="vs_68fe0635411881919e3112029cca1fba",
        query=search_query
    )


@function_tool
def euromonitor(search_query: str):
    """
    Use this tool to retrieve Euromonitor reports from database and return a text output
    """
    return client.vector_stores.search(
        vector_store_id="vs_68fe0780338c819194a6dd8440c41809",
        query=search_query
    )


@function_tool
def financials(search_query: str):
    """
    Use this tool to retrieve financial data from database and return a text output
    """
    return client.vector_stores.search(
    vector_store_id="vs_68fe0234abf08191954d67b63c4daacb",
    query=search_query
    )



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
def insider_transactions(search_query: str):
    """
    Use this tool to retrieve information about insider transactions and return a text output
    """
    return client.vector_stores.search(
        vector_store_id="vs_68fe087329a481919322505a34a5a681",
        query=search_query
    )
    pass


@function_tool
def insider_ownership():
    pass


@function_tool
def performance_based_compensation():
    pass

@function_tool
def alternative_data(search_query: str):

    """
    Use this tool to retrieve alternative data from various sources and return a text output
    """
    return client.vector_stores.search(
        vector_store_id="vs_68fe06aeda788191a2394128ccd5cb52",
        query=search_query
    )


if __name__ == "__main__":
    import asyncio
    from pprint import pprint
    result = asyncio.run(financial_news("Tesla TSLA"))
    pprint(result)