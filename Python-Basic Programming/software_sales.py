# This program displays the total amount of a purchase with a discount
# Input the number of packages purchased
Retails = 99
Quantity = int(input("Enter the number of packages purchased :"))
# Quantity cannot be negative
if Quantity < 0:
    print("Error: The number of packages cannot be negative. "
          "Please proceed and try again")
else:
    # You must enter the default discount number first
    Discount = 0
    # If the quantity is less than 10, you receive no discount
    if Quantity < 10:
        Discount = 0
    # If the quantity is around 10 to 19, you receive 10% discount
    elif (Quantity >= 10) and (Quantity <= 19):
        Discount = 0.1
    # If the quantity is around 20 to 49, you receive 20% discount
    elif (Quantity >= 20) and (Quantity <= 49):
        Discount = 0.2
    # If the quantity is around 50 to 99, you receive 30% discount
    elif (Quantity >= 50) and (Quantity <= 99):
        Discount = 0.3
    # If the quantity is above 100, you receive 40% discount
    elif Quantity >= 100:
        Discount = 0.4
    # Calculate the total amount of the purchase after discount
    print("You received", Discount * 100, "%", "discount")
    Total = Quantity * Retails
    Total_after_discount = Total - (Total * Discount)
    print("The total amount of the purchase before discount =", "$", Total)
    print("The total amount of the purchase after discount =", "$", Total_after_discount)


