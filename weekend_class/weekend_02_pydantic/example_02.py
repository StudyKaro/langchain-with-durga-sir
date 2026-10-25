from pydantic import BaseModel
from langchain_openai import ChatOpenAI
import os
llm = ChatOpenAI(model='gpt-5-nano', api_key=os.getenv("OPENAI_API_KEY"))
class Student(BaseModel):
    name:str 
    age: int
    course:str
    
# bind schema to llm 
schema_llm = llm.with_structured_output(Student)

query = input("You: ")
response = schema_llm.invoke(query)
print(response)
# try different input and check response
# Ram kumar is working in software company since 2010. now technology is going to change and company adopting AI. Microsoft is also hiring N8N experience person.
