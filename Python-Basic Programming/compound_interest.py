# Given Formula : A = P*((1 + (r/n))**(n*t))
# Input
P = (float(input("Enter the amount of principal originally deposited to the account =")))
r = (float(input("Enter the annual interest rate paid by the account =")))
n = (int(input("Enter the number of time per year that the interest is compounded =")))
# If the interest is 4, it is compounded quarterly
if n == 4:
    print("(The interest is compounded quarterly)")
# If the interest is 12, it is compounded monthly
if n == 12:
    print("(The interest is compounded monthly)")
# The number of time per year has to be a natural number
# Input
t = (int(input("Enter the number of years the account will be left to earn interest =")))
# The number of years has to be a natural number
# Calculate using the formula
A = P * ((1 + (r/n))**(n*t))
# Display Results
print("The amount of money in the account after",t,"years =","$",A)

