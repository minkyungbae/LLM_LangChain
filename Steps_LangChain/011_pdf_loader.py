from langchain_community.document_loaders import PyPDFLoader

file_path = "data/ground_rule.pdf"
loader = PyPDFLoader(file_path)

documents = loader.load()
contents = loader.load_and_split()  # 각 줄을 분리
# print(documents)
print(contents)
