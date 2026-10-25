from langchain_core.documents import Document

document1 = Document(
    page_content="Bring the ID, its compusory",
    metadata = {
        "source":"school_rule.txt",
        "department":"administration"
    })

document2 = Document(
    page_content="Commitment, focus and deep work.",
    metadata = {
        "source":"durga_sir_rule.txt",
        "department":"motivational"
    })
document3 = Document(
    page_content="I will become a business.",
    metadata = {
        "source":"business_rule.txt",
        "author":"malik"
    })

docs = [document1,document2,document3]
for index,document in enumerate(docs,start=1):
    print(f"=== Document: {index} ===")
    print(document.page_content) 

    print(document.metadata)

    print(document.metadata["source"])

    print(document.metadata.get("department","Unkown"))

    print(document.metadata.get("author","Not declared"))
    print()

