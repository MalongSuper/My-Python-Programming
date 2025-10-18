# This program finds the first n terms of the Fibonacci series using recursion
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci (Recursion)")
number = int(input("Enter a number: "))
print("The Fibonacci Number is", fibonacci(number))
