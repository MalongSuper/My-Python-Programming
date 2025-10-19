# Class Review
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.Book import Book
    from models.Customer import Customer


class Review:
    def __init__(self, review_id: str, book: 'Book', customer: 'Customer', rating: int, comment: str):
        if not (0 <= rating <= 5):
            raise ValueError("Rating must be between 0 and 5")
        self.review_id = review_id
        self.book = book
        self.customer = customer
        self.rating = rating
        self.comment = comment
        self.approved = False
        self.timestamp = datetime.now()

        # Bidirectional association
        self.book.add_review(self)
        self.customer.add_review(self)

    def approve(self) -> None:
        self.approved = True
        print(f"Review {self.review_id} approved.")

    def reject(self) -> None:
        self.approved = False
        print(f"Review {self.review_id} rejected.")
