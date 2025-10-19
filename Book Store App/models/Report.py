# Report
from typing import List, TYPE_CHECKING
from models.BookReportEntry import BookReportEntry
if TYPE_CHECKING:
    from models.Order import Order


class Report:
    def __init__(self, sales_data: dict, inventory_data: dict, user_activity: dict):
        self.__sales_data = sales_data
        self.__inventory_data = inventory_data
        self.__user_activity = user_activity
        self.__orders: List['Order'] = []  # 0..* association
        self.__book_entries: List[BookReportEntry] = []  # N entries

    def add_order(self, order: 'Order') -> None:
        self.__orders.append(order)

    def add_book_entry(self, entry: BookReportEntry):
        self.__book_entries.append(entry)

    def get_book_entries(self) -> List[BookReportEntry]:
        return self.__book_entries

    def generate_book_report(self) -> str:
        report = "Book Sales Report:\n"
        total = 0
        for entry in self.__book_entries:
            subtotal = entry.total_price()
            total += subtotal
            report += f"- {entry.book.title}: {entry.quantity} units at {entry.price_at_time:.2f} = {subtotal:.2f}\n"
        report += f"\nTotal Book Sales: {total:.2f}\n"
        return report

    def get_orders(self) -> List['Order']:
        return self.__orders

    def generate_sales_report(self) -> str:
        report = "Sales Report:\n"
        for key, value in self.__sales_data.items():
            report += f"{key}: {value}\n"
        return report

    def generate_sales_orders(self) -> str:
        report = "Sales Report (From Orders):\n"
        total = 0
        for order in self.__orders:
            report += f"- Order ID: {order.id}, Amount: {order.total_amount:.2f}\n"
            total += order.total_amount
        report += f"\nTotal Revenue: {total:.2f}\n"
        return report

    def generate_user_report(self) -> str:
        report = "User Activity Report:\n"
        for key, value in self.__user_activity.items():
            report += f"{key}: {value}\n"
        return report

    def generate_inventory_report(self) -> str:
        report = "Inventory Report:\n"
        for key, value in self.__inventory_data.items():
            report += f"{key}: {value}\n"
        return report
