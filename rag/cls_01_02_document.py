from langchain_core.documents import Document

document = Document(
    page_content="Bring the ID, its compusory",
    metadata = {
        "source":"school_rule.txt",
        "department":"administration"
    })

print("=== About ===")

print(document.page_content) 

print(document.metadata)

print(document.metadata["source"])

print(document.metadata["department"])

# print(document.metadata["author"]) #KeyError -> because key is missing

# How to avoid  KeyError even key is missing
# use get() method
print(document.metadata.get("author")) # None

print(document.metadata.get("author","Not declared"))

