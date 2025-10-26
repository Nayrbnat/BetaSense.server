from pathlib import Path
import sys
from typing import List, Dict, Any, Literal, Optional
from enum import Enum

from agents import function_tool

project_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(project_root))
import betasense


# Dashboard Types
class DashboardType(str, Enum):
    PRICE_CHART = "price_chart"
    NEWS_FEED = "news_feed"
    SHORT_INTEREST = "short_interest"
    FINANCIALS = "financials"
    VALUATION = "valuation"
    SENTIMENT = "sentiment"


# Layout Modes
class LayoutMode(str, Enum):
    MAXIMIZED = "maximized"          # Single dashboard fills entire screen
    GRID_2X2 = "grid_2x2"            # 4 dashboards in 2x2 grid
    GRID_1X2 = "grid_1x2"            # 2 dashboards side by side
    GRID_2X1 = "grid_2x1"            # 2 dashboards stacked vertically
    GRID_3X2 = "grid_3x2"            # 6 dashboards in 3x2 grid
    PICTURE_IN_PICTURE = "pip"       # One large + one small overlay


@function_tool
def control_dashboard_layout(
    layout_mode: str,
    primary_dashboard: str,
    secondary_dashboards: Optional[List[str]] = None,
    ticker: Optional[str] = None
) -> Dict[str, Any]:
    """
    Control the frontend dashboard layout and configure which dashboards to display.
    
    This is the PRIMARY tool for managing screen real estate and dashboard visibility.
    
    Args:
        layout_mode: How to arrange dashboards on screen
            - "maximized": Single dashboard fills entire screen
            - "grid_2x2": 4 dashboards in 2x2 grid  
            - "grid_1x2": 2 dashboards side by side
            - "grid_2x1": 2 dashboards stacked vertically
            - "grid_3x2": All 6 dashboards visible
            - "pip": Picture-in-picture (one large, one small overlay)
            
        primary_dashboard: The main/first dashboard to display
            - "price_chart": Stock price and technical analysis
            - "news_feed": Latest news and press releases
            - "short_interest": Short interest and borrow data
            - "financials": Financial statements and metrics
            - "valuation": Valuation multiples and comparisons
            - "sentiment": Social sentiment and analyst ratings
            
        secondary_dashboards: Additional dashboards to show (for multi-dashboard layouts)
            List of dashboard names from above options
            
        ticker: Stock ticker symbol to focus on (e.g., "AAPL", "TSLA")
    
    Returns:
        JSON command for frontend to execute layout change
        
    Example Usage:
        # Maximize price chart for AAPL
        control_dashboard_layout(
            layout_mode="maximized",
            primary_dashboard="price_chart", 
            ticker="AAPL"
        )
        
        # Show price chart + news side by side
        control_dashboard_layout(
            layout_mode="grid_1x2",
            primary_dashboard="price_chart",
            secondary_dashboards=["news_feed"],
            ticker="TSLA"
        )
        
        # Show all 6 dashboards
        control_dashboard_layout(
            layout_mode="grid_3x2",
            primary_dashboard="price_chart",
            secondary_dashboards=["news_feed", "short_interest", "financials", "valuation", "sentiment"],
            ticker="NVDA"
        )
    """
    
    command = {
        "action": "set_layout",
        "layout": {
            "mode": layout_mode,
            "primary_dashboard": primary_dashboard,
            "secondary_dashboards": secondary_dashboards or [],
            "ticker": ticker
        },
        "timestamp": "{{ timestamp }}"
    }
    
    return command


