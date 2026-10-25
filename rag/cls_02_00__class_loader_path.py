from pathlib import Path

# magic method that print current module or python file name
# absolute file path
print(__file__)
# root path till parent of current file
print(Path(__file__).resolve().parent)

