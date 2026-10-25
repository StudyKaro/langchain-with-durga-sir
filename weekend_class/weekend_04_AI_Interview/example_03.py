from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage,SystemMessage, HumanMessage
import os
from getpass import getpass

# getpass is python library that read the password/secret key without showing on screen
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    api_key = getpass("Enter the secrete api key.").strip()

if not api_key:
    raise ValueError("Model API require.")

try:
    llm = ChatOpenAI(api_key=api_key, model = "gpt-5-mini")
    # LLM is gajani
    response = llm.invoke("I am Pradeep Jain")
    print("="*20) # 20 times
    print("First response :","\n", response.content)
    
    response1 = llm.invoke("What is my name?")
    print("="*20) # 20 times
    print("Second response :","\n", response1.content)
    
except Exception as e:
    print("Error message: ")
    print(e)


# print("AI: ",response.content)