# Calculate population in one year
# 1 year = 31,536,000 seconds
# One birth every 7 seconds
print("Population in the next 5 Year:")
birth = 31536000 // 7
# One death every 13 seconds
death = 31536000 // 13
# One new immigrant every 45 seconds
immigrant = 31536000 // 45
# Calculate the population for each of the next five years
# Current population : 312,032,486
population = 312032486
population_year1 = (population + birth) - death + immigrant
population_year2 = (population_year1 + birth) - death + immigrant
population_year3 = (population_year2 + birth) - death + immigrant
population_year4 = (population_year3 + birth) - death + immigrant
population_year5 = (population_year4 + birth) - death + immigrant
# Display the result
print("Year 1 =", population_year1)
print("Year 2 =", population_year2)
print("Year 3 =", population_year3)
print("Year 4 =", population_year4)
print("Year 5 =", population_year5)
