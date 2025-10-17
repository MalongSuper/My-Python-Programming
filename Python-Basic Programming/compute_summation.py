# This program computes the given summation
# The given summation is 1/(1 + sqrt(2)) + 1/(sqrt(2) + sqrt(3))...1/(sqrt(624) + sqrt(625))
from math import sqrt
print("Compound Summation")
# Determine the first formula
Summation = 1 / (1 + sqrt(2))
# Determine the remaining formulas
for Number in range(2, 625):
    # Determine the numbers in summation as A and B
    A = Number
    B = Number + 1
    Summation = Summation + (1 / (sqrt(A) + sqrt(B)))
# Display the result
print("The total of the summation is", round(Summation))
