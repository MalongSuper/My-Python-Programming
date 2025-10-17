# This program displays monthly and total payments for interest rates
Interest_Rate = 5.0
Interest = 0
print("Compare loans with various interest rates")
Loan_Amount = float(input("Loan Amount: "))
Year = int(input("Number of Years: "))
if (Loan_Amount <= 0) or (Year <= 0):
    print("Error: The input is invalid. Please try again")
else:
    # Display the table
    print("Interest Rate\t\tMonthly Payment\t\tTotal Payment")
    # Compute for the initial interest rate 5%
    Monthly_Interest_Rate = Interest_Rate / 1200
    Monthly_Payment = Loan_Amount * Monthly_Interest_Rate / (1 - 1 / (1 + Monthly_Interest_Rate) ** (Year * 12))
    Total_Payment = Monthly_Payment * Year * 12
    print(f'{Interest_Rate}%\t\t\t\t{round(Monthly_Payment, 2)}\t\t\t\t{round(Total_Payment, 2)}')
    # Each interest rate starting from 5% to 8%, with an increment of 1/8
    # Every interest rate is timed to increase fraction e.g. 41/40, 42/41, 43/42,...64/63
    for Interest in range(41, 65):
        FractionA = Interest
        FractionB = Interest - 1
        Interest_Rate = Interest_Rate * (FractionA / FractionB)
        Interest_Rate = round(Interest_Rate, 3)
        # Compute for the remaining interest rate
        Monthly_Interest_Rate = Interest_Rate / 1200
        Monthly_Payment = Loan_Amount * Monthly_Interest_Rate / (1 - 1 / (1 + Monthly_Interest_Rate) ** (Year * 12))
        Total_Payment = Monthly_Payment * Year * 12
        # Round the number in two decimal pieces
        Monthly_Payment = round(Monthly_Payment, 2)
        Total_Payment = round(Total_Payment, 2)
        # Make sure the table is displayed evenly using format()
        print("{:<20}{:<20}{:<40}".format("{}%".format(Interest_Rate), Monthly_Payment, Total_Payment))
