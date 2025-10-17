# This program calculate future investment value
# Input
print("Future Investment Value")
investment_amount = float(input("Enter investment amount: "))
annual_interest_rate = float(input("Enter annual interest rate: "))
year = int(input("Enter number of years: "))
# Year is not negative
if year < 1:
    print("Year is not negative. Please proceed and try again")
else:  # Convert and calculate using the formula
    month = year * 12
    month_interest_rate = annual_interest_rate / 100 / 12
    investment_value = investment_amount * ((1 + month_interest_rate) ** month)
    # Display the result
    print("Accumulated value is", investment_value)
