# Revisão guiada - Dashboard de Preços e Produtos

## O fluxo da aplicação

1. `app.py` define a interface e localiza o arquivo CSV.
2. `load_csv` lê a fonte e verifica as colunas obrigatórias.
3. `clean_products` converte números e datas e remove registros essenciais inválidos.
4. `summarize` calcula os indicadores exibidos nos cartões.
5. `sales_by_category` prepara os dados do gráfico de vendas.
6. Plotly transforma os resultados em gráficos interativos.

## Perguntas de revisão

1. O que aconteceria se `preco` viesse como texto?
2. Por que a limpeza fica em `data_loader.py` e não dentro do `app.py`?
3. Por que o filtro precisa acontecer antes de `summarize`?
4. O que o teste de base vazia protege?
5. Qual é a diferença entre uma métrica e uma visualização?

## Exercícios práticos

1. ~~Adicione uma métrica chamada `categoria_mais_vendida`.~~ Implementado na revisão atual.
2. Crie um filtro por preço mínimo e máximo.
3. Adicione uma tabela com os três produtos mais vendidos.
4. Faça o dashboard mostrar uma mensagem amigável quando o filtro não encontrar linhas.
5. Escreva um teste para garantir que uma coluna obrigatória ausente gera `ValueError`.

## Critério para considerar estudado

Você deve conseguir explicar o fluxo acima, implementar pelo menos dois exercícios
sem copiar a solução e interpretar os números exibidos na aplicação.
