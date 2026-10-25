from pydantic import BaseModel,Field
from langchain_openai import ChatOpenAI
import os
llm = ChatOpenAI(model='gpt-5-nano', api_key=os.getenv("OPENAI_API_KEY"))
class Student(BaseModel):
    name:str = Field(description="Name of student")
    age: int = Field(gt=18,lt=80, description="Age of student.",)
    course:str = Field(default="Langchain", description="Subject or course of student that learning.")
    
# bind schema to llm 
schema_llm = llm.with_structured_output(Student)

query = input("You: ")
response = schema_llm.invoke(query)
print("==== Student detail=====")
print(response.name)
print(response.age)
print(response.course)
print("=========Python dict========")
print(response.model_dump())
print("=========JSON string ========")
print(response.model_dump_json())

# My teacher name is Ram Babu who is around 50 years old and still teaching Java. I am Pradeep jain learning Python
# My teacher name is Ram Babu who is around 50 years old and still teaching Java. I am Pradeep jain learning Python in 35 age
# I am Pradeep
