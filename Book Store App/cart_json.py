import json
import os

CART_JSON_PATH = os.path.join(os.path.dirname(__file__), "templates/cart_data.json")


def load_cart():
    if not os.path.exists(CART_JSON_PATH):
        return []
    with open(CART_JSON_PATH, "r") as f:
        return json.load(f)


def save_cart(user_email, cart_items):
    if not os.path.exists(CART_JSON_PATH):
        all_data = []
    else:
        with open(CART_JSON_PATH, "r") as f:
            all_data = json.load(f)

    # Remove previous entries for this user
    all_data = [entry for entry in all_data if entry["user_email"] != user_email]

    for item in cart_items:
        all_data.append({
            "user_email": user_email,
            "book_title": item["title"],
            "price": float(item["price"].replace("$", "")),
            "quantity": item.get("quantity", 1)
        })

    with open(CART_JSON_PATH, "w") as f:
        json.dump(all_data, f, indent=2)


def remove_cart_by_email(email):
    if not os.path.exists(CART_JSON_PATH):
        return
    with open(CART_JSON_PATH, "r") as f:
        try:
            cart_data = json.load(f)
        except json.JSONDecodeError:
            cart_data = []

    cart_data = [item for item in cart_data if item.get("user_email") != email]

    with open(CART_JSON_PATH, "w") as f:
        json.dump(cart_data, f, indent=2)