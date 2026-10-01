import pandas as pd

from report import build_report


def test_report_groups_by_category():
    data = pd.DataFrame(
        {
            "produto": ["A", "B"],
            "categoria": ["Casa", "Casa"],
            "preco": [10.0, 20.0],
            "quantidade_vendida": [2, 3],
        }
    )
    result = build_report(data)
    assert result.iloc[0]["categoria"] == "Casa"
    assert result.iloc[0]["produtos"] == 2
    assert result.iloc[0]["itens_vendidos"] == 5

