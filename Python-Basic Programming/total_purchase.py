# Calculate Total Purchase
# Input
Item1 = (float(input("Enter the price of Item 1 = $")))
Item2 = (float(input("Enter the price of Item 2 = $")))
Item3 = (float(input("Enter the price of Item 3 = $")))
Item4 = (float(input("Enter the price of Item 4 = $")))
Item5 = (float(input("Enter the price of Item 5 = $")))
# Calculate
Subtotal = (Item1) + (Item2) + (Item3) + (Item4) + (Item5)
Salestax = 0.7
# Display Results
print("The subtotal of the sale = $",(Subtotal))
print("The amount of salestax = $",(Subtotal * Salestax))
print("Total = $",(Subtotal + (Subtotal * Salestax)))