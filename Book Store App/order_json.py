import json
import os

ORDER_JSON_PATH = "templates/order.json"

def save_order_to_json(order):
    order_data = order.to_dict()

    if os.path.exists(ORDER_JSON_PATH):
        with open(ORDER_JSON_PATH, "r") as f:
            try:
                orders = json.load(f)
            except json.JSONDecodeError:
                orders = []
    else:
        orders = []

    orders.append(order_data)

    with open(ORDER_JSON_PATH, "w") as f:
        json.dump(orders, f, indent=2, default=str)

def load_orders_by_user(email):
    if not os.path.exists(ORDER_JSON_PATH):
        return []

    with open(ORDER_JSON_PATH, "r") as f:
        try:
            orders = json.load(f)
        except json.JSONDecodeError:
            return []

    user_orders = [
        order for order in orders if order.get("customer", {}).get("email") == email
    ]
    return user_orders








