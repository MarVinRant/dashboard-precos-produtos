# Revisão do Projeto 4 - API de Produtos

## Domínio

Os modelos Pydantic definem o formato dos dados, as rotas expressam os recursos
HTTP e as funções de domínio executam a consulta. O FastAPI usa esses modelos
para validar entradas e gerar `/docs`.

## Exercícios

1. Implementar `DELETE /produtos/{product_id}`.
2. Retornar `404` para um produto ausente.
3. Adicionar filtro por preço máximo.

## Pergunta de domínio

Quando uma API deve responder com `201` em vez de `200`?

