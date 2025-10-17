# This program finds the minimum amount of sales for $30000
# The base salary is $5,000
Money = 0
# Display the table for amount of sales from $5000 to $30000
print("The Sales Amount")
print("Salary($)\t\tMinimum Amount of Sales")
print("----------------------------------------")
for Sales_Amount in range(5000, 30001, 1000):
    # Lower than $5000 = 8%
    if Sales_Amount <= 5000:
        Money = Sales_Amount * 0.08
    # Higher than $5000 but lower than $10000 = 10%
    elif Sales_Amount <= 10000:
        Money = 5000 * 0.08 + (Sales_Amount - 5000) * 0.1
    # Higher than $10000 = 12%
    elif Sales_Amount > 10000:
        Money = 5000 * 0.08 + (10000 - 5000) * 0.1 + (Sales_Amount - 10000) * 0.12
    print(f'{Sales_Amount}\t\t\t\t\t{int(Money)}')
# Display the result
print("Result:")
print("The minimum amount of sales in order to make $30000 is", int(Money))
