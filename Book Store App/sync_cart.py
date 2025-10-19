from cart_db import CartItem, SessionLocal
from cart_json import load_cart


def sync_cart_to_db():
    db = SessionLocal()
    cart_items = load_cart()
    added = 0

    for item in cart_items:
        existing = db.query(CartItem).filter_by(
            user_email=item["user_email"],
            book_title=item["book_title"]
        ).first()
        if not existing:
            db.add(CartItem(
                user_email=item["user_email"],
                book_title=item["book_title"],
                price=item["price"],
                quantity=item["quantity"]
            ))
            added += 1

    db.commit()
    db.close()
    print(f"{added} cart items synced to cart.db")
