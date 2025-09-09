from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from graph.state.state import ChatState
from graph.nodes.chatbot_node import chatbot_node


# 그래프가 상태를 저장하여 멀티턴 가능
memory = MemorySaver()  # 메모리 체크포인터

def build_graph():
    g = StateGraph(ChatState)
    g.add_node("chatbot", chatbot_node)
    g.add_edge(START, "chatbot")
    g.add_edge("chatbot", END)
    return g.compile(checkpointer=memory)  # 체크포인터 장착

graph = build_graph()
