# This program calculates Population in the next n years
# Assume: One birth every 7 seconds;
# One death every 13 seconds;
# One new immigrant every 45 seconds
# 1 year = 31,536,000 seconds
print("Population in next years")
current_population = int(input("Enter current population: "))
year = int(input("Enter the number of years: "))
# Calculate the population
birth = 31536000 // 7
death = 31536000 // 13
immigrant = 31536000 // 45
# Using a loop
population = 0
for i in range(year):
    population = (current_population + birth) - death + immigrant
    current_population = population
# Display the result
print("Population for the next", year, "year is", population)
