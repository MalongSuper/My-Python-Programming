# This program finds the highest number and counts its occurrence
Number = 0
Count = 0
# Indicate the number to avoid the highest being zero when entering only negative
Highest_Number = float('-inf')
print("Highest number and its occurrence")
while Number >= 0 or Number < 0:
    Number = int(input("Enter a number (0: for end of input): "))
    # The program stops when the user enters zero
    if Number == 0:
        print("You entered the number zero. The program is terminated")
        break
    # Find the highest number in the run
    if Number > Highest_Number:
        Highest_Number = Number
        # Reset the count when the highest number is found
        Count = 1
    # Count its occurrence
    elif Number == Highest_Number:
        Count += 1
# Display the result
print("Result:")
print("The highest number is", Highest_Number)
print("The occurrence count of the largest number is", Count)
