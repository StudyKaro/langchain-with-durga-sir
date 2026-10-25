import os
import json
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage,message_to_dict

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

session_id = input("Session Id ? ").lower()

os.makedirs("chat_history",exist_ok=True)
# file_path = os.path.join(working_directory,session_id+".txt")

print("### To quit/exit chat - type 'exit' ###")


store ={}
def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chain = RunnableWithMessageHistory(llm,get_session_history)

while True:
    user_input = input("YOU: ")
    if user_input.lower() == "exit":
        break
    response = chain.invoke(
        [HumanMessage(content = user_input)],
        config={"configurable": {"session_id":session_id }}
    )
    
    # print("===========data in store==========","\n",store[session_id])
    # with open("chat_history"+"/"+session_id+".txt","w",encoding="utf-8") as file:
    #     file.write(json.dumps(message_to_dict()))
    
    # print("AI: ",response)
    serialized  = [ message_to_dict(message) for message in store[session_id]]
    print(serialized)
    print("\n")
        
    
print("chat ended.")