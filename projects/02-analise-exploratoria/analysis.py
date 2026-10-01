from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).parent
DATA_PATH = PROJECT_DIR / "../../data/products.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"
FIGURES_DIR = OUTPUT_DIR / "figures"


def load_data() -> pd.DataFrame:
    """Carrega e valida a base de produtos."""
    data = pd.read_csv(DATA_PATH)
    required = {"produto", "categoria", "preco", "quantidade_vendida"}
    missing = required.difference(data.columns)
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {sorted(missing)}")
    return data


def build_summary(data: pd.DataFrame) -> dict:
    """Calcula indicadores usados no relatório exploratório."""
    by_category = (
        data.groupby("categoria", as_index=False)["quantidade_vendida"]
        .sum()
        .sort_values("quantidade_vendida", ascending=False)
    )
    return {
        "linhas": int(len(data)),
        "categorias": int(data["categoria"].nunique()),
        "preco_medio": round(float(data["preco"].mean()), 2),
        "produto_mais_caro": str(data.loc[data["preco"].idxmax(), "produto"]),
        "categoria_mais_vendida": str(by_category.iloc[0]["categoria"]),
        "total_vendido": int(data["quantidade_vendida"].sum()),
        "valores_ausentes": int(data.isna().sum().sum()),
    }


def create_figures(data: pd.DataFrame) -> None:
    import matplotlib.pyplot as plt

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    by_category = data.groupby("categoria", as_index=False)["quantidade_vendida"].sum()
    by_category.plot.bar(x="categoria", y="quantidade_vendida", legend=False)
    plt.title("Itens vendidos por categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Quantidade vendida")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "vendas_por_categoria.png", dpi=160)
    plt.close()


def main() -> None:
    data = load_data()
    summary = build_summary(data)
    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    create_figures(data)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

