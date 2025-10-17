# This program calculates account value after specific months
print("Account Value after specific months")
# Input the value
Amount = float(input("Enter an amount: "))
AnnualInterest_Rate = float(input("Enter the annual interest rate: "))
Month = int(input("Enter the number of months: "))
if Amount <= 0:
    print("Error: The amount is invalid. "
          "Please proceed and try again")
elif AnnualInterest_Rate <= 0:
    print("Error: The annual interest rate is invalid. "
          "Please proceed and try again")
elif Month <= 0:
    print("Error: The month is invalid. Please proceed and try again")
else:
    # Calculate the Interest Rate
    Interest_Rate = ((AnnualInterest_Rate / 100) / 12)
    Account_Value = 0
    # Calculate the value after the first month
    for Account in range(1, 2):
        Account_Value = Amount * (1 + Interest_Rate)
    # Calculate the value after the given month
    for Account in range(2, Month + 1):
        Account_Value = (Amount + Account_Value) * (1 + Interest_Rate)
    # Display the result
    print("The Amount in the savings account after", Month, "months:", round(Account_Value, 3))
