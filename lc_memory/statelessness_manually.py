from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
import os

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

messages =[]
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    messages.append(HumanMessage(content=user_input))
    
    chain_result = llm.invoke(messages)
    print("\nAI: ", chain_result.content)
    
    # storing the AI response in the messages list for context history
    messages.append(chain_result)

    print("Number of messages: ", len(messages))

print("\n==========Conversation History:=================")
for message in messages:
    print(f"{type(message).__name__}: {message.content}")
    print("--------------------------------------------------")