@function_tool
def update_dashboard_data(
    dashboard: str,
    data_sources: List[str],
    ticker: str,
    timeframe: Optional[str] = "1D",
    filters: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Update specific dashboard with new data from selected sources.
    
    Use this to refresh dashboard content or change what data is displayed.
    
    Args:
        dashboard: Which dashboard to update
            - "price_chart", "news_feed", "short_interest", "financials", "valuation", "sentiment"
            
        data_sources: Which data sources to pull from
            For price_chart: ["price_data", "volume", "technical_indicators", "options_flow"]
            For news_feed: ["company_news", "sector_news", "earnings_releases", "analyst_reports"]
            For short_interest: ["short_volume", "borrow_rate", "days_to_cover", "institutional_positions"]
            For financials: ["income_statement", "balance_sheet", "cash_flow", "key_metrics"]
            For valuation: ["multiples", "dcf", "comps", "sum_of_parts"]
            For sentiment: ["social_sentiment", "analyst_ratings", "insider_trading", "institutional_flow"]
            
        ticker: Stock ticker symbol
        
        timeframe: Time period for data
            - "1D", "5D", "1M", "3M", "6M", "YTD", "1Y", "5Y", "MAX"
            
        filters: Additional filters/parameters specific to dashboard type
    
    Returns:
        JSON command to update dashboard data
        
    Example:
        # Load AAPL price chart with technical indicators
        update_dashboard_data(
            dashboard="price_chart",
            data_sources=["price_data", "volume", "technical_indicators"],
            ticker="AAPL",
            timeframe="1M"
        )
        
        # Load latest news for Tesla
        update_dashboard_data(
            dashboard="news_feed",
            data_sources=["company_news", "earnings_releases"],
            ticker="TSLA",
            timeframe="1M"
        )
    """
    
    command = {
        "action": "update_data",
        "dashboard": dashboard,
        "config": {
            "data_sources": data_sources,
            "ticker": ticker,
            "timeframe": timeframe,
            "filters": filters or {}
        },
        "timestamp": "{{ timestamp }}"
    }
    
    return command


@function_tool
def highlight_dashboard_element(
    dashboard: str,
    element_type: str,
    element_id: str,
    annotation: Optional[str] = None
) -> Dict[str, Any]:
    """
    Highlight or annotate specific elements within a dashboard to draw user attention.
    
    Use this to point out important findings, anomalies, or key data points.
    
    Args:
        dashboard: Which dashboard contains the element
        element_type: Type of element to highlight
            - "chart_point": Specific point on a chart
            - "metric": A key metric or KPI
            - "news_item": Specific news article
            - "data_row": Row in a table/grid
            - "indicator": Technical indicator signal
            
        element_id: Identifier for the specific element
        annotation: Optional text to display near the highlight
    
    Returns:
        JSON command to highlight element
        
    Example:
        # Highlight unusual volume spike on chart
        highlight_dashboard_element(
            dashboard="price_chart",
            element_type="chart_point",
            element_id="2024-10-15_spike",
            annotation="Unusual volume - 3x average"
        )
    """
    
    command = {
        "action": "highlight_element",
        "dashboard": dashboard,
        "highlight": {
            "element_type": element_type,
            "element_id": element_id,
            "annotation": annotation,
            "style": "pulse"  # Could be: pulse, glow, border, etc.
        },
        "timestamp": "{{ timestamp }}"
    }
    
    return command


@function_tool
def create_dashboard_alert(
    alert_type: str,
    message: str,
    severity: str = "info",
    dashboard: Optional[str] = None,
    action_required: bool = False
) -> Dict[str, Any]:
    """
    Display an alert or notification on the frontend.
    
    Use this to communicate important findings, warnings, or insights to the user.
    
    Args:
        alert_type: Type of alert
            - "insight": Key finding or analysis insight
            - "warning": Risk factor or concern
            - "opportunity": Potential trade or investment opportunity
            - "data_update": New data available
            - "error": Something went wrong
            
        message: Alert message text to display
        
        severity: Alert severity level
            - "info": Informational (blue)
            - "success": Positive finding (green)
            - "warning": Caution needed (yellow)
            - "danger": Risk or critical issue (red)
            
        dashboard: Specific dashboard to show alert on (or None for global)
        action_required: Whether user action is needed
    
    Returns:
        JSON command to display alert
        
    Example:
        # Alert about high short interest
        create_dashboard_alert(
            alert_type="warning",
            message="Short interest increased 45% in last 2 weeks - potential squeeze risk",
            severity="warning",
            dashboard="short_interest"
        )
    """
    
    command = {
        "action": "show_alert",
        "alert": {
            "type": alert_type,
            "message": message,
            "severity": severity,
            "dashboard": dashboard,
            "action_required": action_required,
            "dismissible": True
        },
        "timestamp": "{{ timestamp }}"
    }
    
    return command


@function_tool
def execute_dashboard_comparison(
    ticker_primary: str,
    tickers_compare: List[str],
    comparison_type: str,
    metrics: List[str],
    timeframe: str = "1Y"
) -> Dict[str, Any]:
    """
    Set up a comparison view between multiple tickers across dashboards.
    
    Use this to perform competitive analysis or sector comparisons.
    
    Args:
        ticker_primary: Primary ticker to analyze
        tickers_compare: List of tickers to compare against (up to 5)
        comparison_type: Type of comparison
            - "price_performance": Price chart overlay
            - "fundamentals": Financial metrics comparison
            - "valuation": Valuation multiples comparison
            - "sentiment": Sentiment scores comparison
            
        metrics: Specific metrics to compare (varies by comparison_type)
        timeframe: Time period for comparison
    
    Returns:
        JSON command to set up comparison view
        
    Example:
        # Compare AAPL vs competitors on valuation
        execute_dashboard_comparison(
            ticker_primary="AAPL",
            tickers_compare=["MSFT", "GOOGL", "META"],
            comparison_type="valuation",
            metrics=["P/E", "P/S", "EV/EBITDA", "PEG"],
            timeframe="1Y"
        )
    """
    
    command = {
        "action": "setup_comparison",
        "comparison": {
            "primary": ticker_primary,
            "compare_to": tickers_compare,
            "type": comparison_type,
            "metrics": metrics,
            "timeframe": timeframe
        },
        "timestamp": "{{ timestamp }}"
    }
    
    return command


@function_tool
def reset_dashboards() -> Dict[str, Any]:
    """
    Reset all dashboards to default state and clear any active analyses.
    
    Use this to start fresh or clear the screen between different analyses.
    
    Returns:
        JSON command to reset dashboards
    """
    
    command = {
        "action": "reset_all",
        "timestamp": "{{ timestamp }}"
    }
    
    return command


# Example workflow function (not a tool, just for documentation)
def example_aapl_analysis_workflow():
    """
    Example workflow for: "Is AAPL a good investment now?"
    
    Step 1: Maximize price chart
    control_dashboard_layout(
        layout_mode="maximized",
        primary_dashboard="price_chart",
        ticker="AAPL"
    )
    
    Step 2: Load price data with technical indicators
    update_dashboard_data(
        dashboard="price_chart",
        data_sources=["price_data", "volume", "technical_indicators", "options_flow"],
        ticker="AAPL",
        timeframe="6M"
    )
    
    Step 3: Switch to multi-dashboard view with news and short interest
    control_dashboard_layout(
        layout_mode="grid_1x2",
        primary_dashboard="news_feed",
        secondary_dashboards=["short_interest"],
        ticker="AAPL"
    )
    
    Step 4: Load news data
    update_dashboard_data(
        dashboard="news_feed",
        data_sources=["company_news", "earnings_releases", "analyst_reports"],
        ticker="AAPL",
        timeframe="1M"
    )
    
    Step 5: Load short interest data
    update_dashboard_data(
        dashboard="short_interest",
        data_sources=["short_volume", "borrow_rate", "days_to_cover"],
        ticker="AAPL",
        timeframe="3M"
    )
    
    Step 6: Create alert if any concerning findings
    create_dashboard_alert(
        alert_type="insight",
        message="AAPL showing strong technical support at $165. Recent news positive on Services growth.",
        severity="success"
    )
    """
    pass
