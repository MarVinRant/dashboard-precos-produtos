import db
from pathlib import Path


def test_product_crud_lifecycle(monkeypatch):
    test_db = Path(__file__).parent / ".test_estoque.db"
    monkeypatch.setattr(db, "DB_PATH", test_db)
    try:
        db.initialize()
        db.create_product("Produto teste", "Casa", 10.0, 4)
        products = db.list_products()
        assert len(products) == 1
        product_id = products[0]["id"]
        db.update_stock(product_id, 8)
        assert db.list_products()[0]["estoque"] == 8
        db.delete_product(product_id)
        assert db.list_products() == []
    finally:
        if test_db.exists():
            test_db.unlink()

