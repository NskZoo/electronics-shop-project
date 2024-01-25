import pytest

from src.item import Item

@pytest.fixture
def position():
    return Item("Смартфон", 100, 1)


def test_item_init(position):
    assert position.name == "Смартфон"
    assert position.price == 100
    assert position.quantity == 1



def test_calculate_total_price():
    item = Item('Смартфон', 20_000, 100)
    assert item.calculate_total_price() == 2_000_000

def test_apply_discount():
    item = Item('Смартфон', 1, 300)
    Item.pay_rate = 0.1

    item.apply_discount()

    assert item.price != 270
