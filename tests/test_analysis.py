import pandas as pd

from src.analysis import sales_by_category, summarize


def sample_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "produto": ["A", "B"],
            "categoria": ["Casa", "Casa"],
            "preco": [10.0, 20.0],
            "quantidade_vendida": [2, 3],
            "data_coleta": pd.to_datetime(["2026-09-01", "2026-09-01"]),
        }
    )


def test_summarize_returns_expected_metrics():
    result = summarize(sample_data())
    assert result["preco_medio"] == 15.0
    assert result["menor_preco"] == 10.0
    assert result["maior_preco"] == 20.0
    assert result["total_vendido"] == 5
    assert result["produto_mais_caro"] == "B"


def test_sales_by_category_groups_sales():
    result = sales_by_category(sample_data())
    assert result.iloc[0]["categoria"] == "Casa"
    assert result.iloc[0]["quantidade_vendida"] == 5
