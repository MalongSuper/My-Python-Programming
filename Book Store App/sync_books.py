import json
import os
from sqlalchemy import create_engine, Column, String, Float, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.Book import Book

# SQLAlchemy setup
Base = declarative_base()
DB_PATH = "books.db"
JSON_PATH = "templates/books_data.json"

class BookAccount(Base):
    __tablename__ = "books"
    id = Column(String, primary_key=True)
    title = Column(String)
    author = Column(String)
    price = Column(Float)
    description = Column(String)
    category = Column(String, default="General")
    stock = Column(Integer, default=10)
    is_free = Column(Boolean, default=False)

engine = create_engine(f"sqlite:///{DB_PATH}")
SessionLocal = sessionmaker(bind=engine)

# Recreate table
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# Load JSON
if not os.path.exists(JSON_PATH):
    print("books_data.json not found.")
    exit()

with open(JSON_PATH, "r") as file:
    books = json.load(file)

db = SessionLocal()
added = 0
for b in books:
    # Use Book class for logic
    price = float(b["price"].replace("$", "")) if "price" in b else 0.0
    book_obj = Book(
        title=b["title"],
        category=b.get("category", "General"),
        price=price,
        stock=10,
        description=b.get("description", ""),
        is_free=price == 0.0,
        admin=None  # Set admin if needed
    )
    db.add(BookAccount(
        id=book_obj.id,
        title=book_obj.title,
        author=b.get("author", ""),
        price=book_obj.price,
        description=book_obj.description,
        category=book_obj.category,
        stock=book_obj.stock,
        is_free=book_obj.is_free
    ))
    added += 1
    print(f"Added: {book_obj.title}")

db.commit()
db.close()
print(f"\nSync complete: {added} books added.")
