# This program solves Fibonacci using iteration
def fibonacci(n):
    if n <= 1:
        return False
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


print("Fibonacci (Iteration)")
number = int(input("Enter a number: "))
if fibonacci(number) is False:
    print("No Fibonacci Number Found")
else:
    print("The Fibonacci Number is", fibonacci(number))
