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
    # stateless behaviour
    response = llm.invoke("I am Pradeep Jain")
    messages = []
    system_message = SystemMessage(content= "You are a helpfull AI assistant.")
    messages.append(system_message)
    while True:
        query = input("You: ")
        if query.lower().strip() == "exit":
            break
        messages.append(HumanMessage(content=query))
        response = llm.invoke(messages)
        # messages.append(AIMessage(content = response.content))
        messages.append(response)
        print("AI: ", response.content)

    print("="*20)
    print("Message conversation history")
    for message in messages:
        print(type(message).__name__)
        print(message.content)
        print()
except Exception as e:
    print("Error message: ")
    print(e)


# print("AI: ",response.content)