import os

from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

# memory = InMemoryChatMessageHistory()
# memory.add_user_message("Hi, I am Pradeep Jain")
# memory.add_ai_message("Nice to meet you Pradeep!")
# print(memory)

#store history with session_id key  
# generate the session_id
store ={}
def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]
# pass model and memory
chain = RunnableWithMessageHistory(
    llm,
    get_session_history
)
response = chain.invoke(
    [HumanMessage(content="My name is  Pradeep.")],
    config={"configurable": {"session_id": "jain"}},
)
response = chain.invoke(
    [HumanMessage(content="I live in Sagar.")],
    config={"configurable": {"session_id": "jain"}},
)
response = chain.invoke(
    [HumanMessage(content="Looking bridal for my brother.")],
    config={"configurable": {"session_id": "jain"}},
)
response = chain.invoke(
    [HumanMessage(content="What is my name?")],
    config={"configurable": {"session_id": "jain"}},
)
print(response.content)


    
    
        
        
