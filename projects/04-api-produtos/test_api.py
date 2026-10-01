from main import get_product, health, list_products


def test_health_endpoint_function():
    assert health() == {"status": "ok"}


def test_list_products_can_filter_by_category():
    result = list_products("informática")
    assert result
    assert all(item.categoria == "Informática" for item in result)


def test_get_product_returns_known_product():
    assert get_product(1).produto == "Notebook Pro"

