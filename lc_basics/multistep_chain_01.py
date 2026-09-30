import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import  RunnableSequence
from langchain_core.runnables import RunnableLambda

        #  Components:
llm = ChatOpenAI(model="gpt-4o-mini",api_key=os.getenv("OPENAI_API_KEY")) # model component
prompt = ChatPromptTemplate.from_messages([
 ("system","""Your a helpful bussiness assistant. Provide all basic to advance 
  informationa and step by step friendly assistance.
  Advice practical approaches with steps and realtime ideas. """),
        ("human","{topic}")
]
)
parser = StrOutputParser()
def provide_argument():
        return "China"
        
# custom Runnable compoment that convert string message into the compatible dict object
dict_adaptor = RunnableLambda(lambda input: {"outline":input, "language": "Hindi"})

llm2 = ChatOpenAI(model="gpt-5-nano",api_key=os.getenv("OPENAI_API_KEY"))
prompt2 = PromptTemplate.from_template("""
                                       Prepare a actionable plan with achieavable steps.
                                       On the topic :
                                       {outline}
                                       Rules:
                                       1. Explain in simple {language} language
                                       2. Practicle possible
                                       3. Conclude with loopholes and common mistakes.
                                       """)
topic = input("Enter topic :")
chain = prompt | llm | parser | dict_adaptor | prompt2 | llm2 | parser
for result in chain.stream({"topic":topic}):
        print(result,end="",flush=True)
