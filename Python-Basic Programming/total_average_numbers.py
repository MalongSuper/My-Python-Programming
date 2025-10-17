# This program computes the total and average of numbers
Number = 0
Total = 0
Positive = 0
Negative = 0
Total_Number = 0
Average = 0
print("Total and Average of Numbers")
while Number >= 0 or Number < 0:
    Number = int(input("Enter an integer, the input ends if it is 0: "))
    # Calculate the number of negative and positive numbers
    if Number > 0:
        Positive += 1
    if Number < 0:
        Negative += 1
    # The program should end when the user input 0
    if Number == 0:
        print("You entered the integer 0. The program is terminated")
        break
    # Calculate the total and average of the numbers
    Total += Number
    Total_Number = Positive + Negative
    Average = Total / Total_Number
# Display the result
print("Result:")
print("The number of positive is", Positive)
print("The number of negative is", Negative)
print("The total is", Total)
print("The average is", round(Average, 2))
