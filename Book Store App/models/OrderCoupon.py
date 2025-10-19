# Class Order Coupon
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.Order import Order
    from models.Coupon import Coupon


class OrderCoupon:
    def __init__(self, order: 'Order', coupon: 'Coupon'):
        self.__order = order
        self.__coupon = coupon

    def verify_coupon(self) -> bool:
        return self.__coupon.is_valid()

    def apply(self, total: float) -> float:
        return self.__coupon.apply_discount(total)
