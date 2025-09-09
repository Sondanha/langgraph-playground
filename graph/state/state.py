from typing import Annotated, TypedDict
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages

class ChatState(TypedDict):
    # messages 리스트를 유지하면서 자동으로 누적 관리
    messages: Annotated[list[AnyMessage], add_messages]
