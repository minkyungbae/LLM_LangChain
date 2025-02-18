from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAI

load_dotenv()

llm = OpenAI()
chat_model = ChatOpenAI()

# input_text = "Hello, I'm Aiden."
input_text = "안녕하세요. 저는 에이든입니다."

# print(llm.invoke(input_text))
# print("---")


from langchain.schema import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="you are a helpful assistant"),
    HumanMessage(content=input_text),
]

print(chat_model.invoke(messages))