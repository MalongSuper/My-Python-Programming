# This program displays square root table
import math
print("Square Roots Table")
print("Number\t\tSquare Root")
# Display the table
for Number in range(0, 21, 2):
    Square_Root = math.sqrt(Number)
    print(f'{Number}\t\t\t{round(Square_Root, 4)}')
