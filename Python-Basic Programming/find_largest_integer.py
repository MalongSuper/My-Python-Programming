# This program finds the largest n such that n^3 < 12,000
# Assume from 101 to below
Number = 102
print("Largest Number for n^3 < 12000")
print("Number\t\tThree Power Number")
print("------------------------------")
# Limit the loop, so it should stop when n^3 is less than 12000
while (Number ** 3) > 12000:
    Number -= 1
    ThreePower_Number = Number ** 3
    # Display the table
    print(f'{Number}\t\t\t\t{ThreePower_Number}')
# Display the result
print("Result:")
print("The table displays every three power number until it is below 12000")
print("The largest number such that n^3 is less than 12,000 is", Number)
