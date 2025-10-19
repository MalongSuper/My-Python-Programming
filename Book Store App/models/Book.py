# Class Book
import uuid
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from models.User import Administrator


class Book:
    def __init__(self, title: str, category: str, price: float,
                 stock: int, description: str, is_free: bool, admin: 'Administrator'):
        self.__book_id = "B" + str(uuid.uuid4())
        self.__title = title
        self.__category = category
        self.__price = price
        self.__stock = stock
        self.__description = description
        self.__is_free = is_free
        self.__reviews: List['Review'] = []
        self.__admin = admin  # One admin

    @property
    def admin(self) -> 'Administrator':
        return self.__admin

    # Methods
    def preview(self) -> str:
        return f"{self.__title} ({self.__category}): {self.__description}"

    def update_stock(self, amount: int) -> None:
        self.__stock -= amount

    # Properties (getters)
    @property
    def id(self) -> str:
        return self.__book_id

    @property
    def title(self) -> str:
        return self.__title

    @property
    def category(self) -> str:
        return self.__category

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    @property
    def description(self) -> str:
        return self.__description

    @property
    def is_free(self) -> bool:
        return self.__is_free

    def add_review(self, review: 'Review'):
        self.__reviews.append(review)

    def get_reviews(self) -> List['Review']:
        return self.__reviews

    def get_average_rating(self) -> float:
        approved_reviews = [r.rating for r in self.__reviews if r.approved]
        return sum(approved_reviews) / len(approved_reviews) if approved_reviews else 0



