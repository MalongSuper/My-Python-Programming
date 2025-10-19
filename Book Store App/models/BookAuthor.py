# Book Author
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.Author import Author
    from models.Book import Book


class BookAuthor:
    def __init__(self, book: 'Book', author: 'Author', role: str, contribution: str):
        self.__book = book
        self.__author = author
        self.__role = role
        self.__contribution = contribution

    def get_role(self) -> str:
        return self.__role

    def get_contribution_level(self) -> str:
        return self.__contribution

    @property
    def book(self) -> 'Book':
        return self.__book

    @property
    def author(self) -> 'Author':
        return self.__author
