# This program determines whether a number is a perfect number
print("Perfect Number")
print("These are four perfect numbers below 10000")
# Check if the number is divisible
for Number in range(1, 10001):
    Total_Divisor = 0
    for Divisor in range(1, Number):
        # Exclude the divisor being the number itself
        if (Number % Divisor) == 0 and Divisor != Number:
            # Compute the sum of the divisors
            Total_Divisor += Divisor
    # The number is perfect when it is equal to the sum of all of its divisors
    if Total_Divisor == Number:
        Perfect_Number = Number
        # Display the result
        print("", Perfect_Number, end=" ")
