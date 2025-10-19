import json
from datetime import datetime

def load_coupons():
    with open("templates/coupon.json", "r") as f:
        return json.load(f)

def save_coupons(coupons):
    with open("templates/coupon.json", "w") as f:
        json.dump(coupons, f, indent=2)

def get_user_coupon(email, code):
    for coupon in load_coupons():
        if coupon["user_email"] == email and coupon["code"] == code:
            return coupon
    return None
