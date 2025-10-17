# Calculate energy needed to heat water
# Given formula : Q = M * (final temperature - init temperature) * 4184
# Input
print("Calculating Energy")
amount = (float(input("Enter the amount of water in kilograms: ")))
init_temperature = (float(input("Enter the initial temperature: ")))
final_temperature = (float(input("Enter the final temperature: ")))
# Calculate
energy = amount * (final_temperature - init_temperature) * 4184
# Display the result
print("The energy needed is", energy)
