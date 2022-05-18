import csv

class Item:
    discount = 0.9
    all = []
    laptop = []

    def __init__(self, name: str, price: int, quantity=0):
        assert price >= 0, f"Price {price} is not greater or equal than 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal than 0"

        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __add__(self, object):
        return self.price * self.quantity + object.price * object.quantity

    def get_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.discount

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        reader = csv.DictReader(open(csv_file))
        for i in list(reader):
            cls(
                i['name'],
                int(i['price']),
                int(i['quantity'])
            )

    @staticmethod
    def range_price(start, stop):
        for each_item in Item.all:
            if (stop >= each_item.price) and (each_item.price >= start) and (each_item.quantity > 0):
                print(each_item)

    @staticmethod
    def print_availabe_items():
        for each_item in Item.all:
            if (each_item.quantity > 0):
                print(each_item)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        assert len(new_name) < 10, 'The name is too long!'
        self.__name = new_name