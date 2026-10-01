import pandas as pd

from model import train_model


def test_train_model_returns_metrics():
    data = pd.DataFrame(
        {
            "produto": ["A", "B", "C", "D", "E", "F", "G", "H"],
            "categoria": ["Casa", "Casa", "Casa", "Casa", "Casa", "Casa", "Casa", "Casa"],
            "preco": [10, 20, 30, 40, 50, 60, 70, 80],
            "quantidade_vendida": [80, 70, 60, 50, 40, 30, 20, 10],
        }
    )
    coefficients, metrics = train_model(data)
    assert len(coefficients) == 3
    assert set(metrics) == {"mae", "baseline_mae", "r2"}

