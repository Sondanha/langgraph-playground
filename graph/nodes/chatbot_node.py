from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage
from graph.state.state import ChatState

def chatbot_node(state: ChatState) -> dict:
    # 여기서 매번 LLM 객체 생성 (API 키는 이미 load_env()로 환경에 있음)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    ai = llm.invoke(state["messages"])
    return {"messages": [AIMessage(content=ai.content)]}
