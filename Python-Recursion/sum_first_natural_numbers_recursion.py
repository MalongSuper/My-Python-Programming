# This program finds the sum of first n natural numbers using recursion


def sum_natural_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum_natural_number(n - 1)


print("Sum Natural Numbers (Recursion)")
number = int(input("Enter a length of natural number: "))
print("The Sum is", sum_natural_number(number))
