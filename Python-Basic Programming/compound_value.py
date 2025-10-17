# This program calculates account value after the sixth month
# Suppose the annual interest rate of 5%
Interest_Rate = 1 + 0.00417
Account_Value = 0
# Input the monthly saving amount
Amount = float(input("Enter the monthly saving amount: "))
if Amount < 0:
    print("Error: You cannot enter a negative number. "
          "Please proceed and try again")
else:
    # Calculate the value after the first month
    for Month in range(1):
        Account_Value = Amount * Interest_Rate
    # Calculate the value for the sixth month
    for Month in range(2, 7):
        Account_Value = (Amount + Account_Value) * Interest_Rate
    # Display the result
    print("After the sixth month, the account value is", round(Account_Value, 4))
