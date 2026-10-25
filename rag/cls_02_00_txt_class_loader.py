from langchain_community.document_loaders import TextLoader
from pathlib import Path

# magic method that print current module or python file name
# absolute file path
print(__file__)

print(Path(__file__).resolve().parent)

# base_dir = Path(__file__).resolve().parent

# file_path = base_dir / "student_rules.txt"

# from pathlib import Path

# base_dir = Path(__file__).resolve().parent

# file_path = base_dir / "student_rules.txt"
# print(file_path)