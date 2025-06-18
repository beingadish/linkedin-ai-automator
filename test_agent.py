from agent.decision_engine import get_agent

# Get the agent
agent = get_agent()

# Test the agent with a sample prompt
response = agent.invoke("What can you do?")

# Print the response
print(response)
