import os

from langchain_classic.memory import ConversationBufferMemory, ConversationBufferWindowMemory
from langchain_classic.chains import ConversationChain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
# k=2 turn, save latest or say last 2 turn(4 messages), ealier messages will drop
memory = ConversationBufferWindowMemory(return_messages=True, k=2)

# conversation chain deal with memory automatically.
# It will save the conversation history in memory and retrieve it when needed.
chain = ConversationChain(
    llm=llm,
    memory=memory
)
# result = chain.invoke({"input":"I am Pradeep"})
# print(result)
while True:
    chat = input("YOU: ")
    if chat.lower() == "exit":
        print("Chat ended.")
        break
    # call LLM(model)
    result = chain.invoke({"input":chat})
    # print(result["history"])
    # return AI response
    print(result["response"])
    # print(type(result)) # dict with 'history' attribute
    # for message in result["history"]:
    #     print(type(message).__name__," : ", message.content)

print("---------HISTORY------------")
# load the history
history = memory.load_memory_variables({})
# print(history)

for message in history["history"]:
    print(type(message).__name__," : ", message.content)