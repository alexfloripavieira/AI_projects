from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo")

prompt_template = PromptTemplate.from_template("Me fale sobre o carro {carro}.")

runnable_sequence = prompt_template | model | StrOutputParser()

response = runnable_sequence.invoke({"carro": "Haval H6 2025"})

print(response)


runnable_sequence = (
    PromptTemplate.from_template("Me fale sobre o carro {carro}.")
    | model
    | StrOutputParser()
)

response = runnable_sequence.invoke({"carro": "BYD Song Plus 2025"})

print(response)
