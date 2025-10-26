from pathlib import Path
import sys
from typing import List, Dict, Any, Literal, Optional
from enum import Enum

from agents import function_tool

project_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(project_root))
import betasense


@function_tool
async def control_browser(panel: str, action: str):
    """
    panel: one of "price-chart", "portfolio-monitor", "market-news", "indices", "comparables", "document-library"
    action: one of "maximize", "minimize"
    """
    return {
        "panel": panel,
        "action": action
    }


# # Dashboard Types
# class DashboardType(str, Enum):
#     PRICE_CHART = "price_chart"
#     PORTFOLIO_MONITOR = "portfolio_monitor"
#     MARKET_NEWS = "market_news"
#     INDICES = "indices"
#     COMPARABLES = "comparables"
#     DOCUMENT_LIBRARY = "document_library"


# # Layout Modes
# class LayoutMode(str, Enum):
#     CUSTOM = "custom"                # Custom positioning and sizing
#     MAXIMIZED = "maximized"          # Single paneltype fills entire screen
#     GRID_2X2 = "grid_2x2"            # 4 paneltype in 2x2 grid
#     GRID_1X2 = "grid_1x2"            # 2 paneltype side by side
#     GRID_2X1 = "grid_2x1"            # 2 paneltype stacked vertically
#     GRID_3X2 = "grid_3x2"            # 6 paneltype in 3x2 grid
#     PICTURE_IN_PICTURE = "pip"       # One large + one small overlay


# @function_tool
# def control_dashboard_layout(
#     layout_mode: str,
#     paneltype: List[Dict[str, Any]],
#     ticker: Optional[str] = None,
#     minimize: Optional[List[str]] = None,
#     maximize: Optional[str] = None,
#     zoom: Optional[float] = None
# ) -> Dict[str, Any]:
#     """
#     Control the frontend dashboard layout with precise control over positioning, sizing, and visibility.
    
#     This is the PRIMARY tool for managing screen real estate and dashboard configuration.
    
#     Args:
#         layout_mode: How to arrange paneltype on screen
#             - "custom": Custom positioning with explicit x, y, width, height for each paneltype
#             - "maximized": Single paneltype fills entire screen
#             - "grid_2x2": 4 paneltype in 2x2 grid  
#             - "grid_1x2": 2 paneltype side by side
#             - "grid_2x1": 2 paneltype stacked vertically
#             - "grid_3x2": All 6 paneltype visible
#             - "pip": Picture-in-picture (one large, one small overlay)
            
#         paneltype: List of dashboard configurations. Each dashboard dict contains:
#             - "type" (required): Dashboard type
#                 - "price_chart": Stock price and volume analysis
#                 - "portfolio_monitor": Portfolio performance and holdings tracking
#                 - "market_news": Latest market news and press releases
#                 - "indices": Major indices and sector performance
#                 - "comparables": Peer comparison and relative metrics
#                 - "document_library": Research documents and filings
            
#             - "position" (optional for custom mode): {"x": int, "y": int}
#                 - x: Horizontal position in pixels from left edge
#                 - y: Vertical position in pixels from top edge
                
#             - "size" (optional for custom mode): {"width": int|str, "height": int|str}
#                 - width: Dashboard width (pixels as int, or percentage as "50%")
#                 - height: Dashboard height (pixels as int, or percentage as "50%")
                
#             - "z_index" (optional): Stacking order (higher = on top)
            
#             - "data_sources" (optional): List of data sources to load immediately
#             - "timeframe" (optional): Time period for data (e.g., "1D", "1M", "1Y")
#             - "filters" (optional): Additional filters/parameters
            
#         ticker: Stock ticker symbol to focus on (e.g., "AAPL", "TSLA")
        
#         minimize: List of dashboard types to minimize to taskbar/dock
#             - Example: ["indices", "document_library"]
#             - Minimized dashboards remain accessible but hidden from view
            
#         maximize: Single dashboard type to maximize (overrides layout_mode if provided)
#             - Example: "price_chart"
#             - When set, this dashboard fills the entire screen
            
