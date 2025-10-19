# Author
import uuid
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from models.BookAuthor import BookAuthor


class Author:
    def __init__(self, author_name: str, bio: str):
        self.__author_id = "A" + str(uuid.uuid4())
        self.__author_name = author_name
        self.__bio = bio
        self.__books: List[BookAuthor] = []

    def add_book(self, book_author: 'BookAuthor') -> None:
        self.__books.append(book_author)

    def get_books(self) -> List:
        return [entry.book for entry in self.__books]

    @property
    def author_id(self) -> str:
        return self.__author_id

    @property
    def author_name(self) -> str:
        return self.__author_name

    @property
    def bio(self) -> str:
        return self.__bio
