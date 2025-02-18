# import comma separated list output parser
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()

prompt = PromptTemplate.from_template(
    template="나에게 {subject}에 대한 유머를 말해줘.\n{format_instructions}",
    partial_variables={"format_instructions": format_instructions},
)

llm = ChatOpenAI()

chain = prompt | llm | output_parser

print(chain.invoke({"subject": "고양이"}))
