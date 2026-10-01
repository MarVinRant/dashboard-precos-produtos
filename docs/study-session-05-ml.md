# Sessão 5 - Machine Learning

## Objetivo

Entender o fluxo mínimo de um modelo supervisionado e aprender a avaliar se ele
realmente melhora uma previsão simples.

## Fluxo

1. selecionar features (`preco` e `categoria`);
2. definir o target (`quantidade_vendida`);
3. separar treino e teste;
4. codificar categorias e ajustar os coeficientes;
5. comparar o modelo com a previsão pela média;
6. salvar MAE, MAE baseline e R².

## Exercício implementado

O projeto agora calcula `baseline_mae`. O modelo deve ser comparado com esse
valor, em vez de ser considerado bom apenas por produzir uma previsão.

## Tente explicar

1. O que o MAE mede?
2. Por que o baseline é importante?
3. O que significa um R² negativo?
4. Por que oito registros não sustentam uma decisão comercial definitiva?

## Exercício seguinte

Adicionar uma feature de faixa de preço e verificar se o MAE melhora sem usar
informações que só estariam disponíveis depois da venda.

