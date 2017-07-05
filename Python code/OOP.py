class ShoppingCart(object):
    def __init__(self):
        self.total = 0
        self.items = {}


def add_item(self, item_name, quantity, price):
    self.total += price * quantity
    self.items.update({item_name: quantity})


def remove_item(self, item_name, quantity, price):
    if item_name in self.items:
        if quantity < self.items[item_name] and quantity > 0:
            self.items[item_name] -= quantity
            self.total -= price * quantity

elif quantity >= self.items[item_name]:
self.total -= price * self.items[item_name]
del self.items[item_name]


def checkout(self, cash_paid):
    if cash_paid >= self.total:
        return cash_paid - self.total


return "Cash paid not enough"


class Shop(ShoppingCart):
    def __init__(self):
        self.quantity = 100


def remove_item(self):
    self.quantity -= 1