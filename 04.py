from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo")

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content="Você deve responder baseado em dados geográficos de regiões do Brasil."
        ),
        HumanMessagePromptTemplate.from_template(
            "Por favor, me fale sobre a região {regiao}."
        ),
        AIMessage(
            content="Claro, vou começar coletando informações sobre a região e analisando os dados disponíveis."
        ),
        HumanMessage(content="Certifique-se de incluir dados demográficos."),
        AIMessage(content="Entendido. Aqui estão os dados:"),
    ]
)

prompt = chat_template.format_messages(regiao="Sul")

response = model.invoke(prompt)

print(response.content)
