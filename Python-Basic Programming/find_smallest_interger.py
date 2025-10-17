# This program finds the smallest n such that n^2 > 12,000
Number = 0
print("Smallest Number for n^2 > 12000")
print("Number\t\tPower Number")
print("------------------------")
# Limit the loop, so it should stop when n^2 is greater 12000
while (Number ** 2) < 12000:
    Number += 1
    Power_Number = Number ** 2
    # Display the table
    print(f'{Number}\t\t\t\t{Power_Number}')
# Display the result
print("Result:")
print("The table displays every power number until it exceeds 12000")
print("The smallest number such that n^2 is greater than 12,000 is", Number)
