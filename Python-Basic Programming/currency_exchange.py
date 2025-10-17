# This program converts the exchange rate between US Dollars and Chinese RMB
# Input the exchange rate from Dollars to RMB
Exchange_Rate = float(input("Enter the exchange rate from Dollars to RMB: "))
# Input whether to convert Dollars to RMB or the opposite
Dollars_to_RMB = int(input("Enter 0 to convert Dollars to RMB and 1 vice versa: "))
if Exchange_Rate <= 0:
    print("Error: The exchange rate is invalid. Please proceed and try again")
elif (Dollars_to_RMB != 0) and (Dollars_to_RMB != 1):
    print("Error: Incorrect input")
else:
    # When the input is 0, converts from Dollars to RMB
    if Dollars_to_RMB == 0:
        Dollars = float(input("Enter the dollar amount: "))
        while Dollars < 0:
            Dollars = float(input("Incorrect value. Please enter again: "))
        Converted_RMB = Dollars * Exchange_Rate
        print("$", Dollars, "is", round(Converted_RMB, 2), "yuan")
    # When the input is 1, converts from RMB to Dollars
    if Dollars_to_RMB == 1:
        RMB = float(input("Enter the RMB amount: "))
        while RMB < 0:
            RMB = float(input("Incorrect value. Please enter again: "))
        Converted_Dollars = RMB / Exchange_Rate
        print(RMB, "yuan", "is $", round(Converted_Dollars, 2))
