from agent.decision_engine import app

if __name__ == "__main__":
    initial_state = {
        "messages": [
            {"role": "system", "content": "Always use available tools to answer user questions."},
            {"role": "user", "content": "What is my LinkedIn display name?"}
        ],
        "username": ""
    }

    result = app.invoke(initial_state)
    print("\n✅ Final State:", result)
    print("\n📨 Messages:")
    for msg in result["messages"]:
        print(msg)