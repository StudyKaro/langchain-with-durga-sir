from langchain_community.document_loaders import WebBaseLoader
loader= WebBaseLoader(web_path="https://www.durgasoftonline.com/s/pages/new-batches")
documents = loader.load()

print("List of Document: ",len(documents))
document = documents[0]

print("Page Content: ",document.page_content)
print("Metadata : ",document.metadata)