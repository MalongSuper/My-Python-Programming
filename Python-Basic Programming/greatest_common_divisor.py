# This program computes the greatest common divisor
GCD = 0
print("Greatest Common Divisor")
Number1 = int(input("Enter first integer: "))
Number2 = int(input("Enter second integer: "))
if (Number1 <= 0) or (Number2 <= 0):
    print("Error: The number is invalid. Please try again")
else:
    # Find D to be the minimum of Number 1 and Number 2
    # Suppose D is Number 1
    if Number1 < Number2:
        # Simulates d, d - 1, d - 2, ..., 2, 1 by for in range()
        for D in range(1, Number1 + 1):
            if (Number1 % D) == 0 and (Number2 % D) == 0:
                GCD = D
        print("The Greatest Common Divisor for", Number1, "and", Number2, "is", GCD)
    # Suppose D is Number 2
    if Number2 < Number1:
        for D in range(1, Number2 + 1):
            if (Number1 % D) == 0 and (Number2 % D) == 0:
                GCD = D
        print("The Greatest Common Divisor for", Number1, "and", Number2, "is", GCD)
    # If it is the same number, the number is the GCD
    if Number1 == Number2:
        GCD = Number1 = Number2
        print("The Greatest Common Divisor for", Number1, "and", Number2, "is", GCD)
