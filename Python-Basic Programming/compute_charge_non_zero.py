# This program modifies converts monetary unit but displays the nonzero denominations only
# Input the amount
Amount = eval(input("Enter an amount in double: "))
if Amount < 0:
    print("You cannot enter a negative number. "
          "Please proceed and try again")
elif Amount == 0:
    print("There is no amount")
else:
    # Convert the amount to cents
    Amount_to_Cent = int(Amount * 100)
    # Calculate the dollars
    Dollars = Amount_to_Cent // 100
    Remain_Dollars = Amount_to_Cent % 100
    # Calculate the quarters
    Quarters = Remain_Dollars // 25
    Remain_Quarters = Remain_Dollars % 25
    # Calculate the dimes
    Dimes = Remain_Quarters // 10
    Remain_Dimes = Remain_Quarters % 10
    # Calculate the nickels
    Nickels = Remain_Dimes // 5
    Remain_Nickels = Remain_Dimes % 5
    # Calculate the pennies
    Pennies = Remain_Nickels
    # Display the results but only the nonzero denominations
    print("Your amount", Amount, "consists of")
    if Dollars == 1:
        print(Dollars, "dollar")
    elif Dollars > 1:
        print(Dollars, "dollars")
    if Quarters == 1:
        print(Quarters, "quarter")
    elif Quarters > 1:
        print(Quarters, "quarters")
    if Dimes == 1:
        print(Dimes, "dime")
    elif Dimes > 1:
        print(Dimes, "dimes")
    if Nickels == 1:
        print(Nickels, "nickel")
    elif Nickels > 1:
        print(Nickels, "nickels")
    if Pennies == 1:
        print(Pennies, "penny")
    elif Pennies > 1:
        print(Pennies, "pennies")
