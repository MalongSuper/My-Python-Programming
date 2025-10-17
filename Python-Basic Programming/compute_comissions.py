# This program computes the commissions
def compute_commissions(sales_amount):  # Define function
    money = 0
    # Compute the sales for $10000
    if sales_amount == 10000:
        money = 5000 * 0.08 + (10000 - 5000) * 0.1
    # Compute the sales for higher than $10000 = 12%
    elif sales_amount > 10000:
        money = 5000 * 0.08 + (10000 - 5000) * 0.1 + (sales_amount - 10000) * 0.12
    print(f'{sales_amount}\t\t\t{int(money)}')


def main():  # Define main function
    print("Table of Commission")
    print("Sales Amount\tCommission")
    # Display the table
    for sales_amount in range(10000, 100001, 5000):
        compute_commissions(sales_amount)


# Display the result
main()
