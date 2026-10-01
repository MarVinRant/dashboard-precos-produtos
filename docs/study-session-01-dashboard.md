# Sessão 1 - Entendendo o dashboard

## Objetivo

Ao terminar esta sessão, você deve conseguir explicar como os dados saem do
CSV, são limpos, transformados em indicadores e exibidos no Streamlit.

## Resumo guiado

O `data_loader.py` é responsável pela entrada e pela qualidade dos dados. O
`analysis.py` contém regras de negócio: calcular métricas e agrupar vendas. O
`app.py` coordena a interface, chama essas funções e desenha os gráficos.

Essa separação reduz o acoplamento: uma alteração na regra de cálculo não exige
reescrever toda a tela, e as regras podem ser testadas sem abrir o navegador.

## Tente responder sem consultar o código

1. Qual é a diferença entre `load_csv` e `clean_products`?
2. Por que `summarize` recebe um `DataFrame` em vez de ler o arquivo diretamente?
3. O que muda nos indicadores quando o usuário seleciona uma categoria?
4. Qual teste protege o comportamento quando não há registros?

## Exercício de mão na massa

Adicione ao dashboard uma métrica chamada `ticket_medio`, definida como:

```text
preço total dos produtos / quantidade de produtos
```

Regras:

- retornar `0.0` quando a base estiver vazia;
- criar um teste para a base com dois produtos;
- exibir a métrica na interface;
- executar a suíte completa depois da alteração.

O filtro por faixa de preço foi implementado como a atividade seguinte da
revisão, com validação para intervalos invertidos.

## Evidência da sessão

Registre abaixo, após concluir o exercício:

- Minha explicação do fluxo: ____________________________________________
- Teste criado: _______________________________________________________
- Resultado da suíte: _________________________________________________
- Dúvida que permaneceu: ______________________________________________

