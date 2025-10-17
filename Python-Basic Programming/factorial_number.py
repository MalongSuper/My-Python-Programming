# This program calculates the factorial of a number
# Input a non-negative integer
Factorial = 1
Number = int(input("Enter a non-negative integer: "))
print("The factorial of the number")
while Number < 0:
    Number = int(input("Only non-negative number is allowed. Please enter again:"))
# Calculate the factorial of a number
for Number in range(1, Number + 1):
    # Formula : n! = n * (n-1) * (n-2) *...1
    Factorial *= Number
# Display the factorial
print(Number, "!", "=", Factorial)
