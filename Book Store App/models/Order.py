# Class Order
import uuid
from datetime import datetime
from typing import List, TYPE_CHECKING
from models.OrderItem import OrderItem
from models.OrderCoupon import OrderCoupon
from models.ShippingProvider import ShippingProvider
if TYPE_CHECKING:
    from models.Payment import Payment
    from models.User import Customer
    from models.Book import Book


class Order:
    def __init__(self, customer: 'Customer', payment_status: str, delivery_address: str):
        self.__id = "B" + str(uuid.uuid4())
        self.__customer = customer
        self.__order_items: List[OrderItem] = []
        self.__total_amount = 0
        self.__payment_status = payment_status
        self.__delivery_address = delivery_address
        self.__payment: 'Payment' = None
        self.__date_created = datetime.now()
        self.__order_coupons: List[OrderCoupon] = []
        self.__shipping_provider: ShippingProvider = None

    def add_item(self, book: 'Book', quantity: int):
        item = OrderItem(book, quantity)
        self.__order_items.append(item)
        self.__total_amount += item.total_price()
        book.update_stock(quantity)

    def generate_invoice(self) -> str:
        invoice = f"Invoice for Order ID: {self.__id}\n"
        invoice += f"Date: {self.__date_created.strftime('%Y-%m-%d %H:%M:%S')}\n"
        invoice += f"Customer: {self.__customer.userId}\n"
        invoice += f"Delivery Address: {self.__delivery_address}\n"
        invoice += f"Payment Status: {self.__payment_status}\n"
        invoice += "\nItems:\n"

        for item in self.__order_items:
            invoice += f"- {item.book.title} x {item.quantity} = {item.total_price():.2f}\n"

        invoice += f"\nTotal Amount: {self.__total_amount:.2f}\n"
        return invoice

    def update_status(self, new_status: str) -> None:
        self.__payment_status = new_status

    def add_coupon(self, order_coupon: OrderCoupon):
        if order_coupon.verify_coupon():
            self.__order_coupons.append(order_coupon)
            self.__total_amount = order_coupon.apply(self.__total_amount)

    @property
    def order_coupons(self):
        return self.__order_coupons

    @property
    def id(self):
        return self.__id

    @property
    def customer(self) -> 'Customer':
        return self.__customer

    @property
    def order_items(self):
        return self.__order_items

    @property
    def total_amount(self):
        return self.__total_amount

    @property
    def payment(self):
        return self.__payment

    def set_payment(self, payment: 'Payment'):
        self.__payment = payment

    @property
    def date_created(self) -> datetime:
        return self.__date_created

    def set_shipping_provider(self, provider: ShippingProvider):
        self.__shipping_provider = provider

    @property
    def shipping_provider(self) -> ShippingProvider:
        return self.__shipping_provider

    def to_dict(self):
        return {
            "id": self.id,
            "customer": {
                "email": self.customer.email,
                "name": self.customer.name
            },
            "items": [
                {
                    "title": item.book.title,
                    "price": item.book.price,
                    "quantity": item.quantity
                } for item in self.order_items
            ],
            "total_amount": self.total_amount,
            "payment_status": self.payment.status if self.payment else "Pending",
            "payment": {
                "id": self.payment.payment_id,
                "method": self.payment.method,
                "status": self.payment.status
            } if self.payment else None,
            "coupon": {
                "code": self.order_coupons[0]._OrderCoupon__coupon.get_code(),
                "discount": self.order_coupons[0]._OrderCoupon__coupon.discount
            } if self.order_coupons else None,
            "date_created": self.date_created.isoformat()
        }



