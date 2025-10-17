# This program displays matrix of 0s and 1s
import random


def print_number(n):  # Define function
    line = n
    count = 0
    # The line of the matrix depends on the number
    for matrix in range(1, n + 1):
        # Display the number
        for number in range(1, n + 1):
            element = random.randint(0, 1)
            print(element, end=" ")
            count += 1
            if (count % line) == 0:
                print()


def main():
    print("Matrix of 0s and 1s")
    # Input the number
    n = int(input("Enter n: "))
    if n <= 1:
        print("Error: Cannot display matrix because the input is invalid. "
              "Please proceed and try again")
    else:
        print_number(n)  # Use the function


# Display the result
main()
