# This program displays the amortization schedule for the loan
print("Loan amortization schedule")
Loan_Amount = float(input("Loan Amount: "))
Year = int(input("Number of Years: "))
Interest_Rate = float(input("Annual Interest Rate: "))
if (Loan_Amount <= 0) or (Year <= 0) or (Interest_Rate <= 0):
    print("Error: The input is invalid. Please try again")
else:
    # Compute the monthly payment and total payment
    Monthly_Interest_Rate = Interest_Rate / 1200
    Monthly_Payment = Loan_Amount * Monthly_Interest_Rate / (1 - 1 / (1 + Monthly_Interest_Rate) ** (Year * 12))
    Total_Payment = Monthly_Payment * Year * 12
    # Round the number in two decimal pieces
    Monthly_Payment = round(Monthly_Payment, 2)
    Total_Payment = round(Total_Payment, 2)
    # Display the result
    print()
    print("Monthly Payment: ", Monthly_Payment)
    print("Total Payment: ", Total_Payment)
    # Display the table
    print()
    print("Payment#\tInterest\tPrincipal\tBalance")
    Balance = Loan_Amount
    for Payment in range(1, Year * 12 + 1):
        Interest = Monthly_Interest_Rate * Balance
        Principal = Monthly_Payment - Interest
        Balance = Balance - Principal
        # Round the number in two decimal pieces
        Interest = round(Interest, 2)
        Principal = round(Principal, 2)
        Balance = round(Balance, 2)  # Balance at the end can not be zero
        # Use format() to ensure the table is even
        print("{:<12}{:<12}{:<12}{:<25}".format(Payment, Interest, Principal, Balance))
