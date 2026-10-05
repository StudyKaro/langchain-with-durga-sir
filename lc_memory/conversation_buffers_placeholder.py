import os

from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationChain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful tutor for LangChain."),
    # Insert previous human and AI messages before the current question.
    MessagesPlaceholder(variable_name="history"),
    ("human", "{topic}"),
])

# The memory_key must match the placeholder's variable_name.
# return_messages=True supplies message objects instead of one history string.
memory = ConversationBufferMemory(memory_key="history", return_messages=True)

# conversation chain deal with memory automatically.
# It will save the conversation history in memory and retrieve it when needed.
chain = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
)

while True:
    chat = input("YOU: ")
    if chat.lower() == "exit":
        print("Chat ended.")
        break
    # call LLM(model)
    result = chain.invoke({"topic":chat}) # call to prompt and replace topic
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
