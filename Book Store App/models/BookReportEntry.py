# book_report_entry.py
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.Book import Book


class BookReportEntry:
    def __init__(self, book: 'Book', quantity: int, price_at_time: float):
        self.__book = book
        self.__quantity = quantity
        self.__price_at_time = price_at_time

    def total_price(self) -> float:
        return self.__quantity * self.__price_at_time

    @property
    def book(self) -> 'Book':
        return self.__book

    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def price_at_time(self) -> float:
        return self.__price_at_time
