from pydantic import BaseModel
# BaseModel is Parent class must be extend
# reponsible to define schema and validation
# in schema every element by default mandatoy
# schema mean define type and fields name
class Student(BaseModel):
    name:str 
    age: int
    course:str
s = Student(name="Vandhu",age=34,course="Moksha Shashtra") 
# there is no such param constructor bcoz take care by BaseModel 
print(s)
# s directly print magic method take care by BaseModel

# s1 = Student(name="Vandhu",age=34) # validation error for course
#print(s1)
s2 = Student(name="Vandhu",age='34',course="Moksha Shashtra") # for age convert automatically
print(s2)

# s3 = Student(name="Vandhu",age='thirty four',course="Moksha Shashtra") # validation error
# print(s3)

data = s.model_dump() # convert into dict
print(data)
json_string = s.model_dump_json() # convert into json
print(json_string)