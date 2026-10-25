import os

from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationChain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
memory = ConversationBufferMemory(return_messages=True)

# conversation chain deal with memory automatically.
# It will save the conversation history in memory and retrieve it when needed.
chain = ConversationChain(
    llm=llm,
    memory=memory
)
while True:
    chat = input("YOU: ")
    if chat.lower() == "exit":
        print("Chat ended.")
        break
    # call LLM(model)
    result = chain.invoke({"input":chat})
    # print(result["history"])
    # print(type(result)) # dict with 'history' attribute
    for message in result["history"]:
        print(type(message).__name__," : ", message.content)

print("---------HISTORY------------")
# load the history
history = memory.load_memory_variables({})
print(history)