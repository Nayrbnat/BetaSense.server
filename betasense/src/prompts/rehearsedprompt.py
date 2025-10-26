
VALUE_INVESTOR_AAPL_ANALYSIS = """
# Value Investment Analysis: AAPL
## Question: Is AAPL a good investment from a value investor perspective?

### STEP 1: Peer Comparison
emit_thinking_process("Starting with peer comparison to see how AAPL's valuation and quality metrics stack up against MSFT, GOOGL, and META. This will show if AAPL is relatively cheap or expensive.")
comparable_multiples(search_query="AAPL vs MSFT GOOGL META P/E P/B P/FCF ROE ROIC comparison")
emit_thinking_process("Analyzing the comparable data. Looking at relative valuation multiples and quality metrics to establish baseline.")

### STEP 2: Show Portfolio Context
emit_thinking_process("Now checking portfolio positioning to understand AAPL's weight and performance relative to other holdings.")
control_browser(panel="portfolio-monitor", action="maximize")
emit_thinking_process("Opening portfolio monitor to see how AAPL compares to the rest of the holdings. This gives context on relative positioning.")
[Analyze and comment on AAPL's position in portfolio]
control_browser(panel="portfolio-monitor", action="minimize")
emit_thinking_process("Portfolio context established. Moving to deep dive on AAPL fundamentals.")

### STEP 3: AAPL Fundamentals
emit_thinking_process("Pulling AAPL's core financial metrics: ROIC, ROE, FCF, debt levels, and margins. Value investors need >15% ROIC and low debt.")
financials(search_query="AAPL ROIC ROE free cash flow debt-to-equity margins")
emit_thinking_process("Reviewing the fundamental data to assess business quality and financial health.")

### STEP 4: Check Market News
emit_thinking_process("Checking recent news and sentiment. Need to identify any catalysts or risks that could impact the investment thesis.")
control_browser(panel="market-news", action="maximize")
emit_thinking_process("Checking recent market news for AAPL. Looking for catalysts, sentiment, or risks that might impact the investment thesis.")
[Analyze recent news and sentiment]
control_browser(panel="market-news", action="minimize")
emit_thinking_process("News review complete. Now assessing business quality and margin trends.")

### STEP 5: Quality Assessment
emit_thinking_process("Analyzing profitability trends and margin stability. Value investors want consistent or expanding margins as proof of competitive moat.")
performance_analysis(search_query="AAPL margin trends profitability")
emit_thinking_process("Evaluating margin trends and operational performance to confirm business quality.")

### STEP 6: Valuation Check
emit_thinking_process("Checking street consensus for price targets and fair value estimates. This helps establish margin of safety calculation.")
street_consensus(search_query="AAPL price targets fair value")
emit_thinking_process("Comparing current price to consensus targets to determine if there's adequate margin of safety (need 30-40% discount).")

### STEP 7: Recommendation
emit_thinking_process("Synthesizing all data: peer comparison, fundamentals, news, quality metrics, and valuation. Building final recommendation.")
emit_finding_summary("
VERDICT: [BUY/HOLD/AVOID]
Quality: ROIC X%, Margins [trend], Moat [strength]
Valuation: [premium/discount] vs peers, margin of safety X%
Action: [Clear 2-sentence recommendation]
")
"""
