import pandas as pd 
from bs4 import BeautifulSoup
import requests

#Importamos grande parte das dependencias tecnologicas para o projeto



#pegamos a url que iremos fazer um request (no caso é o carrefour)

url = "https://mercado.carrefour.com.br/categoria/mercearia/guloseimas/chocolates-e-bombons"

#Pro carrefour entender que a gente na "teoria" a gente é um usuario, iremos dizer que somos um usuario que está utilizando o windows 10 com sistema operacional x64, com o chrome na versão 120.0.0.0, e diremos que ele é compativel tanto com o mobizilla quanto com o safari

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


#Aqui a gente faz a requisição para dos headers do html pra testar se está funcionando
resposta = requests.get(url, headers=headers)


#A gente vai verificar se o servidor respondeu pra gente e permitiu o acesso, por isso a gente está utilizando os status code, onde o principal onde foi aceito é a requisição 200. O HTML.parser basicamente identifica as tags html de um site inteiro. resposta.text porque quando você pega o headers, ele vem com vários dados como status code, tags, informações desnecessárias e etc... por isso utilizamos como .text porque assim ele só vai pegar as tags.
if resposta.status_code == 200:
        print("Conexão bem sucedida, o site liberou!")
        sopa = BeautifulSoup(resposta.text, 'html.parser')
        dados_extraidos = []

        #O bloco de produtos serve basicamente pra procurar o link da tag >a< e o find_all pra selecionar todos que possuem o >a< + os atributos como data-test: search-product-card

        bloco_de_produtos = sopa.find_all('a', attrs={'data-test': 'search-product-card'})

        for bloco in bloco_de_produtos:
        # Aqui a gente vai buscar o nome do elemento (no caso o nome do produto), ent a gente fala pra cada bloco que está dentro de bloco_de_produtos vai procurar pela tag H2 e vai dizer que a classe precisa estar em text-sm (texto pequeno), depois iremos dizer que ele vai tirar os espaços desnecessários + iremos dizer para caso o item exista, marcar como o nome dele e caso não exista marcar como 'sem nome'
                nome_elemento = sopa.find('h2', class_='text-sm')
                nome = nome_elemento.text.strip() if nome_elemento else 'Sem nome'

        # A gente vai aplicar a mesma coisa só que com o preço 
                preco_elemento = sopa.find('span', class_='text-price-default')
                preco = preco_elemento.text.strip() if preco_elemento else '0'

        #adicionaremos para a váriavel de dados extraidos 

                dados_extraidos.append({'Nome': nome, 'Preço': preco})

        #Transformaremos isso em uma tabela 
        
        df = pd.DataFrame(dados_extraidos)


        if not df.empty:
                df['Preço'] = df['Preço'].str.replace(r'R\$ ', '', regex=True).str.replace(',', '.').astype(float)     
                df.to_csv("Chocolates_Carrefour.csv", index=False)      
                print("A extração está pronta pra ser limpa")
                print(df.head())

        else:
                print("A extração falhou: Nenhum produto encontrado ou o site pode ter bloqueado o request.")

                with open("html_recebido.html", "w", encoding="utf-8") as arquivo:
                        arquivo.write(resposta.text)
       




        





else:
        print(f"Bloqueado! Código do erro: {resposta.status_code}")

