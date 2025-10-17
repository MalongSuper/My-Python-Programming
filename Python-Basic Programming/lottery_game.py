# This program plays Lottery Game by generating a three-digit lottery number
import random
print("Lottery Game")
# Random generated lottery number
Lottery_Number = random.randint(100, 999)
# Input a three-digits number
User_Number = int(input("Enter a three-digits number: "))
if (User_Number < 100) or (User_Number > 999):
    print("Error: Invalid value. Please proceed and try again")
else:
    print("The lottery has generated number:", Lottery_Number)
    # If the user number matches the lottery number in the exact order, the award is $10,000
    if User_Number == Lottery_Number:
        print("Exact match. Your award is $10,000")
    else:
        # Get all the digits from Lottery_Number
        Lottery_Digit1 = Lottery_Number // 100
        Lottery_Digit2 = (Lottery_Number // 10) % 10
        Lottery_Digit3 = Lottery_Number % 10
        # Get all the digits from User_Number
        User_Digit1 = User_Number // 100
        User_Digit2 = (User_Number // 10) % 10
        User_Digit3 = User_Number % 10
        # If the digits in the user number matches the lottery number, the award is $3,000
        # Supposed that the user entered number 123
        # The match lottery number is 132, 213, 231, 312, 321
        if (((Lottery_Digit1 == User_Digit1) and (Lottery_Digit2 == User_Digit3) and (Lottery_Digit3 == User_Digit2))
                or ((Lottery_Digit1 == User_Digit2) and (Lottery_Digit2 == User_Digit1)
                    and (Lottery_Digit3 == User_Digit3))
                or ((Lottery_Digit1 == User_Digit2) and (Lottery_Digit2 == User_Digit3)
                    and (Lottery_Digit3 == User_Digit1))
                or ((Lottery_Digit1 == User_Digit3) and (Lottery_Digit2 == User_Digit1)
                    and (Lottery_Digit3 == User_Digit2))
                or ((Lottery_Digit1 == User_Digit3) and (Lottery_Digit2 == User_Digit2)
                    and (Lottery_Digit3 == User_Digit1))):
            print("Match all digits. Your award is $3,000")
        else:
            # If at least one digit in the number matches the lottery number, the award is $1,000.
            List = (Lottery_Digit1, Lottery_Digit2, Lottery_Digit3)
            if (User_Digit1 in List) or (User_Digit2 in List) or (User_Digit3 in List):
                print("Match one digit. Your award is $1,000")
            else:
                print("No match found")
