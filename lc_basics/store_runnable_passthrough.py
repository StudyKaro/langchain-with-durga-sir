from langchain_core.runnables import RunnableParallel, RunnablePassthrough,RunnableLambda

double_adaptor = RunnableLambda(lambda input: input * 2)
square_adaptor = RunnableLambda(lambda input: input ** 2)
cube_adaptor = RunnableLambda(lambda input: input ** 3)

chain = RunnableParallel(
    double=double_adaptor,
    square=square_adaptor,
    cube=cube_adaptor,
    original=RunnablePassthrough()
)
# result = chain.batch([3,5,10])
# print("===========Result=========")
# for key in result:
#     for k,v in key.items():
#         print(k.capitalize(),":",v)
#     print("============")

result = chain.invoke(5)
print("===========Result=========")
for key, value in result.items():
    print(f"{key.capitalize()}: {value}")
print("============")
