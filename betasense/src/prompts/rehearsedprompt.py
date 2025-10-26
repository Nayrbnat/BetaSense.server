
VALUE_INVESTOR_AAPL_ANALYSIS = """
# Value Investment Analysis: AAPL
## Question: Is AAPL a good investment from a value investor perspective?

### STEP 1: Peer Comparison
comparable_multiples(search_query="AAPL vs MSFT GOOGL META P/E P/B P/FCF ROE ROIC comparison")

### STEP 2: Show Portfolio Context
control_browser(panel="portfolio-monitor", action="maximize")
emit_thinking_process("Opening portfolio monitor to see how AAPL compares to the rest of the holdings. This gives context on relative positioning.")
[Analyze and comment on AAPL's position in portfolio]
control_browser(panel="portfolio-monitor", action="minimize")

### STEP 3: AAPL Fundamentals
financials(search_query="AAPL ROIC ROE free cash flow debt-to-equity margins")

### STEP 4: Check Market News
control_browser(panel="market-news", action="maximize")
emit_thinking_process("Checking recent market news for AAPL. Looking for catalysts, sentiment, or risks that might impact the investment thesis.")
[Analyze recent news and sentiment]
control_browser(panel="market-news", action="minimize")

### STEP 5: Quality Assessment
performance_analysis(search_query="AAPL margin trends profitability")

### STEP 6: Valuation Check
street_consensus(search_query="AAPL price targets fair value")

### STEP 7: Recommendation
emit_finding_summary("
VERDICT: [BUY/HOLD/AVOID]
Quality: ROIC X%, Margins [trend], Moat [strength]
Valuation: [premium/discount] vs peers, margin of safety X%
Action: [Clear 2-sentence recommendation]
")
"""
