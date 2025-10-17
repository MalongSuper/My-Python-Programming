# Given Formula : V = (R - 2*E) / S
# Input
R = (float(input("Enter the length of the row in feet =")))
E = (float(input("Enter the amount of space by an end-post assembly in feet =")))
S = (float(input("Enter the amount of space between the vines in feet =")))
# Calculate using the formula
V = (R - (2*E)) / S
# Display Results
print("The number of grapevines that will fit in the row =",int(V))
# The number of grapevines cannot be a decimal number
