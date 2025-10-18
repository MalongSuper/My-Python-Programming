# This program finds the Lowest Common Multiple of two numbers using the preceding result.

def greatest_common_divisor(n1, n2):
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    else:
        return greatest_common_divisor(n2, n1 % n2)


def lowest_common_multiple(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    else:
        return (n1 * n2) // greatest_common_divisor(n1, n2)


print("Lowest Common Multiple (Recursion)")
number1 = int(input("Enter Number 1: "))
number2 = int(input("Enter Number 2: "))
result = lowest_common_multiple(number1, number2)
print("Lowest Common Multiple:", result)
