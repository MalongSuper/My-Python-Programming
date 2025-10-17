# This program sums the digits in an integer
# Input a number
Number = int(input("Enter a number between 0 and 1000: "))
if (Number < 0) or (Number > 1000):
    print("Error: The number you entered is not in the limit. "
          "Please proceed and try again")
else:
    Total_Digit = 0
    while Number > 0:
        # Use the % operator to extract digits
        Digit = Number % 10
        # Calculate the digits
        Total_Digit += Digit
        # Use the // operator to remove the extracted digit
        Number = Number // 10
        # The program will continue until the Number has reached zero
    print("The sum of the digits is", Total_Digit)
