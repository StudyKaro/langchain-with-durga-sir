from langchain_community.document_loaders import WebBaseLoader
loader= WebBaseLoader(
    web_path="https://www.durgasoftonline.com/s/pages/new-batches",
    bs_get_text_kwargs={
        "separator":" ", # can use '\n', ',' etc. 
        "strip":True
    }
    )

documents = loader.load()

print("List of Document: ",len(documents))
document = documents[0]

# slice upto 500 words not whole content
print("Page Content: ",document.page_content[:500])
print("Metadata : ",document.metadata)