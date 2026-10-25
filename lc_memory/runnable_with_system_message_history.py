import os
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpfull assistant"),
    MessagesPlaceholder("history"), # must be follow sequence
    ("human","{input}")
])

#store history with session_id key 
# key value pair 
store ={}

def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

pipeline = prompt | llm

chain = RunnableWithMessageHistory(
    pipeline,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)
response = chain.invoke(
    input={"input":"My name is  Pradeep."},
    config={"configurable": {"session_id": "jain"}},
)
response = chain.invoke(
    input={"input":"Learning Langchain memory preservation."},
    config={"configurable": {"session_id": "jain"}},
)
response = chain.invoke(
    input={"input":"Implementing through Python"},
    config={"configurable": {"session_id": "jain"}},
)
response = chain.invoke(
    input={"input":"What is my name?"},
    config={"configurable": {"session_id": "jain"}},
)
print(response.content)

response = chain.invoke(
    input={"input":"My name is  Vandana."},
    config={"configurable": {"session_id": "vandana"}},
)
response = chain.invoke(
    input={"input":"I am Pregnant, 3rd trimister running."},
    config={"configurable": {"session_id": "vandana"}},
)
response = chain.invoke(
    input={"input":"Learning how to care baby"},
    config={"configurable": {"session_id": "vandana"}},
)
response = chain.invoke(
    input={"input":"What is my name?"},
    config={"configurable": {"session_id": "vandana"}},
)

print("============STORED SESSION=======")
for key,value in store.items():
    print(f" Session - Key : {key}, Value : {value}")


    
    
        
        
