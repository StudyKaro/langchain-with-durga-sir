
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import  RunnableSequence, RunnableLambda, RunnableParallel


square_adaptor = RunnableLambda(lambda input: {"topic": input**2})
cube_adaptor = RunnableLambda(lambda input: {"topic": input**3})
parallel_chain = RunnableParallel(square=square_adaptor, cube=cube_adaptor)
parallel_result = parallel_chain.invoke(3)
print("Parallel Result:", parallel_result)
print("Square Table of content:", parallel_result["square"])
print("Cube Table of content:", parallel_result["cube"])