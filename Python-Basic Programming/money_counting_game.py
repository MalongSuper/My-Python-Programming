# This program creates a money change-counting game
# Input the number of pennies, nickels, dimes and quarters
Pennies = int(input("Enter the number of pennies :"))
Nickels = int(input("Enter the number of nickels :"))
Dimes = int(input("Enter the number of dimes :"))
Quarters = int(input("Enter the number of quarters :"))
# The number of coins cannot be negative or a zero
if (Pennies < 1) or (Nickels < 1) or (Dimes < 1) or (Quarters < 1):
    print("Error: The number of coins cannot be negative or a zero. "
          "Please proceed and try again")
else:
    # 1 penny = 0.01 dollars, 1 nickel = 0.05 dollars,
    # 1 dime = 0.1 dollars, 1 quarter = 0.25 dollars
    # Combine all of the coins to dollars
    Dollar = (Pennies * 0.01) + (Nickels * 0.05) + (Dimes * 0.1) + (Quarters * 0.25)
    # Display the total dollars
    print("The total value of the coins is",Dollar,"dollars")
    # The user will win the game if the total value is exactly one dollar
    if Dollar == 1:
        print("Congratulation! You won the game")
    # If the user doesn't win, display if the amount is more or less than a dollar
    else:
        if Dollar > 1:
            print("The amount you entered was more than 1 dollar")
        elif Dollar < 1:
            print("The amount you entered was less than 1 dollar")


