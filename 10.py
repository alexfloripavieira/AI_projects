from dotenv import load_dotenv
from langchain.agents import Tool
from langchain.prompts import PromptTemplate
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.utilities import PythonREPL
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI(model="gpt-3.5-turbo")

python_repl = PythonREPL()
python_repl_tool = Tool(
    name="Python REPL",
    description="Um shell Python. Use isso para executar código Python. Execute apenas códigos Python válidos."
    'Se você precisar obter o retorno do código, use a função "print(...)".',
    func=python_repl.run,
)

agent_executor = create_python_agent(
    llm=model,
    tool=python_repl_tool,
    verbose=True,
)

prompt_template = PromptTemplate(
    input_variables=["query"],
    template="""
    Resolva o problema: {query}.
    """,
)

query = r"quanto é 20% de 3000"
prompt = prompt_template.format(query=query)

response = agent_executor.invoke(prompt)
print(response.get("output"))