#         zoom: Zoom level for all dashboards (0.5 to 2.0)
#             - 1.0 = 100% (default)
#             - 0.75 = 75% zoom out (see more content)
#             - 1.5 = 150% zoom in (larger text/charts)
    
#     Returns:
#         JSON command for frontend to execute layout change
        
#     Example Usage:
#         # Maximize price chart for AAPL
#         control_dashboard_layout(
#             layout_mode="maximized",
#             paneltype=[
#                 {
#                     "type": "price_chart",
#                     "data_sources": ["price_data", "volume"],
#                     "timeframe": "6M"
#                 }
#             ],
#             ticker="AAPL"
#         )
        
#         # Show price chart + news side by side (grid layout)
#         control_dashboard_layout(
#             layout_mode="grid_1x2",
#             paneltype=[
#                 {
#                     "type": "price_chart",
#                     "data_sources": ["price_data", "volume"]
#                 },
#                 {
#                     "type": "market_news",
#                     "data_sources": ["company_news", "earnings_releases"]
#                 }
#             ],
#             ticker="TSLA"
#         )
        
#         # Custom layout with precise positioning and sizing
#         control_dashboard_layout(
#             layout_mode="custom",
#             paneltype=[
#                 {
#                     "type": "price_chart",
#                     "position": {"x": 0, "y": 0},
#                     "size": {"width": "70%", "height": "60%"},
#                     "z_index": 1,
#                     "data_sources": ["price_data", "volume"],
#                     "timeframe": "1M"
#                 },
#                 {
#                     "type": "market_news",
#                     "position": {"x": "70%", "y": 0},
#                     "size": {"width": "30%", "height": "60%"},
#                     "z_index": 1,
#                     "data_sources": ["company_news"]
#                 },
#                 {
#                     "type": "indices",
#                     "position": {"x": 0, "y": "60%"},
#                     "size": {"width": "50%", "height": "40%"},
#                     "z_index": 1
#                 },
#                 {
#                     "type": "comparables",
#                     "position": {"x": "50%", "y": "60%"},
#                     "size": {"width": "50%", "height": "40%"},
#                     "z_index": 1
#                 }
#             ],
#             ticker="NVDA"
#         )
        
#         # Picture-in-picture with main chart and small news overlay
#         control_dashboard_layout(
#             layout_mode="pip",
#             paneltype=[
#                 {
#                     "type": "price_chart",
#                     "data_sources": ["price_data", "volume"]
#                 },
#                 {
#                     "type": "market_news",
#                     "position": {"x": "75%", "y": "75%"},
#                     "size": {"width": "20%", "height": "20%"},
#                     "z_index": 10
#                 }
#             ],
#             ticker="AAPL"
#         )
        
#         # Maximize a specific dashboard (overrides layout_mode)
#         control_dashboard_layout(
#             layout_mode="custom",
#             paneltype=[
#                 {"type": "price_chart"},
#                 {"type": "market_news"},
#                 {"type": "comparables"}
#             ],
#             ticker="TSLA",
#             maximize="price_chart"  # This dashboard fills the screen
#         )
        
#         # Minimize less important dashboards to declutter
#         control_dashboard_layout(
#             layout_mode="grid_2x2",
#             paneltype=[
#                 {"type": "price_chart"},
#                 {"type": "market_news"},
#                 {"type": "comparables"},
#                 {"type": "indices"}
#             ],
#             ticker="NVDA",
#             minimize=["indices", "document_library"]  # Hide these for now
#         )
        
#         # Zoom out to see more data at once
#         control_dashboard_layout(
#             layout_mode="grid_1x2",
#             paneltype=[
#                 {"type": "price_chart"},
#                 {"type": "comparables"}
#             ],
#             ticker="AAPL",
#             zoom=0.75  # 75% zoom - fit more information on screen
#         )
        
#         # Zoom in for presentation/readability
#         control_dashboard_layout(
#             layout_mode="maximized",
#             paneltype=[{"type": "price_chart"}],
#             ticker="MSFT",
#             zoom=1.25  # 125% zoom - larger charts and text
#         )
#     """
    
