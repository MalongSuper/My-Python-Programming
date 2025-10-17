# This program converts monetary units as an integer whose last two digits are the cents
# Input an integer with the last two digits represent the cents
Amount = int(input("Enter an amount: "))
if Amount < 0:
    print("Error: You cannot enter a negative number. "
          "Please proceed and try again")
else:
    # Display the represents
    Dollars = Amount // 100
    Cents = Amount % 100
    if Dollars >= 1:
        print("The amount you entered represents", Dollars, "dollars and", Cents, "cents")
    if Dollars < 1:
        print("The amount you entered represents", Cents, "cents")
    # Calculate the dollars
    Dollars_Cents = Amount / 100
    # Calculate the quarters
    Quarters = Cents // 25
    Remain_Quarters = Cents % 25
    # Calculate the dimes
    Dimes = Remain_Quarters // 10
    Remain_Dimes = Remain_Quarters % 10
    # Calculate the nickels
    Nickels = Remain_Dimes // 5
    Remain_Nickels = Remain_Dimes % 5
    # Calculate the pennies
    Pennies = Remain_Nickels
    # Display the results
    print("Your amount", Dollars_Cents, "consists of")
    print("\t", Dollars, "dollars\n",
          "\t", Quarters, "quarters\n",
          "\t", Dimes, "dimes\n",
          "\t", Nickels, "nickels\n",
          "\t", Pennies, "pennies")
