from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import RunnableSequence
store_val ={}
# callable functions to be used in the chain
def add_fun(input):
    result = input + 10
    print(result)
    store_val["add_result"] = result
    return result
def mult_fun(input):
    result = input * 2
    store_val["mult_result"] = result
    print(result)
    return result
def sub_fun(input):
    result = input - 5
    store_val["sub_result"] = result
    print(result)
    return result

# `RunnableLambda` converts a python callable into a `Runnable`.
add_adaptor = RunnableLambda(add_fun)
mult_adaptor = RunnableLambda(mult_fun)
sub_adaptor = RunnableLambda(sub_fun)
# can call a single component 
# print("Call Add_Adaptor with input 5: ",add_adaptor.invoke(5))

chain = add_adaptor | mult_adaptor | sub_adaptor
# input only on first component of the chain, rest of the components will get the output of previous component as input
result = chain.invoke(5)
print("Final Result:", result)
print("Stored Values:", store_val)

chain2 = RunnableSequence(add_adaptor, mult_adaptor, sub_adaptor)
result2 = chain2.invoke(10)
print("Final Result (Chain 2):", result2)
print("Stored Values (Chain 2):", store_val)

for result3 in RunnableSequence(add_adaptor, mult_adaptor, sub_adaptor).batch([3,4,30]):
    print("Final Result (Batch):", result3)
print("Stored Values (Batch):", store_val)

for result4 in RunnableSequence(add_adaptor, mult_adaptor, sub_adaptor).stream(50):
    print("Final Result (streaming):", result4)
print("Stored Values (Streaming):", store_val)