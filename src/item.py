import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return f"{self.__name}"

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
            print(f'Корректное название - {value}')
        else:
            self.__name = value[:10]
            print(f'Длинное слово - {value[:10]}')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        all_price = self.quantity * self.price
        return all_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price - self.price * self.pay_rate

    @name.setter
    def name(self, value):
        self._name = value

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        path = os.path.join(os.path.dirname(__file__), 'items.csv')
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                print(cls(name=item.get('name'),
                          price=item.get('price'),
                          quantity=item.get('quantity')))

    @staticmethod
    def string_to_number(number):
        return int(float(number))

