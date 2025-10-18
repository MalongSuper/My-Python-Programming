# Class Product

class Product:
    __productList = []  # Initial List
    __amountList = []

    def __init__(self, name="", price=0.0, quantity=0):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__amountList.append(self.getAmount)
        self.__productList.append([name, quantity, price])

    @property
    def getAmount(self):
        return self.__price * self.__quantity

    @classmethod
    def totalAmount(cls):
        return sum(cls.__amountList)

    @classmethod
    def output(cls):
        print("+-------------------------------------------------------------+")
        print("| {:<15} | {:>5} | {:>15} | {:>15} |".format("ITEM", "QNT", "PRICE", "AMOUNT"))
        print("+-------------------------------------------------------------+")
        for i in range(len(cls.__productList)):
            print("| {:<15} | {:>5} | {:>15} | {:>15} |".format(cls.__productList[i][0],
                                                                cls.__productList[i][1], cls.__productList[i][2],
                                                                cls.__amountList[i]))
        print("+-------------------------------------------------------------+")
        print("{:<45} {:<35}".format(" TOTAL AMOUNT:\t\t\t", cls.totalAmount()))


def main():
    Product("LIPTON", 25000.0, 1)
    Product("ICE TEA", 5000.0, 12)
    Product("CAFE CAPPUCCINO", 20000.0, 1)
    Product("CAFE ESPRESSO", 25000.0, 2)
    Product("ORANGE JUICE", 30000.0, 1)
    Product.output()


main()
