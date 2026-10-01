# Sessão 3 - SQLite e CRUD

## Objetivo

Entender como uma aplicação Python persiste dados e protege regras básicas de
negócio antes de exibir o resultado na interface.

## Fluxo

1. `initialize` cria a tabela se ela ainda não existir.
2. `create_product` executa o `INSERT` com parâmetros.
3. `list_products` e `search_products` executam consultas `SELECT`.
4. `update_stock` e `update_price` executam `UPDATE`.
5. `delete_product` executa `DELETE`.
6. Cada operação fecha a conexão para não bloquear o arquivo no Windows.

## Exercício implementado

O projeto agora possui busca por nome, atualização de preço e rejeição de preço
negativo, com teste do ciclo cadastrar → consultar → atualizar → excluir.

## Tente explicar

1. Qual é a diferença entre DDL e DML?
2. Por que `?` é usado no SQL?
3. Por que a conexão precisa ser fechada mesmo após o `commit`?

## Exercício seguinte

Adicione uma coluna `estoque_minimo` e mostre um alerta quando o estoque atual
for menor ou igual ao limite.

