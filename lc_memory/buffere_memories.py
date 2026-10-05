from langchain_classic.memory import ConversationBufferMemory

    # Initialize the memory buffer
memory = ConversationBufferMemory()

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
print(memory_vars)