# Derived Attributes in OOP
class Item:
    def __init__(self, item_id, name, price, quantity):
        self.__item_id = item_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def Amount(self):  # Derived Attributes
        return self.__price * self.__quantity

    @Amount.setter
    def Amount(self, amount):
        # Derived Attribute: Must be obtained by using one of the attributes
        # Recompute the base attribute so that
        # the amount reflects the new value
        # Here, self.__price is recomputed
        if self.__quantity == 0:
            raise ValueError("Price must be greater than 0 to set amount.")
        self.__price = amount / self.__quantity


def main():
    item = Item(123, "Coca Cola", 10000, 2)
    print(item.Amount)
    item.Amount = 50000
    print(item.Amount)


main()
