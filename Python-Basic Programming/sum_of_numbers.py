# This program display the sum of positive numbers
Total = 0
Positive = 0
# The loop will keep going forever when you enter positive numbers
while Positive >= 0:
    Positive = int(input("Enter a positive number :"))
    # The loop will end when you enter a negative number
    if Positive < 0:
        print("You entered a negative number. The loop is terminated")
        break
    # The program will then sum up all the entered numbers
    Total += Positive
# Display their sum
print("The sum of all the positive numbers :", Total)
