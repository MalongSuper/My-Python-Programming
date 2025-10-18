# This program finds a ** b using recursion
# Use a ** b = a × a ** b-1


def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)


print("Power Number (Recursion)")
value_a = int(input("Enter a: "))
value_b = int(input("Enter b: "))
print("Result:", power(value_a, value_b))
