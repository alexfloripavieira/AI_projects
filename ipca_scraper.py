import sqlite3

import requests
from bs4 import BeautifulSoup

url = "https://www.idealsoftwares.com.br/indices/ipca_ibge.html"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
html_content = response.content

with open("pagina.html", "wb") as f:
    f.write(html_content)

soup = BeautifulSoup(html_content, "html.parser")

tables = soup.find_all("table")
print(f"Quantidade de tabelas encontradas: {len(tables)}")
if len(tables) == 0:
    raise Exception("Nenhuma tabela encontrada na página.")
table = tables[0]  # ou ajuste o índice conforme necessário

ipca_data = []
for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    if cols:
        month_year = cols[0].text.strip()
        value = (
            cols[1].text.strip().replace(",", ".").replace(" ", "").replace("\n", "")
        )
        if value:
            # Adicione este print para depuração
            print(f"month_year encontrado: '{month_year}'")
            partes = month_year.split("/")
            if len(partes) == 2:
                month, year = partes
                ipca_data.append((float(value), month, int(year)))
            else:
                print(f"Ignorando linha inesperada: '{month_year}'")


conn = sqlite3.connect("ipca.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS IPCA (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value REAL,
    month TEXT,
    year INTEGER,
    UNIQUE(month, year)
)
""")

for data in ipca_data:
    value, month, year = data
    cursor.execute(
        """
    INSERT OR IGNORE INTO IPCA (value, month, year)
    VALUES (?, ?, ?)
    """,
        (value, month, year),
    )

conn.commit()
conn.close()

print("Dados históricos do IPCA salvos com sucesso!")
for idx, t in enumerate(tables):
    print(f"Tabela {idx}: classes = {t.get('class')}")
