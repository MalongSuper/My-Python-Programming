# This program finds the sum of digits of a given number using recursion
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(int(n / 10))


print("Sum of Digits (Recursion)")
number = int(input("Enter a number: "))
result = sum_digits(number)
print("The sum of digits is", result)
