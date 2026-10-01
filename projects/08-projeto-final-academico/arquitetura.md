# Arquitetura

```text
Usuário
   |
Streamlit (interface e indicadores)
   |
FastAPI (rotas e validação)
   |
SQLite (persistência)
   |
Relatórios e análises Pandas/NumPy
```

O dashboard piloto e os projetos intermediários permanecem independentes para
facilitar estudo e testes. A aplicação integrada demonstra a comunicação entre
as camadas e utiliza o mesmo banco para a interface e a API.

