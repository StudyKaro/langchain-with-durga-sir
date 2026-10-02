from langchain_core.runnables import RunnableBranch,RunnableLambda,RunnableSequence

# Example 1

runnable_branch1 = RunnableLambda(lambda input: "PASS")
runnable_branch2 = RunnableLambda(lambda input: "FAIL")


runnable_branch = RunnableBranch(
    (lambda input: input > 35 , runnable_branch1),
    runnable_branch2
)

runnable_branch_result = runnable_branch.invoke(40)
print("Runnable Branch Result:", runnable_branch_result)

# Example 2 :

branch = RunnableBranch(
    (lambda input: input%2 == 0 , RunnableLambda(lambda input: "EVEN")),  
    RunnableLambda(lambda input: "ODD")
)
branch_result = branch.invoke(7)
print("Branch Result:", branch_result)

# Example 3 :

branch1 = RunnableBranch(
    (lambda input: (input%6) == 1 ,lambda input: "Move one step forward"),  
    (lambda input: (input%6) == 2 ,lambda input: "Move two steps forward"),  
    (lambda input: (input%6) == 3 ,lambda input: "Move three steps forward"),  
    (lambda input: (input%6) == 4 ,lambda input: "Move four steps forward"),  
    (lambda input: (input%6) == 5 ,lambda input: "Move five steps forward"),  
    lambda input: "Move six steps forward" # default is mandatory 
)

input_value = int(input("Roll the disc: "))
branch_result1 = branch1.invoke(input_value)
print("Branch Result:", branch_result1)
