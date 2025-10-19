# Class User
from abc import ABC, abstractmethod
from models.Report import Report
import uuid
from typing import List


class User(ABC):
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    @property
    def email(self):
        return self.__email

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def userId(self):
        return NotImplemented

    @abstractmethod
    def register(self):
        pass

    def login(self, email, password):
        if self.__email == email and self.__password == password:
            print(f"{self.name} logged in successfully.")
            return True
        else:
            print("Login failed.")
            return False

    def logout(self):
        print(f"{self.name} has logged out.")

    def edit_profile(self, new_name, new_email):
        self.__name = new_name
        self.__email = new_email
        print("Profile updated.")


class Customer(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.__user_id = "C" + str(uuid.uuid4())
        self.__orders = []  # Association to Order objects
        self.__report: Report = None  # 0..1 Association
        self.__reviews: List['Review'] = []

    @property
    def userId(self):
        return self.__user_id

    def register(self):
        print(f"Customer '{self.name}' registering with Bookie or third-party...")
        print("Verification email sent to user.")
        print(f"Generated user ID: {self.userId}")
        return True

    @staticmethod
    def search_books(keyword):
        print(f"Searching for books with keyword: {keyword}")

    @staticmethod
    def add_to_cart(book):
        print(f"Added '{book}' to cart")

    def place_order(self, order):
        self.__orders.append(order)

    def get_orders(self):
        return self.__orders

    def view_order_history(self):
        print(f"Order history for {self.__name}:")
        for order in self.__orders:
            order.generate_invoice()

    @staticmethod
    def track_order(order_id):
        print(f"Tracking order with ID: {order_id}")

    @staticmethod
    def download_pdf(order_id):
        print(f"Downloading PDF for order ID: {order_id}")

    @staticmethod
    def apply_coupon(coupon_code):
        print(f"Applying coupon code: {coupon_code}")

    def set_report(self, report: Report):
        self.__report = report

    def get_report(self) -> Report:
        return self.__report

    def generate_sales_report(self):
        if self.__report:
            print(self.__report.generate_sales_report())
        else:
            print("No report assigned to this customer.")

    def generate_user_activity_report(self):
        if self.__report:
            print(self.__report.generate_user_report())
        else:
            print("No report assigned to this customer.")

    def add_review(self, review: 'Review'):
        self.__reviews.append(review)

    def get_reviews(self) -> List['Review']:
        return self.__reviews


class Administrator(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.__admin_id = "A" + str(uuid.uuid4())
        self.__books: List['Book'] = []  # 0..* books

    @property
    def userId(self):
        return self.__admin_id

    def register(self):
        print(f"Admin '{self.name}' submitting credentials for validation...")
        print("Admin validated by system policy.")
        print(f"Admin email created: {self.name.lower().replace(' ', '')}@bookie.com")
        print(f"Generated admin ID: {self.userId}")
        return True

    def upload_book(self, book: 'Book'):
        self.__books.append(book)
        return f"Book '{book}' uploaded successfully"

    def get_books(self) -> List['Book']:
        return self.__books

    @staticmethod
    def manage_inventory():
        print("Inventory management panel opened")

    @staticmethod
    def view_reports():
        print("Generating reports...")
