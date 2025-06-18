from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType

# Create a dummy tool for now
def dummy_tool_function(input_text: str) -> str:
    return f"Received: {input_text}"

tools = [
    Tool(
        name="EchoTool",
        func=dummy_tool_function,
        description="Echoes the input back to the user."
    )
]

# Initialize the LLM with the correct model
llm = OllamaLLM(model="gemma3:1b")

# Initialize the agent with at least one tool
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def get_agent():
    return agent
