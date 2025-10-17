# This program computes the gratuity and total
# Using split() to enter two values in one line
# The value must be a float
Subtotal, Gratuity_Rate = [float(SG) for SG in input("Enter the subtotal and the gratuity rate: ").split(",")]
if (Subtotal < 0) or (Gratuity_Rate < 0):
    print("Error: You cannot enter a negative number. "
          "Please proceed and try again")
else:
    # Calculates the gratuity and total
    Gratuity = Subtotal * (Gratuity_Rate / 100)
    Total = Subtotal + Gratuity
    # Display the result
    print("The gratuity is", round(Gratuity, 2), "and the total is", round(Total, 2))
