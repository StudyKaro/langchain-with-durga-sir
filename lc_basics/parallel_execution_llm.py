
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (RunnableSequence,
                                      RunnableLambda,
                                      RunnableParallel)

llm = ChatOpenAI(model="gpt-4o-mini",api_key=os.getenv("OPENAI_API_KEY")) # model component
prompt1 = PromptTemplate.from_template("Generate a clean and funny joke on : {topic}. ")
prompt2 = PromptTemplate.from_template("A strong motivational message on {topic}.")
parser = StrOutputParser()

joke_chain = prompt1| llm | parser #Branch1
motivate_chain = prompt2 | llm | parser #Branch2

# RunnableParallel allows run multiple chains in parallel and get their results in a single dictionary.
# Same input passed to all branches, and each branch can have its own chain of components.
parallel_chain = RunnableParallel(
    joke=joke_chain, #Branch1 Name : joke => that name used in dict to access the result of that branch
    motivate=motivate_chain #Branch2 Name : motivate => that name used in dict to access the result of that branch
)
topic = input("Enter topic :")

# Single input to the parallel chain, which will be passed to both branches
parallel_result = parallel_chain.invoke({"topic": topic})
print("Parallel Result:", parallel_result)
print("Joke:", parallel_result["joke"])
print("Motivate:", parallel_result["motivate"])