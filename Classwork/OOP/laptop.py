from item import Item

class Laptop(Item):    
    def __init__(self, name: str, price: int, quantity=0, numpad=False):
        super().__init__(name, price, quantity)

        assert isinstance(numpad, bool), 'dsadsa'
        self.numpad = numpad
        Laptop.laptop.append(self)