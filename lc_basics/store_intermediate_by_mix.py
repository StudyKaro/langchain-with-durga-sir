from langchain_core.runnables import RunnablePassthrough
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import  RunnableSequence
from langchain_core.runnables import RunnableLambda

llm = ChatOpenAI(model="gpt-4o-mini",api_key=os.getenv("OPENAI_API_KEY")) # model component
prompt = ChatPromptTemplate.from_messages([
 ("system","""Your a helpful bussiness assistant. Provide all basic to advance 
  informationa and step by step friendly assistance.
  Advice practical approaches with steps and realtime ideas. """),
        ("human","{topic}")
]
)
parser = StrOutputParser()

chain_with_values = (
    RunnablePassthrough.assign(
        topic=lambda data: data["input"],
    )
    | 
    prompt
    | llm
    | parser
)

result = chain_with_values.invoke({"input": "Jainism"})

print(result)