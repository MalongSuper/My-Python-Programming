# This program finds factorial number using recursion
# Use a ** b = a × a ** b-1


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial Number (Recursion)")
number = int(input("Enter a number: "))
print("Result:", factorial(number))
