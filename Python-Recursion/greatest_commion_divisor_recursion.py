# This program finds the Greatest Common Divisor of two numbers using recursion.


def greatest_common_divisor(n1, n2):
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    else:
        return greatest_common_divisor(n2, n1 % n2)


print("Greatest Common Divisor (Recursion)")
number1 = int(input("Enter Number 1: "))
number2 = int(input("Enter Number 2: "))
result = greatest_common_divisor(number1, number2)
print("Greatest Common Divisor:", result)
