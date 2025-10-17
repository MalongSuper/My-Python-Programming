# This program reverses a four-digit number
Number = int(input("Enter a four-digit number: "))
if (Number >= 10000) or (Number < 1000):
    print("Error: The number you entered must be four-digit. "
          "Please proceed and try again")
elif Number < 0:
    print("Error: You cannot enter a negative number. "
          "Please proceed and try again")
else:
    # Assume the value
    Reverse_Number = 0
    # Create a loop that will do continuous calculation
    while Number > 0:
        Digit = Number % 10
        Reverse_Number = (Reverse_Number * 10) + Digit
        Number = Number // 10
        # The loop will stop when the number divided has reached zero
    print("The reversed number is:", Reverse_Number)
