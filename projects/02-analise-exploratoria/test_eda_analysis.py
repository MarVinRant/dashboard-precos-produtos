import pandas as pd

from analysis import build_summary


def test_build_summary_returns_expected_indicators():
    data = pd.DataFrame(
        {
            "produto": ["A", "B"],
            "categoria": ["Casa", "Casa"],
            "preco": [10.0, 20.0],
            "quantidade_vendida": [2, 3],
        }
    )
    result = build_summary(data)
    assert result["linhas"] == 2
    assert result["preco_medio"] == 15.0
    assert result["preco_mediano"] == 15.0
    assert result["desvio_preco"] == 5.0
    assert result["produto_mais_caro"] == "B"
    assert result["total_vendido"] == 5

