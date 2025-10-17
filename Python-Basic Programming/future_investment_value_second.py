# This program computes the future investment value
def future_investment_value(investment_amount, monthly_interest_rate, years):  # Define function
    # Calculate the annual interest rate
    annual_interest_rate = monthly_interest_rate / 1200
    for years in range(1, years + 1):
        # Calculate using the formula
        investment_amount = investment_amount * ((1 + annual_interest_rate) ** 12)
        # Display the table
        print(f'{years}\t\t\t\t{round(investment_amount, 2)}')


def main():  # Define main function
    print("Future Investment Value")
    # Input the value
    amount_invested = float(input("The amount invested: "))
    annual_interest_rate = int(input("Annual interest rate: "))
    years = 30  # Assume the value for the function
    print("Years\t\tFuture Value")
    future_investment_value(amount_invested, annual_interest_rate, years)


# Display the result
main()
