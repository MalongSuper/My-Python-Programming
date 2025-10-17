# This program computes the series of cancellation
print("Demonstrate cancellation errors")
print("Assume the n = 50000")
# Suppose n is 50000
Left_to_Right = 0
Right_to_Left = 0
n = 50000
# Compute the series from left to right
for In in range(1, n + 1):
    Left_to_Right += 1 / In
print("The summation from left to right:", Left_to_Right)
# Compute the series from right to left
for In in range(n + 1, 0, -1):
    Right_to_Left += 1 / In
# Display the results
print("The summation from right to left:", Right_to_Left)
