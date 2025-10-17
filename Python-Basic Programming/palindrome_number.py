# This program determines palindrome number
# Input a three-digit integer
Integer = int(input("Enter a three-digits integer: "))
if (Integer >= 1000) or (Integer < 100):
    print("Error: You didn't enter a three-digits integer. Please proceed and try again")
else:
    # The integer is a palindrome if it reads the same both sides
    # Both the first digit and the last digit of the integer has to share the same number
    # This function helps take out the first and the last digit of the integer
    Digit_in_Front = Integer % 10
    Digit_in_Back = Integer // 100
    # Display the result
    if Digit_in_Front == Digit_in_Back:
        print(Integer, "is a palindrome")
    else:
        print(Integer, "is not a palindrome")
