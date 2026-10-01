from __future__ import annotations

from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).parent
DATA_PATH = PROJECT_DIR / "../../data/products.csv"
OUTPUT_PATH = PROJECT_DIR / "outputs" / "relatorio_categorias.csv"


def build_report(data: pd.DataFrame) -> pd.DataFrame:
    """Resume vendas e preços por categoria."""
    return (
        data.groupby("categoria", as_index=False)
        .agg(
            produtos=("produto", "count"),
            preco_medio=("preco", "mean"),
            itens_vendidos=("quantidade_vendida", "sum"),
        )
        .sort_values("itens_vendidos", ascending=False)
    )


def main() -> None:
    data = pd.read_csv(DATA_PATH)
    report = build_report(data)
    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    report.to_csv(OUTPUT_PATH, index=False)
    print(f"Relatório criado em: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

