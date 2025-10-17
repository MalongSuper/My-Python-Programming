# This program computes a given series
def estimate(i):  # Define function
    # Calculate the m value
    m = 0
    for i in range(1, i + 1):
        m += ((-1) ** (i + 1)) / (2 * i - 1)
    m *= 4
    m = round(m, 4)
    return m


def main():  # Define main function
    # Display the table
    print("Compute a given series")
    print("i\t\t\tm(i)")
    for n in range(1, 2):
        print(n, end="\t\t\t")
        print(estimate(n))
    for n in range(101, 902, 100):
        print(n, end="\t\t\t")
        print(estimate(n))


# Display the result
main()
