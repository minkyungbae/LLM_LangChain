from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

# 좀 더 상세하게 알려줌
class Movie(BaseModel):
    title: str = Field(description="The title of the movie")
    year: int = Field(description="The year the movie was released")
    rating: float = Field(description="The rating of the movie")

# 자르는 애도 있네??
parser = PydanticOutputParser(pydantic_object=Movie)
# print(parser.get_format_instructions()) # instruction : 지시 사항

temperature = 0.0 # 똑같은 input을 넣었을 때, 생성해내는 랜덤성을 설정 (0.0 : 창의성이 낮음)
model_name = "gpt-4o-mini" # LLM 갖고 왔어용
llm = ChatOpenAI(temperature=temperature, model_name=model_name)

#프롬프트
prompt = PromptTemplate.from_template(
    template="{subject}에 대한 영화를 랜덤으로 생성해줘.\n{format_instructions}",
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
# partial_variables : 바뀌지 않을 변수값

chain = prompt | llm | parser # chain으로 연결

movie = chain.invoke({"subject": "코딩"})
print(movie)
print(type(movie))
print(movie.title)
print(movie.year)
print(movie.rating)
