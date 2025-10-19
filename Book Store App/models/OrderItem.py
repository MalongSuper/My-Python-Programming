# Class OrderItem
from models.Book import Book


class OrderItem:
    def __init__(self, book: Book, quantity: int):
        self.__book = book
        self.__quantity = quantity

    def total_price(self) -> float:
        return self.book.price * self.__quantity

    @property
    def book(self) -> Book:
        return self.__book

    @property
    def quantity(self) -> int:
        return self.__quantity

