# Rabbit Problem with Fibonacci

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

def main():
    month = int(input("Enter the number of months: "))
    print(f"Number of rabbit pairs after {month} months is: {fibonacci(month)}")


main()