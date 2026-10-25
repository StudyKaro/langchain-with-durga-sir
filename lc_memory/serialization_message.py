import os
import json
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage,message_to_dict,messages_from_dict
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

prompt = ChatPromptTemplate.from_messages([
    SystemMessage("Your a helpful assistant."),
    HumanMessage("Hi, I am Pradeep Jain."),
    AIMessage("Nice to meet you pradeep.")
]
)

print(prompt.messages)

#----------------------#
#----Serialization----#
# Mumbai baloon wala example-> bollon plyable, but not transporatable, remove air so transport and again fill air and play
#-- convert into dict---#
#---------------------#
#-- convert into dict---#
serialized_message = [message_to_dict(message) for message in prompt.messages]
print(serialized_message)

# dict to json, json object is universaly transportable

dict_to_json = json.dumps(serialized_message, indent=2)
print(dict_to_json)

json_to_dict = json.loads(dict_to_json)
print(json_to_dict)

#-----Deserialization-----#
deserialized = messages_from_dict(json_to_dict)
print(deserialized)

