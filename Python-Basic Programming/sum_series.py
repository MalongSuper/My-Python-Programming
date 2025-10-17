# This program sums a given series
# The series is 1/3 + 3/5 + 5/7 +... + 95/97 + 97/99
print("Sum a series")
Total = 0
# Give out fractions
for Number in range(1, 98, 2):
    FractionA = Number
    FractionB = Number + 2
    # Compute the series
    Total = Total + (FractionA / FractionB)
# Display the result
print("The sum of the series is", Total)
