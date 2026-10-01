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