#     command = {
#         "action": "set_layout",
#         "layout": {
#             "mode": layout_mode,
#             "paneltype": paneltype,
#             "ticker": ticker,
#             "minimize": minimize,
#             "maximize": maximize,
#             "zoom": zoom
#         },
#         "timestamp": "{{ timestamp }}"
#     }
    
#     return command


# @function_tool
# def update_dashboard_data(
#     dashboard: str,
#     data_sources: List[str],
#     ticker: str,
#     timeframe: Optional[str] = "1D",
#     filters: Optional[Dict[str, Any]] = None
# ) -> Dict[str, Any]:
#     """
#     Update specific dashboard with new data from selected sources.
    
#     Use this to refresh dashboard content or change what data is displayed.
    
#     Args:
#         dashboard: Which dashboard to update
#             - "price_chart", "news_feed", "short_interest", "financials", "valuation", "sentiment"
            
#         data_sources: Which data sources to pull from
#             For price_chart: ["price_data", "volume", "technical_indicators", "options_flow"]
#             For news_feed: ["company_news", "sector_news", "earnings_releases", "analyst_reports"]
#             For short_interest: ["short_volume", "borrow_rate", "days_to_cover", "institutional_positions"]
#             For financials: ["income_statement", "balance_sheet", "cash_flow", "key_metrics"]
#             For valuation: ["multiples", "dcf", "comps", "sum_of_parts"]
#             For sentiment: ["social_sentiment", "analyst_ratings", "insider_trading", "institutional_flow"]
            
#         ticker: Stock ticker symbol
        
#         timeframe: Time period for data
#             - "1D", "5D", "1M", "3M", "6M", "YTD", "1Y", "5Y", "MAX"
            
#         filters: Additional filters/parameters specific to dashboard type
    
#     Returns:
#         JSON command to update dashboard data
        
#     Example:
#         # Load AAPL price chart with technical indicators
#         update_dashboard_data(
#             dashboard="price_chart",
#             data_sources=["price_data", "volume", "technical_indicators"],
#             ticker="AAPL",
#             timeframe="1M"
#         )
        
#         # Load latest news for Tesla
#         update_dashboard_data(
#             dashboard="news_feed",
#             data_sources=["company_news", "earnings_releases"],
#             ticker="TSLA",
#             timeframe="1M"
#         )
#     """
    
#     command = {
#         "action": "update_data",
#         "dashboard": dashboard,
#         "config": {
#             "data_sources": data_sources,
#             "ticker": ticker,
#             "timeframe": timeframe,
#             "filters": filters or {}
#         },
#         "timestamp": "{{ timestamp }}"
#     }
    
#     return command


# @function_tool
# def highlight_dashboard_element(
#     dashboard: str,
#     element_type: str,
#     element_id: str,
#     annotation: Optional[str] = None
# ) -> Dict[str, Any]:
#     """
#     Highlight or annotate specific elements within a dashboard to draw user attention.
    
#     Use this to point out important findings, anomalies, or key data points.
    
#     Args:
#         dashboard: Which dashboard contains the element
#         element_type: Type of element to highlight
#             - "chart_point": Specific point on a chart
#             - "metric": A key metric or KPI
#             - "news_item": Specific news article
#             - "data_row": Row in a table/grid
#             - "price_level": Significant price level or event
            
#         element_id: Identifier for the specific element
#         annotation: Optional text to display near the highlight
    
#     Returns:
#         JSON command to highlight element
        
#     Example:
#         # Highlight unusual volume spike on chart
#         highlight_dashboard_element(
#             dashboard="price_chart",
#             element_type="chart_point",
#             element_id="2024-10-15_spike",
#             annotation="Unusual volume - check market_news for catalyst"
#         )
#     """
    
#     command = {
#         "action": "highlight_element",
#         "dashboard": dashboard,
#         "highlight": {
#             "element_type": element_type,
#             "element_id": element_id,
#             "annotation": annotation,
#             "style": "pulse"  # Could be: pulse, glow, border, etc.
#         },
#         "timestamp": "{{ timestamp }}"
#     }
    
