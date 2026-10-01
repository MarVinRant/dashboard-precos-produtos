# Dashboard de Preços e Produtos

Projeto de estudo para praticar Python, Pandas, análise de dados e visualização.

## Objetivo

Carregar dados de produtos, limpar os registros, calcular indicadores e exibir uma visão simples dos preços e vendas.

## Funcionalidades do MVP

- carregar dados locais em CSV;
- importar tabelas HTML com `pandas.read_html`;
- calcular preço médio, maior preço, menor preço e total vendido;
- filtrar por categoria;
- exibir tabela e gráficos em Streamlit.

## Como executar

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Indicadores disponíveis

- preço médio dos produtos;
- menor e maior preço;
- total de itens vendidos;
- categoria com maior volume vendido;
- preços agrupados por produto;
- vendas agrupadas por categoria.

## Aprendizados do piloto

Este projeto foi construído para praticar o fluxo básico de análise de dados: carregar, validar, limpar, resumir e visualizar informações. A primeira versão usa uma base CSV local para manter a execução reproduzível e deixa preparada a importação de tabelas HTML.

## Estrutura

```text
app.py
data/products.csv
src/analysis.py
src/data_loader.py
tests/test_analysis.py
```

## Próximos passos

1. adicionar importação de uma fonte externa real;
2. incluir filtros por faixa de preço;
3. registrar histórico de coletas;
4. criar testes de integração;
5. publicar uma demonstração e um post técnico no LinkedIn.

## Trilha de projetos

Os projetos complementares da disciplina estão em [`projects/`](projects/):

- análise exploratória de dados;
- sistema de estoque com SQLite e CRUD;
- API de produtos com FastAPI;
- previsão de vendas com Machine Learning em NumPy;
- automação de relatórios;
- aplicação integrada com SQLite, FastAPI e Streamlit;
- documentação do projeto acadêmico final.

O roteiro de estudo está em [`docs/study-review.md`](docs/study-review.md) e o
checklist de publicação está em [`docs/publication-checklist.md`](docs/publication-checklist.md).

O dashboard piloto está disponível em:
https://dashboard-precos-rantech.streamlit.app/

## Demonstrações publicadas

- Dashboard piloto: https://dashboard-precos-rantech.streamlit.app/
- Sistema de estoque CRUD: https://dashboard-precos-apputos-lramqypvzf2nskkwh5cbqq.streamlit.app/
- Aplicação integrada: https://aplicacao-integrada-rantech.streamlit.app/

As aplicações Streamlit são executadas pelo Streamlit Community Cloud a partir
deste repositório. A API FastAPI do projeto 4 permanece disponível para execução
local e para um próximo deploy em um serviço de API dedicado.
