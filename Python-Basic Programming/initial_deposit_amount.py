# Find the initial deposit amount
# Input
print("Initial Deposit Amount")
account_value = float(input("Enter final account value: "))
annual_interest_rate = float(input("Enter annual interest rate in percent: "))
year = int(input("Enter number of years: "))
# Year is not negative
if year < 1:
    print("Year is not negative. Please proceed and try again")
else:  # Convert and calculate using the formula
    month = year * 12
    month_interest_rate = annual_interest_rate / 100 / 12
    init_deposit_amount = account_value / ((1 + month_interest_rate) ** month)
    # Display the result
    print("Initial deposit value is", init_deposit_amount)
