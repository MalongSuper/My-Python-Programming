# This program calculate average acceleration
# Given formula: a = (v1 - v0) / t
# Input
print("Acceleration")
v0, v1, t = eval(input("Enter v0, v1, and t: "))
# Calculate
average = (v1 - v0) / t
# Display the result
print("The average acceleration is", round(average, 4))
