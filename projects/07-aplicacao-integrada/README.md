# Projeto 7 - Aplicação integrada

Projeto de consolidação da trilha. A aplicação integrada reunirá o banco do
estoque, a API de produtos, a análise exploratória e uma interface Streamlit.

## Escopo planejado

- SQLite como fonte persistente;
- FastAPI para exposição dos dados;
- Streamlit para consumo e visualização;
- testes unitários e de integração;
- documentação de arquitetura;
- deploy público.

## Executar

Em um terminal, inicie a API:

```bash
uvicorn api:app --reload
```

Em outro terminal, inicie a interface:

```bash
streamlit run app.py
```

Os dois componentes usam o mesmo banco SQLite.

## Demonstração Streamlit

https://aplicacao-integrada-rantech.streamlit.app/