#     return command


# @function_tool
# def create_dashboard_alert(
#     alert_type: str,
#     message: str,
#     severity: str = "info",
#     dashboard: Optional[str] = None,
#     action_required: bool = False
# ) -> Dict[str, Any]:
#     """
#     Display an alert or notification on the frontend.
    
#     Use this to communicate important findings, warnings, or insights to the user.
    
#     Args:
#         alert_type: Type of alert
#             - "insight": Key finding or analysis insight
#             - "warning": Risk factor or concern
#             - "opportunity": Potential trade or investment opportunity
#             - "data_update": New data available
#             - "error": Something went wrong
            
#         message: Alert message text to display
        
#         severity: Alert severity level
#             - "info": Informational (blue)
#             - "success": Positive finding (green)
#             - "warning": Caution needed (yellow)
#             - "danger": Risk or critical issue (red)
            
#         dashboard: Specific dashboard to show alert on (or None for global)
#         action_required: Whether user action is needed
    
#     Returns:
#         JSON command to display alert
        
#     Example:
#         # Alert about significant market move
#         create_dashboard_alert(
#             alert_type="warning",
#             message="Major index volatility detected - S&P 500 down 3% intraday",
#             severity="warning",
#             dashboard="indices"
#         )
#     """
    
#     command = {
#         "action": "show_alert",
#         "alert": {
#             "type": alert_type,
#             "message": message,
#             "severity": severity,
#             "dashboard": dashboard,
#             "action_required": action_required,
#             "dismissible": True
#         },
#         "timestamp": "{{ timestamp }}"
#     }
    
#     return command

# @function_tool
# def reset_dashboards() -> Dict[str, Any]:
#     """
#     Reset all paneltype to default state and clear any active analyses.
    
#     Use this to start fresh or clear the screen between different analyses.
    
#     Returns:
#         JSON command to reset paneltype
#     """
    
#     command = {
#         "action": "reset_all",
#         "timestamp": "{{ timestamp }}"
#     }
    
#     return command


# # # Example workflow function (not a tool, just for documentation)
# # """'''
# #     Example workflow for: "Is AAPL a good investment now?"
    
# #     Step 1: Set up comprehensive view with price chart, news, and indices
# #     control_dashboard_layout(
# #         layout_mode="custom",
# #         paneltype=[
# #             {
# #                 "type": "price_chart",
# #                 "position": {"x": 0, "y": 0},
# #                 "size": {"width": "70%", "height": "60%"},
# #                 "data_sources": ["price_data", "volume"],
# #                 "timeframe": "6M"
# #             },
# #             {
# #                 "type": "market_news",
# #                 "position": {"x": "70%", "y": 0},
# #                 "size": {"width": "30%", "height": "60%"},
# #                 "data_sources": ["company_news", "earnings_releases", "analyst_reports"],
# #                 "timeframe": "1M"
# #             },
# #             {
# #                 "type": "indices",
# #                 "position": {"x": 0, "y": "60%"},
# #                 "size": {"width": "100%", "height": "40%"},
# #                 "data_sources": ["major_indices", "sector_performance", "market_breadth"],
# #                 "timeframe": "3M"
# #             }
# #         ],
# #         ticker="AAPL"
# #     )
    
# #     Step 2: If price dip detected, use financial_news() to identify catalyst
# #     news_results = financial_news(query="Apple AAPL", category="business")
# #     # Analyze news for negative sentiment, product issues, regulatory concerns, etc.
    
# #     Step 3: Highlight the price drop and reference news
# #     highlight_dashboard_element(
# #         dashboard="price_chart",
# #         element_type="chart_point",
# #         element_id="price_drop_oct_20",
# #         annotation="5% drop - see market_news for iPhone production delays"
# #     )
    
# #     Step 4: Create alert with news-based findings
# #     create_dashboard_alert(
# #         alert_type="insight",
# #         message="AAPL down 5% on news of iPhone production delays in China. Analyst downgrades citing supply chain risks.",
# #         severity="warning"
# #     )
# # """
# #  pass
