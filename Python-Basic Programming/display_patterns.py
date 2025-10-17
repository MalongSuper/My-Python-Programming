# This program displays number pattern
def display_pattern(n):  # Define function
    for P in range(1, n + 1):
        for R in range(n - P):  # This code uses to space the pattern
            print(format("  "), end="")
        for S in range(P, 0, -1):
            print(format(S, '2d'), end="")
        print()


def main():  # Define main function
    print("Display Pattern")
    # Input value
    n = int(input("Enter a number: "))
    display_pattern(n)


# Display the result
main()
