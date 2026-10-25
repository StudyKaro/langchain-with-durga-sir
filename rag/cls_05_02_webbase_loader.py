from langchain_community.document_loaders import WebBaseLoader
loader= WebBaseLoader(
    web_path="https://reference.langchain.com/python/langchain-community/document_loaders/web_base/WebBaseLoader",
    bs_get_text_kwargs={
        "separator":" ", 
        "strip":True
    },
    raise_for_status=True, # enable exception 
    header_template={
        "User-Agent": "LangChainDay4EducationalDemo/1.0"
    },
    requests_kwargs={
    "timeout": 15 # wait for max 15 seconds
    }
    )

print(loader.bs_get_text_kwargs)
print(loader.bs_kwargs)
try:
    documents = loader.load()

    # print("List of Document: ",len(documents))
    # document = documents[0]

    # # slice upto 500 words not whole content
    # print("Page Content: ",document.page_content[:500])
    # print("Metadata : ",document.metadata)
except Exception as e:
    print("Webpage loading error.")
    print("Error type: ", type(e).__name__)
    print("Error: ",e)