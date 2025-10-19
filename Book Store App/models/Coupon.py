# Class Coupon
from datetime import datetime

class Coupon:
    def __init__(self, code: str, discount_percent: float, expiry_date):
        self.__code = code
        self.__discount_percent = discount_percent
        self.__expiry_date = expiry_date

    def apply_discount(self, total: float) -> float:
        return total * (1 - self.__discount_percent / 100)

    def is_valid(self) -> bool:
        return datetime.now() < self.__expiry_date

    def get_code(self):
        return self.__code

    @property
    def discount(self) -> float:
        return self.__discount_percent

    @property
    def expiry(self) -> datetime:
        return self.__expiry_date
