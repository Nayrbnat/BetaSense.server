from agents import function_tool


@function_tool
def emit_thinking_process(thinking_process: str):
    """
    Call this tool to emit the agent's thinking process at any point in time.

    Make sure you write a 1-2 senteces of detailed and clear thinking process to help the user understand your reasoning. 
    Make it engaging to the user and make them feel involved in the conversation - they need to feel that you are working as hard as possible to help them!
    Make it super rigorous, as if you are tackling a very hard problem - no matter how simple the user's question is.
    """
    return thinking_process


@function_tool
def emit_finding_summary(finding_summary: str):
    """
    Call this tool to emit a summary of findings after using all the tools to gather information.

    Make sure this summary is professional, beautiful, sounds like a star-level analyst, and captures all the key insights you have found using the tools.
    Any PM should be ultra impressed by your summary! Your objective of calling this tool is to wow them with your deep insights and analysis.
    """
    return finding_summary

@function_tool
def parse_pdf():
    pass


@function_tool
def parse_excel():
    pass


@function_tool
def read_image():
    pass