# This program computes CD value after specific months
# Input the values
print("CD Value after specific months")
Amount = float(input("Enter the initial deposit amount: "))
AnnualRate = float(input("Enter annual percentage yield: "))
Month = int(input("Enter maturity period (number of months): "))
if Amount <= 0:
    print("Error: The deposit amount is invalid. Please proceed and try again")
elif AnnualRate <= 0:
    print("Error: The annual yield is invalid. Please proceed and try again")
elif Month <= 0:
    print("Error: The maturity period is invalid. Please proceed and try again")
else:
    # Display the table
    print()
    print("Month\t\tCD Value")
    # Compute the CD value
    MonthRate = AnnualRate / 1200
    for Period in range(1, Month + 1):
        Amount = Amount + (Amount * MonthRate)
        # Display the result
        print(f'{Period}\t\t\t{round(Amount, 2)}')
