# Revisão do Projeto 7 - Aplicação integrada

## Domínio

O SQLite é a persistência, a API expõe recursos HTTP e o Streamlit oferece uma
interface para o usuário. A integração deve preservar responsabilidades claras
entre essas camadas.

## Exercícios

1. Fazer a interface consumir `GET /produtos` em vez de ler o banco diretamente.
2. Adicionar uma rota de filtro por categoria.
3. Criar um teste que cadastre e consulte um produto.

## Pergunta de domínio

Qual é a vantagem de trocar a interface sem precisar reescrever a regra de
persistência?

