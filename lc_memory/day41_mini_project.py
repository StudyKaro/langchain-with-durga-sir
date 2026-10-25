import os
import json
from langchain_core.messages import BaseMessage,AIMessage,SystemMessage, HumanMessage,message_to_dict, messages_from_dict
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory, BaseChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

#----------------------------------#
#-------GPT MODEL CONNECTION-------#
#----------------------------------#
llm = ChatOpenAI(model="gpt-4o-mini",api_key=os.getenv("OPENAI_API_KEY"))

#----------------------------------#
#-----------PROMPT-----------------#
#----------------------------------#

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful AI digital assistant."),
        MessagesPlaceholder(variable_name = "history"),
        ("human","{user_query}")
    ]
)

#----------------------------------#
#----------- CHAIN ----------------#
#----------------------------------#

chain = prompt | llm

#============= File Chat Memory
class FileChatMessageHistory(BaseChatMessageHistory): # extending and overriding its methods
    def __init__(self,session_id,storage_path = "chat_history"):
        self.session_id = session_id
        os.makedirs(storage_path,exist_ok=True)
        self.file_path = os.path.join(storage_path,f"{session_id}.json")
    @property
    def messages(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path,"r",encoding="utf-8") as file:
            data = json.load(file)
            return messages_from_dict(data)
        
    def add_messages(self, messages:list[BaseMessage]) -> None:
        all_existing_messages = list(self.messages)
        all_existing_messages.extend(messages)
        serialized = [message_to_dict(message) for message in all_existing_messages]
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(serialized,file,ensure_ascii=False,indent=2)
    def clear(self):
        return super().clear()

def get_session_history(session_id):
    return FileChatMessageHistory(session_id)

#-------------------------------------#
#------------In Memory-----------------#
#-------------------------------------#
store = {}
def get_history_by_session(sesson_id):
    if history_type == "memory": 
        if sesson_id not in store :
            store[sesson_id] = InMemoryChatMessageHistory()
        return store[sesson_id]
    else:
        return  FileChatMessageHistory(session_id)

#-------------------------------------#
#------------Runnable-----------------#
#-------------------------------------#

wrapper = RunnableWithMessageHistory(
    chain,
    get_history_by_session,
    # get_session_history,
    input_messages_key="user_query",
    history_messages_key="history"
)

history_type = input("History Type (Memory/File): ").lower()

session_id = input("Enter session id: ")

while True:
    user_query  = input("YOU: ")
    if user_query.lower() == "exit":
        print("Chat ended.")
        break
    response = wrapper.invoke(
        {"user_query": user_query},
        config={
            "configurable" :{
                "session_id":session_id
                } 
        }
        )
    print("AI:",response.content,"\n")