import json
import os
from sqlalchemy import Column, String, Float, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Setup SQLAlchemy
Base = declarative_base()
DB_PATH = "books.db"
JSON_PATH = os.path.join(os.path.dirname(__file__), "templates/books_data.json")


class Book(Base):
    __tablename__ = "books"
    title = Column(String, primary_key=True)
    author = Column(String)
    price = Column(String)
    description = Column(String)


engine = create_engine(f"sqlite:///{DB_PATH}")
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)


# JSON Helpers
def load_books_from_json():
    if not os.path.exists(JSON_PATH):
        return []
    with open(JSON_PATH, "r") as f:
        return json.load(f)


def save_books_to_json(books):
    with open(JSON_PATH, "w") as f:
        json.dump(books, f, indent=2)


# Sync JSON to DB
def sync_books_to_db():
    session = SessionLocal()
    books = load_books_from_json()
    added = 0
    for b in books:
        if not session.query(Book).filter_by(title=b["title"]).first():
            new_book = Book(
                title=b["title"],
                author=b["author"],
                price=b["price"],
                description=b["description"]
            )
            session.add(new_book)
            added += 1
    session.commit()
    session.close()
    print(f"{added} books synced to books.db")


# Sync DB to JSON
def export_books_to_json():
    session = SessionLocal()
    books = session.query(Book).all()
    result = [
        {
            "title": b.title,
            "author": b.author,
            "price": b.price,
            "description": b.description
        } for b in books
    ]
    save_books_to_json(result)
    session.close()
    print("Exported books to JSON")


if __name__ == "__main__":
    sync_books_to_db()
    # export_books_to_json()  # Optional
