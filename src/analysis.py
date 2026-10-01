import pandas as pd


def summarize(data: pd.DataFrame) -> dict[str, float | int | str]:
    """Calcula indicadores principais da base."""
    if data.empty:
        return {
            "preco_medio": 0.0,
            "menor_preco": 0.0,
            "maior_preco": 0.0,
            "total_vendido": 0,
            "produto_mais_caro": "-",
            "categoria_mais_vendida": "-",
        }

    most_expensive = data.loc[data["preco"].idxmax(), "produto"]
    category_totals = sales_by_category(data)
    return {
        "preco_medio": float(data["preco"].mean()),
        "menor_preco": float(data["preco"].min()),
        "maior_preco": float(data["preco"].max()),
        "total_vendido": int(data["quantidade_vendida"].sum()),
        "produto_mais_caro": str(most_expensive),
        "categoria_mais_vendida": str(category_totals.iloc[0]["categoria"]),
    }


def sales_by_category(data: pd.DataFrame) -> pd.DataFrame:
    """Agrupa a quantidade vendida por categoria."""
    return (
        data.groupby("categoria", as_index=False)["quantidade_vendida"]
        .sum()
        .sort_values("quantidade_vendida", ascending=False)
    )
