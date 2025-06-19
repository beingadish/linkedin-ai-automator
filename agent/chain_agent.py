# from langchain_ollama import OllamaLLM
# from langchain.agents import initialize_agent, AgentType
# from tools.get_username import get_username_tool

# llm = OllamaLLM(model="gemma3:1b")

# agent = initialize_agent(
#     tools=[get_username_tool],
#     llm=llm,
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     verbose=True,
#     handle_parsing_errors=True,
# )

# def get_agent():
#     return agent

