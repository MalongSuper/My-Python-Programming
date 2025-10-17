# This program displays table of pentagonal number
def get_pentagonal_number(n):  # Define functions
    number_per_line = 10
    count = 0
    for m in range(1, n + 1):
        n = m * (3 * m - 1) // 2
        # Display the table using format()
        print(format(n, '5d'), end=" ")
        # Display ten numbers per line
        count += 1
        if (count % number_per_line) == 0:
            print()


def main():  # Main functions
    print("\t\t\t\tTable of Pentagonal Number")
    print("-------------------------------------------------------------")
    n = 100
    get_pentagonal_number(n)  # Use the result from the previous function


# Display the result
main()
