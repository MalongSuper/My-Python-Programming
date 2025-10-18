# Create Table with Python
from rich.table import Table
from rich.console import Console

console = Console()
table = Table(title=input("* Enter table name: "))

number_of_columns = int(input("* Enter number of columns: "))

for col in range(number_of_columns):
    table.add_column(input(f"+ Enter column {col + 1}: "))

for row in range(number_of_columns):
    table.add_row(input(f"- Enter row {row + 1}: "))

console.print(table)
