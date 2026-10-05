from langchain_classic.memory import ConversationBufferMemory, ConversationBufferWindowMemory

 # return_messages=True . help to return in message object format instead of string format
memory = ConversationBufferWindowMemory(return_messages=True, k=2) 
# k=2 means not 2 messages 
# k=2 means last 2 interactions/turn (1 human message + 1 AI message) will be stored in the memory buffer.
    # Save some interaction history
memory.save_context(
        {"input": "Hi, my name is Alice."},
        {"output": "Hello Alice! How can I help you today?"}
    )
memory.save_context(
        {"input": "Learning Langchain"},
        {"output": "Great to hear!"}
    )
memory.save_context(
        {"input": "What is trap"},
        {"output": "Might be a problem"}
    )
memory.save_context(
        {"input": "What kind of human trap"},
        {"output": "Perfection, Motivation and Comparison."}
    )
    # Retrieve the memory variables to pass into a prompt
memory_vars = memory.load_memory_variables({})
for m in memory_vars['history']:
    print(f"{type(m).__name__}: {m.content}")
