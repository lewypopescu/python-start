print(__name__)


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        if item in self.items:
            print(f"{item} is already in the cart.")
        else:
            self.items.append(item)
            print(f"{item} has been added to the cart.")
        return self.items

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} has been removed from the cart.")
        else:
            print(f"{item} is not in the cart.")
        return self.items
