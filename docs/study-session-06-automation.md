# Sessão 6 - Automação de relatório

## Objetivo

Entender como transformar uma tarefa repetitiva em um processo determinístico,
validado e fácil de executar novamente.

## Fluxo

1. ler `products.csv`;
2. validar as colunas obrigatórias;
3. agrupar por categoria;
4. gravar CSV e JSON;
5. informar o caminho dos resultados.

## Exercício implementado

O relatório agora gera duas saídas e interrompe o processo com uma mensagem
clara quando a entrada não possui as colunas necessárias.

## Tente explicar

1. Qual é a diferença entre uma função pura e o processo completo de relatório?
2. Por que gerar CSV e JSON pode atender consumidores diferentes?
3. O que deve acontecer quando a fonte muda de formato?

## Exercício seguinte

Adicionar uma opção de linha de comando para escolher a pasta de saída sem
alterar o código-fonte.

