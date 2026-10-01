from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).parent
DATA_PATH = PROJECT_DIR / "../../data/products.csv"
OUTPUT_PATH = PROJECT_DIR / "outputs" / "relatorio_categorias.csv"
JSON_OUTPUT_PATH = PROJECT_DIR / "outputs" / "relatorio_categorias.json"
REQUIRED_COLUMNS = {"produto", "categoria", "preco", "quantidade_vendida"}


def validate_data(data: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS.difference(data.columns)
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {sorted(missing)}")


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
    validate_data(data)
    report = build_report(data)
    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    report.to_csv(OUTPUT_PATH, index=False)
    JSON_OUTPUT_PATH.write_text(
        json.dumps(report.to_dict(orient="records"), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Relatório criado em: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

