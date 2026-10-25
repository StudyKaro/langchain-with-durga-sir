from langchain_core.documents import Document

document = Document(
    page_content="Read a page of Memory.",
    metadata = {
        "source":"memory_ebook.pdf",
        "department":"self improvement",
        "author":"walker atkinson"
    })

print("=== About ===")
print(type(document).__name__) # document

print(document.page_content) # content

print(document.metadata)

# get meta info, its not fix vary according to requirement.
print(document.metadata["source"])

print(document.metadata["department"])

print(document.metadata["author"])