# Revisão do Projeto 3 - Estoque CRUD

## Domínio

O módulo `db.py` concentra conexão, criação da tabela e operações CRUD. A
interface Streamlit coleta entradas e chama funções de persistência, sem montar
SQL diretamente na tela.

## Exercícios

1. Adicionar atualização de preço.
2. Criar uma busca por nome.
3. Testar uma tentativa de preço negativo.

## Pergunta de domínio

Por que uma consulta parametrizada é mais segura que concatenar o texto digitado
pelo usuário em uma string SQL?

