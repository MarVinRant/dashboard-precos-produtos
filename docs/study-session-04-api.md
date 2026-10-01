# Sessão 4 - API REST

## Objetivo

Entender como uma aplicação expõe dados por HTTP, valida entradas e comunica
resultados usando códigos de status.

## Rotas estudadas

- `GET /health`: verifica disponibilidade;
- `GET /produtos`: lista e filtra por categoria;
- `GET /produtos/filtro/preco`: filtra por preço máximo;
- `GET /produtos/{id}`: consulta um produto;
- `POST /produtos`: cria um produto e retorna `201`;
- `DELETE /produtos/{id}`: remove um produto e retorna `204`.

## Exercício implementado

O projeto agora possui exclusão, filtro por preço máximo e tratamento de produto
inexistente com `404`.

## Tente explicar

1. Por que `POST` retorna `201`?
2. Qual é a diferença entre erro de validação e recurso inexistente?
3. Por que os schemas não devem aceitar preço negativo?

## Exercício seguinte

Persistir os produtos em SQLite sem alterar o contrato das rotas.

