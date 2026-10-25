from pathlib import Path
from langchain_core.documents import Document


try:
    file_path = (Path(__file__).resolve().parent/"own_rule.txt")
    file_path.write_text("""
                         \n 1. Save 100 rupee every day.
                         \n 2. Learn a sutra form tatwarth sutra.
                         \n 3. Learn 5 minutes Durga sir.
                         \n 4. Read book.""",
                         encoding="utf-8")
    document = Document(
        page_content=file_path.read_text(encoding="utf-8"),
        metadata = {
            "source":str(file_path) # ile_path.name to get only file name
        }
        ) # convert file text into the page_content
    print(document.page_content)
    print(document.metadata.get("source","Not available"))
except Exception as e:
    print("Error message:",e)
    
#=====================================
# But this approach not at all recommonded 
# 1. No scalability -> Every one can write its own way.
# 2. Loader is missing that was the part of RAG
# 3. So use BaseLoader
#======================================