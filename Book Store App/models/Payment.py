# Class Payment
import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.Order import Order  # Only used during type checking, not at runtime


class Payment:
    def __init__(self, order: 'Order', method: str):
        self.__payment_id = "P" + str(uuid.uuid4())
        self.__order = order
        self.__method = method
        self.__status = "Pending"

    def process(self) -> bool:
        print(f"Processing payment {self.__payment_id} for Order {self.__order.id} using {self.__method}...")
        # Simulate external system logic here
        self.__status = "Processed"
        return True

    def confirm(self) -> bool:
        if self.__status == "Processed":
            self.__status = "Confirmed"
            print(f"Payment {self.__payment_id} confirmed.")
            return True
        print("Cannot confirm payment that is not processed.")
        return False

    @property
    def payment_id(self) -> str:
        return self.__payment_id

    @property
    def order(self) -> 'Order':
        return self.__order

    @property
    def method(self) -> str:
        return self.__method

    @property
    def status(self) -> str:
        return self.__status
