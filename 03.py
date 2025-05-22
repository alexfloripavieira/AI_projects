from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo")

template = """
Traduza o texto do {idioma1} para o {idioma2}:
{texto}
"""

prompt_template = PromptTemplate.from_template(template=template)

prompt = prompt_template.format(
    idioma1="português",
    idioma2="francês",
    texto="Bom dia!",
)

response = model.invoke(prompt)
separator = "#" * 20
print(response)
print(f"{separator}")
print(response.content)
