# Guia de estudo e revisão dos projetos

Este guia deve ser usado antes de qualquer publicação. A regra é conseguir
explicar o projeto sem copiar a resposta do chat e fazer pelo menos uma
alteração funcional em cada código.

## 1. Dashboard de Preços e Produtos

### Explique

- como o CSV chega ao `DataFrame`;
- por que `summarize` e `sales_by_category` ficam separados da interface;
- como o filtro de categoria altera os indicadores;
- por que os testes verificam valores e não apenas se a tela abriu.

### Pratique

1. Adicione um filtro por faixa de preço.
2. Crie uma métrica para a categoria mais vendida.
3. Escreva um teste para uma base vazia.

## 2. Análise exploratória

### Explique

- diferença entre pergunta analítica e gráfico;
- como dados ausentes são identificados;
- por que as conclusões precisam ser baseadas nos números calculados;
- onde os resultados são salvos para permitir reprodução.

### Pratique

1. Adicione o desvio padrão do preço ao resumo.
2. Crie um gráfico de preço médio por categoria.
3. Escreva uma conclusão com dois números observados.

## 3. Estoque com SQLite e CRUD

### Explique

- o que significam Create, Read, Update e Delete;
- por que os comandos usam parâmetros em vez de concatenar strings;
- como as restrições `CHECK` protegem os dados;
- por que a conexão precisa ser fechada.

### Pratique

1. Adicione busca por nome.
2. Impeça o cadastro de produtos duplicados.
3. Crie um teste para preço negativo.

## 4. API de Produtos

### Explique

- diferença entre rota, schema e modelo de domínio;
- quando usar os status 200, 201 e 404;
- como o filtro por categoria funciona;
- como a documentação `/docs` é gerada.

### Pratique

1. Crie uma rota para excluir produto.
2. Adicione filtro por preço máximo.
3. Escreva um teste para produto inexistente.

## 5. Machine Learning

### Explique

- o que são feature e target;
- por que os dados são separados em treino e teste;
- o significado de MAE e R²;
- por que uma métrica ruim é um resultado importante, não um erro a esconder.

### Pratique

1. Compare o modelo com uma previsão pela média.
2. Adicione uma nova variável ao conjunto de features.
3. Explique por que a base pequena limita a conclusão.

## 6. Automação de relatório

### Explique

- quais são entrada, transformação e saída;
- por que a função `build_report` é testável isoladamente;
- como executar o relatório novamente sem editar o código.

### Pratique

1. Gere também um relatório JSON.
2. Inclua o produto mais vendido por categoria.
3. Valide se as colunas obrigatórias existem antes de processar.

## 7. Aplicação integrada

### Explique

- qual responsabilidade pertence ao Streamlit;
- qual responsabilidade pertence à API;
- por que o SQLite é uma camada separada;
- como a mesma fonte pode alimentar a interface e os endpoints.

### Pratique

1. Faça a interface consumir a API em vez de acessar o banco diretamente.
2. Adicione uma rota de filtro por categoria.
3. Crie um teste de integração para cadastro e consulta.

## 8. Projeto acadêmico final

Antes da entrega, responda sem consultar o código:

1. Qual problema a aplicação resolve?
2. Quais são os requisitos funcionais?
3. Como os dados percorrem o sistema?
4. Que testes comprovam o funcionamento?
5. Qual limitação ainda existe?
6. O que seria evoluído em uma próxima versão?

