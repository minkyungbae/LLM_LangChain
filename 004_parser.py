# 자르기
from langchain.schema import BaseOutputParser


class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text: str) -> list:
        return text.strip().split(",") # strip : 양쪽 공백 제거


parser = CommaSeparatedListOutputParser()

print(parser.invoke("a, b, c"))
