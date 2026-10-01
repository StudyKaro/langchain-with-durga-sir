from langchain_core.runnables import RunnablePassthrough

chain_with_values = (
    RunnablePassthrough.assign(
        add_result=lambda data: data["input"] + 10
    )
    | RunnablePassthrough.assign(
        mult_result=lambda data: data["add_result"] * 2
    )
    | RunnablePassthrough.assign(
        sub_result=lambda data: data["mult_result"] - 5
    )
)

result = chain_with_values.invoke({"input": 5})

print(result)