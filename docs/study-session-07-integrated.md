# Sessão 7 - Aplicação integrada

## Objetivo

Entender como camadas diferentes colaboram sem concentrar todas as
responsabilidades em um único arquivo.

## Camadas

- `integrated_db.py`: persistência e consultas SQLite;
- `api.py`: contrato HTTP, validação e filtros;
- `app.py`: interface e interação com o usuário.

## Exercício implementado

A API integrada agora aceita `GET /produtos?categoria=...`, mantendo o filtro
fora da interface e testando o resultado vazio para uma categoria inexistente.

## Tente explicar

1. O que muda se o banco for trocado por PostgreSQL?
2. Por que a interface não deveria montar SQL diretamente?
3. Qual camada deveria validar o formato de uma requisição HTTP?

## Exercício seguinte

Fazer o Streamlit consumir a API HTTP, em vez de acessar `integrated_db.py`
diretamente, e criar um teste de integração para cadastro e consulta.

