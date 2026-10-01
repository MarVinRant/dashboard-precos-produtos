from api import health, products


def test_integrated_api_health():
    assert health() == {"status": "ok"}


def test_integrated_api_returns_list():
    assert isinstance(products(), list)


def test_integrated_api_filters_category():
    result = products("categoria inexistente")
    assert result == []

