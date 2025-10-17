# This program sums a given series
def sum_series(n):  # Define function
    # Display the table
    total = 0
    for i in range(1, n + 1):
        fraction_a = i
        fraction_b = i + 1
        # Calculate using given formula
        total += fraction_a / fraction_b
        total = round(total, 3)
        print(f'{i}\t\t\t{total}')


def main():  # Define main function
    n = 20
    print("Sum Series Table")
    print("i\t\t\tm(i)")
    sum_series(n)


# Display the result
main()
