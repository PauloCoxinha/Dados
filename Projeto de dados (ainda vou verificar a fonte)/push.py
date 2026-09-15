import pandas as pd 
import requests 
from bs4 import BeautifulSoup


url = "https://ceagesp.gov.br/cotacoes/"

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