import pytest

from src.item import Item

@pytest.fixture
def position():
    return Item("Смартфон", 100, 1)


def test_item_init(position):
    assert position.name == "Смартфон"
    assert position.price == 100
    assert position.quantity == 1


def test_calculate_total_price(position):
    assert position.calculate_total_price() != 100


def test_apply_discount(position):
    position.apply_discount()
    Item.pay_rate = 0.8
    assert position.price == 80
