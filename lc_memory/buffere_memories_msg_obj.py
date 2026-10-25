from langchain_classic.memory import ConversationBufferMemory

 # return_messages=True . help to return in message object format instead of string format
memory = ConversationBufferMemory(return_messages=True)

    # Save some interaction history
memory.save_context(
        {"input": "Hi, my name is Alice."},
        {"output": "Hello Alice! How can I help you today?"}
    )
memory.save_context(
        {"input": "Learning Langchain"},
        {"output": "Great to hear!"}
    )

    # Retrieve the memory variables to pass into a prompt
memory_vars = memory.load_memory_variables({})
for m in memory_vars['history']:
    print(f"{type(m).__name__}: {m.content}")
# HumanMessage: Hi, my name is Alice.
# AIMessage: Hello Alice! How can I help you today?
# HumanMessage: Learning Langchain
# AIMessage: Great to hear!
