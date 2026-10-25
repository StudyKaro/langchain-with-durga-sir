import os
import json
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import BaseMessage,message_to_dict,messages_from_dict
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-5-nano",api_key=os.getenv("OPENAI_API_KEY"))

prompt = ChatPromptTemplate(
    [
        ("system","""
         Your are a helpful AI assistant.
         Respond in simple English.
         """),
        MessagesPlaceholder("history"),
        ("human","{user_input}")
    ]
)

chain = prompt | llm

class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id,storage_path = "chat_history"):
        self.session_id = session_id
        os.makedirs(storage_path,exist_ok=True)
        self.file_path = os.path.join(storage_path,f"{session_id}.json")
        
    @property
    def messages(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path,"r",encoding="utf-8") as file:
           json_file = json.load(file)
        #    self.messages = messages_from_dict(json_file)
           return messages_from_dict(json_file)
       
    def add_messages(self,messages:list[BaseMessage]):
        existing_messages = list(self.messages)
        existing_messages.extend(messages)
        serialized = [message_to_dict(m) for m in existing_messages]
        with open(self.file_path,"w",encoding="utf-8") as file:
            json.dump(serialized,file,ensure_ascii=False,indent=2)

    def clear(self):
        def clear(self):
            if os.path.exists(self.file_path):
             os.remove(self.file_path)
    
def get_session_history(session_id):
    return FileChatMessageHistory(session_id)

wrapper = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="user_input",
    history_messages_key="history"
)

# session_id = input("Enter session ID: ")
# while True:
#     user_input = input("YOU: ")
#     if user_input.lower() == "exit":
#         break
#     response = wrapper.invoke(
#         {"user_input":user_input},
#         config={
#             "configurable":{
#                 "session_id":session_id
#             }
#         }
#     )
#     print("AI: ",response.content,"\n")
def authentications():
    option = int(input("""
        1. Sign Up
        2. Sign In
        Choose your otion 1 or 2 : 
        """))
    if option == 1:
        name = input("Enter name: ").strip()
        user_name = input("user_name: ").strip().lower()
        password = input("password: ")
        if not name or not user_name or not password:
            print("all fields are required")
            return
        
        users = {
            "user_name":user_name,
            "password":password
        }
        with open("users.json","a",encoding="utf-8") as file:
            json.dump(users,file,indent=2)
            print("successfully sign up.")
    elif option == 2:
        user_name = input("Enter user_name :").lower()
        password = input("Enter password :").lower()
        with open("users.json","r",encoding="utf-8") as file:
            data = json.load(file)
            print("successfully sign in.")
authentications()