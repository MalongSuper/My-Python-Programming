# This program implements the sqrt function using Babylonian rule
def sqrt(n):
    # Assume initial positive value for last guess is 1
    last_guess = 1
    next_guess = (last_guess + (n / last_guess)) / 2
    # Use a loop to add the number to the value continue to calculate the next guess
    # The loop ends when difference between next guess and small guess is less than 0.0001
    # Next guess and Last guess can switch place
    while abs(next_guess - last_guess) >= 0.0001:
        last_guess = next_guess
        next_guess = (last_guess + (n / last_guess)) / 2
    return next_guess


def main():
    print("Approximate Square Root")
    # Input a number
    n = float(input("Enter a positive number: "))
    if n < 0:
        print("Error: Negative number is invalid. Please try again")
    else:
        print("The Square Root is", sqrt(n))


# Display the result
main()
