from __future__ import annotations

import sqlite3
from contextlib import closing
from pathlib import Path


DB_PATH = Path(__file__).parent / "integrated.db"


def connect() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize() -> None:
    with closing(connect()) as connection, connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                produto TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco REAL NOT NULL CHECK (preco >= 0),
                quantidade_vendida INTEGER NOT NULL CHECK (quantidade_vendida >= 0)
            )
            """
        )


def all_products() -> list[dict]:
    with closing(connect()) as connection:
        rows = connection.execute("SELECT * FROM produtos ORDER BY produto").fetchall()
        return [dict(row) for row in rows]


def add_product(produto: str, categoria: str, preco: float, quantidade_vendida: int) -> None:
    with closing(connect()) as connection, connection:
        connection.execute(
            "INSERT INTO produtos (produto, categoria, preco, quantidade_vendida) VALUES (?, ?, ?, ?)",
            (produto, categoria, preco, quantidade_vendida),
        )

