from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
import os

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

system_message = SystemMessage(content="You are a helpful assistant.Provide answer in Hindi)")
#  to store complete conversation history
messages =[]
messages.append(system_message)
MAX_HISTORY_LENGTH = 6  # Maximum number of messages to keep in history
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == 'exit':
        break
    messages.append(HumanMessage(content=user_input))
    # Recent window or recent history approach: Only keep the last MAX_HISTORY_LENGTH messages for context
    # MAX_HISTORY_LENGTH = -6, -6 means last 6 recent messages
    recent_messages = messages[-MAX_HISTORY_LENGTH:]  # fetch last 6 messages
    history_messages = [system_message,*recent_messages] # unpacked recent messages and added system message to the history messages
    chain_result = llm.invoke(history_messages)
    print("\nAI: ", chain_result.content)
    
    # storing the AI response in the messages list for context history
    
    messages.append(chain_result)

    print("Number of messages: ", len(messages))
    print("Number of recent messages: ", len(recent_messages))
    print("Number of messages sent to model: ", len(history_messages))

print("\n==========Conversation History:=================")
for message in messages:
    print(f"{type(message).__name__}: {message.content}")
    print("--------------------------------------------------")
    
print("\n==========Recent Conversation History:=================")
for message in recent_messages:
    print(f"{type(message).__name__}: {message.content}")
    print("--------------------------------------------------")