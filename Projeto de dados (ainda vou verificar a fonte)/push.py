#Nessa primeira parte a gente vai basicamente requisitar as tecnologias que iremos utilizar, que no caso seria o pandas para analisar os dados, o request pra requisitar a entrada do site e o bs4 (beautifulsoup) para extrair os dados.

import pandas as pd 
import requests 
from bs4 import BeautifulSoup

# Aqui a gente vai dizer qual url a váriavel vai guardar que no caso é o ceagesp pois esse site é oficial e fala sobre a cotação de frutas e outras coisas, a escolha do ceagesp foi porque o site aceita a extração do beautifulsoup sem questionar se é um bot ou não.

url = "https://ceagesp.gov.br/cotacoes/"


#A parte de sessão é uma parte "nova" justamente porque eu enfrentei um problema onde os dados que eu estava recebendo estavam retornando como "none". ou seja, o site estava negando de alguma forma, ou eu estava extraindo de maneira "incorreta". Para resolver essa situação eu parti do principio que o site funcionava com COOKIES e os headers de usuários então eu simulei uma sessão de cookies utilizando o request.Session()
sessao = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

sessao.get(url, headers=headers)

filtros_busca = {
    "cot_grupo": "FRUTAS",
    "cot_data": "11/09/2026"
}

resposta = sessao.post(url, data=filtros_busca, headers=headers)

soup = BeautifulSoup(resposta.text, 'html.parser')

tabela = soup.find('table', class_="contacao_lista")

print(tabela)

dados_extraidos = []

linhas = tabela.find_all('tr')

for linha in linhas:
    colunas = linha.find_all('td')

    if len(colunas) > 5:
        produtos = colunas[0].text.strip()
        classificacao = colunas[1].text.strip()
        unidade = colunas[2].text.strip()
        preco_menor = colunas[3].text.strip()
        preco_comum = colunas[4].text.strip()
        preco_maior = colunas[5].text.strip()

        dados_extraidos.append([produtos, classificacao, unidade, preco_menor, preco_comum, preco_maior])

df_bronze = pd.DataFrame(dados_extraidos, columns=['produtos', 'classificacao', 'unidade', 'preco_menor', 'preco_comum', 'preco_maior'])


print(df_bronze.head(10))


print("Salve rapaziada, n vou perder aa droga da sequencia")

