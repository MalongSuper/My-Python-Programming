# Calculate Payment Instalments
# Input
Purchase = (float(input("Enter the amount of purchase = $")))
Payment = (int(input("Enter the desired number of payment instalments =")))
# Calculate
TotalPurchase = ((Purchase * 0.05) + Purchase)
Instalments = (TotalPurchase / Payment)
# Display Results
print("The total amount of the purchase =","$",(TotalPurchase))
print("The amount of instalments cost =","$",(Instalments))