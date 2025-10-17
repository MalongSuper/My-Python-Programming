# This program simulates Monte Carlo
import random
OddPosition = 0
# Position 1 is on the left side of the square
# Position 3 is on the upper right side of the square, wrap in a triangle
# The dart is thrown one million times
print("Monte Carlo")
for NumberDarts in range(1, 1000001):
    # Indicate co-ordinate (x, y) for every time
    X = random.uniform(-1, 1)
    Y = random.uniform(-1, 1)
    # Assume the co-ordinate for each point of the square are
    # (-1,1); (1,1); (-1, -1), (1, -1)
    # Check the point by the co-ordinates
    # Check if the dart is in position 1 of the square
    if (X <= 0) and (Y >= -1) and (Y <= 1):
        OddPosition += 1
    # Check if the dart is in position 3 (triangle) of the square
    if (X >= 0) and (Y >= 0) and (Y <= 1) and (X + Y) <= 1:
        OddPosition += 1
# Check for the probability for the dart to fall into an odd-numbered
Probability = (OddPosition / 1000000) * 100
print("The Dart hits the odd position", OddPosition, "time")
print("The probability is", round(Probability, 2), "%")
