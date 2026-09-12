# 🍫 Análise de Chocolates do Carrefour

## 📌 Sobre o projeto

Este projeto tem como objetivo analisar as marcas de chocolate disponíveis no Carrefour, buscando entender quais marcas possuem maior quantidade de produtos e, consequentemente, quais apresentam mais oportunidades de mercado.

A ideia também é analisar a diferença de preços entre os produtos e marcas, permitindo identificar padrões e diferenças dentro do catálogo de chocolates.

Ao final do projeto, a intenção é utilizar os dados coletados para construir um dashboard com as principais informações e análises.

---

## 🎯 Objetivos

- Extrair dados de produtos de chocolate do Carrefour;
- Identificar o nome e o preço dos produtos;
- Organizar os dados coletados em tabelas;
- Analisar a quantidade de produtos por marca;
- Comparar os preços entre diferentes marcas;
- Identificar possíveis oportunidades de mercado;
- Criar um dashboard para visualização dos dados.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **Requests**
- **BeautifulSoup**
- **Pandas**
- **venv**

### Tecnologias que poderão ser utilizadas futuramente

- **Selenium**
- **Playwright**
- Ferramentas de visualização de dados

---

## 🔎 Processo de extração

Inicialmente, a ideia era realizar a extração dos dados utilizando o `Requests`, simulando um usuário através dos `headers`.

O primeiro passo foi estabelecer uma conexão com a `URL` do Carrefour e verificar o `status code` retornado pelo site.

Após isso, utilizei o `BeautifulSoup` com `html.parser` para analisar o HTML retornado e localizar os elementos que continham as informações dos produtos.

Utilizando o DevTools do navegador, foi possível identificar o bloco principal dos produtos e localizar elementos como:

- Nome do produto;
- Preço;
- Tags HTML;
- Classes;
- Atributos, como `data-test`.

A partir dessas informações, utilizei um `for` para percorrer os blocos de produtos e extrair os dados necessários.

Depois da extração, os dados seriam enviados para o **Pandas**, onde poderiam ser organizados e posteriormente analisados.

---

## ⚠️ Problema encontrado

Durante o desenvolvimento, os dados não estavam sendo retornados corretamente.

Inicialmente, verifiquei se o problema estava na organização dos dados e criei uma etapa para verificar se a tabela estava sendo preenchida.

Também criei um arquivo com a resposta recebida pelo site para investigar o problema.

Após analisar o retorno, descobri que o Carrefour estava identificando as requisições realizadas pelo `Requests` como uma requisição automatizada, bloqueando o acesso.

Também tentei acessar a `API` do Carrefour, porém, após diversas requisições utilizando o meu IP, o acesso acabou sendo bloqueado.

---

## 🧠 Próximo passo

Para continuar o projeto, a ideia seria deixar de apenas simular um usuário através do `Requests` e utilizar uma ferramenta de automação de navegador, como **Selenium** ou **Playwright**.

Essas tecnologias permitem automatizar um navegador e trabalhar com páginas que dependem de um navegador real para carregar ou disponibilizar determinados elementos.

Porém, como ainda não possuo conhecimento sobre essas tecnologias, será necessário estudá-las antes de continuar essa etapa do projeto.

Por enquanto, o projeto não será abandonado, mas também não será minha prioridade atual.

---

## 📊 Resultado esperado

O resultado final esperado é uma análise dos chocolates disponíveis no Carrefour, contendo informações como:

- Marcas disponíveis;
- Quantidade de produtos por marca;
- Preços dos produtos;
- Comparação de preços;
- Diferenças entre marcas;
- Possíveis oportunidades de mercado.

Essas informações serão utilizadas posteriormente para a criação de um **dashboard de análise de chocolates do Carrefour**.

---

## 📚 O que estou aprendendo com este projeto

Este projeto está sendo desenvolvido como uma forma prática de aprender sobre:

- Web Scraping;
- Requisições HTTP;
- HTML e estrutura de páginas;
- BeautifulSoup;
- Manipulação de dados com Pandas;
- Tratamento e limpeza de dados;
- Automação de navegadores;
- Limitações e bloqueios durante processos de extração de dados;
- Análise e visualização de dados.

Além de desenvolver o projeto, o objetivo é entender **o processo completo de transformar dados encontrados na web em informações que possam ser analisadas e utilizadas para tomada de decisão**.

---

## 🚧 Status do projeto

**Em desenvolvimento / Temporariamente pausado**

A primeira tentativa de extração utilizando `Requests` e `BeautifulSoup` encontrou limitações devido ao bloqueio das requisições automatizadas.

O projeto poderá ser retomado após o estudo de ferramentas como **Selenium** ou **Playwright**.
