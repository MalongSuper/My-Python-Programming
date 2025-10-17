# Calculate Tip, Tax, and Total
# Input
Charge = (float(input("Enter the charge of the food = $")))
# Calculate
Tip = (Charge * 0.18)
Tax = (Charge * 0.07)
Total = Charge + Tip + Tax
# Display Results
print("The amount of 18% Tip = $",Tip)
print("The amount of 7% Salestax = $",Tax)
print("Total = $",Total)