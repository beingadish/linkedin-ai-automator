from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import create_react_agent, ToolNode
from agent.state_schema import State
from tools.get_username import get_username_tool
from tools.get_linkedin_html import get_linkedin_html
from tools.extract_username_tool import extract_username_tool
from langchain_core.messages import AIMessage
import json
import re
import uuid

# --- Configuration ---
llm = ChatOllama(model="orieg/gemma3-tools:4b", temperature=0)
tools = [get_username_tool]
llm_with_tools = llm.bind_tools(tools)

# Create the reactive agent and tool executor node
agent_node = create_react_agent(llm_with_tools, tools)
tool_node = ToolNode(tools=tools)

# --- Graph Setup ---
builder = StateGraph(State)

MAX_STEPS = 10

def log_state(state):
    step = state.get('step', 0)
    print(f"\n[LangGraph] Step {step} State:")
    
    for msg in state.get("messages", []):
        print(f" - {msg.__class__.__name__}: {getattr(msg, 'content', '')}")
    
    last_msg = state.get("messages", [])[-1]
    if isinstance(last_msg, AIMessage):
        if last_msg.tool_calls:
            print(f"[DEBUG] Tool Calls: {last_msg.tool_calls}")

    state['step'] = step + 1
    if state['step'] > MAX_STEPS:
        print("\n[LangGraph] 🚨 SAFETY BREAKER: Exceeded max steps. Exiting.")
        raise RuntimeError("LangGraph stuck in loop")

    return state

builder.add_node("logger", log_state)
builder.add_node("agent", agent_node)
builder.add_node("tool", tool_node)

builder.add_edge(START, "logger")
builder.add_edge("logger", "agent")

def should_route(state):
    messages = state["messages"]
    last = messages[-1]
    if isinstance(last, AIMessage):
        if last.tool_calls:
            return "tool"
        if last.content:
            return END
    return "agent"

builder.add_conditional_edges("agent", should_route, {
    "tool": "tool",
    END: END,
    "agent": "agent"
})
builder.add_edge("tool", "agent")

def parse_tool_call(state):
    messages = state["messages"]
    last = messages[-1]
    if not (isinstance(last, AIMessage) and last.content):
        return state

    match = re.search(r"```tool_call>\s*(.*?)\s*```", last.content, re.DOTALL)
    if not match:
        return state

    raw = match.group(1).strip()
    print("[DEBUG] Raw tool_call:\n", raw)

    # Strip trailing noise like </tool_call>
    pos = raw.rfind('}')
    json_text = raw[:pos+1]

    try:
        data = json.loads(json_text)
    except json.JSONDecodeError as e:
        print("[DEBUG] ❌ JSON error:", e)
        return state

    # Flatten 'parameters' → 'args'
    if "parameters" in data:
        data = {
            "name": data["name"],
            "args": data["parameters"]
        }

    # 🎯 Add missing 'id' and 'type'
    call_id = str(uuid.uuid4())
    data["id"] = call_id
    data["type"] = "tool_call"

    # Replace AIMessage with validated tool call
    new_msg = AIMessage(
        content="",
        tool_calls=[data],
        additional_kwargs=last.additional_kwargs,
        response_metadata=last.response_metadata,
        id=last.id,
    )
    messages[-1] = new_msg
    print(f"[DEBUG] ✅ Injected tool_call with id={call_id}")
    
    return state


builder.add_node("parse_tool_call", parse_tool_call)
builder.add_edge("agent", "parse_tool_call")
builder.add_edge("parse_tool_call", "tool")

# Final compiled app
app = builder.compile()