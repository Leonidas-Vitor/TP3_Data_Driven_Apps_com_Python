"""Utility functions and classes."""
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import MessagesPlaceholder
from langgraph.checkpoint.memory import MemorySaver

def init_memory():
    """Initialize the memory for contextual conversation.

    We are caching this, so it won't be deleted
     every time, we restart the server.
    """
    return ConversationBufferMemory(
        memory_key="chat_history", return_messages=True, k=3#, output_key="answer"
    )
    #return MemorySaver()


MEMORY = init_memory()
CHAT_HISTORY = MessagesPlaceholder(variable_name="chat_history")