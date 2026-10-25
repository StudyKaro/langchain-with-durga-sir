from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, AIMessage,HumanMessage
from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(model="gpt-4o-mini",api_key=os.getenv("OPENAI_API_KEY"))
messages = [
    SystemMessage(content="""You are a helpful travel assistant. Provide travel guide base on user corncerns.
     Rules:
     1. Provide travel plan with day wise activities.
     2. Include travel tips and local attractions.
     3. Include food and accommodation suggestions.
     4. Provide a estimated time on activities and travel time.
     5. Practical and realistic suggestions.
     Output format :
     Format the output in a clear and organized manner. 
     Day wise activities should be in bullet points with estimated time for each activity.
     
     additionally : wish to User with name.
     """),
        HumanMessage(content =
                     """Provide travel plan :
     Name : Pradeep
     Destination : Laddakh
     Budget :  80000 INR
     Duration: 7 days.
     """)
]


 
chain_result = llm.invoke(messages)
while True:
    print("===========Result=========")
    print(chain_result.content)
    input_text = input("\n\nDo you have any other questions or concerns? (Type 'exit' to quit): ")
    if input_text.lower() == 'exit':
        break
    messages.append(chain_result)
    messages.append(HumanMessage(content=input_text))
    chain_result = llm.invoke(messages)