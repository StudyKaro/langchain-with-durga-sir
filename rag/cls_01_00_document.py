from langchain_core.documents import Document

#we can create manual Document Object
# Document is a class
# Usually DocumentLoader create the Object of Document class, But manually also create
# Document class has two propery 1. page_content->str 2. metadata-> dict
# page_content = original page 
# metadata = additional info , its in dict type and optional
document = Document(page_content="Read a page of Memory.")

print("Document Object : ")
print(type(document).__name__) # document

print(document.page_content) # content