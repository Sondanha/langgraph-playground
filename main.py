import os, sys
from dotenv import load_dotenv
from uuid import uuid4
from langchain_core.messages import HumanMessage, AIMessage
from graph.graph import graph

# .env 로드 및 키 세팅
load_dotenv()
os.environ.setdefault("OPENAI_API_KEY", os.getenv("OPEN_API_KEY", ""))

THREAD_ID = "cli"  # 한 세션 고정. reset 시 바꿔서 초기화

def stream_chat(user_input: str):
    cfg = {"configurable": {"thread_id": THREAD_ID}}
    for state in graph.stream({"messages": [HumanMessage(content=user_input)]},
                              stream_mode="values",
                              config=cfg):
        msg = state["messages"][-1]
        if isinstance(msg, AIMessage):
            yield msg.content

if __name__ == "__main__":
    print("quit/exit/q 종료, reset 기록 초기화.")
    while True:
        user_input = input(">> ").strip()
        low = user_input.lower()
        if low in {"quit", "exit", "q"}:
            print("종료합니다."); sys.exit(0)
        if low == "reset":
            THREAD_ID = str(uuid4())  # 새 스레드로 갈아타서 히스토리 초기화
            print("기록 초기화."); continue

        for chunk in stream_chat(user_input):
            print(chunk)
