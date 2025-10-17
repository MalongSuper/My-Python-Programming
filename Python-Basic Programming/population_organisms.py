# This program predicts the approximate size of a population of organisms
Number_of_Date = 0
Day_Approximate = 0
Organisms = 0
# Input the starting number of organisms
Number_of_Organisms = int(input("Starting number of organism : "))
# Input the average daily population increase as a percentage
Average = float(input("Average daily increase in percentage (%) : "))
# Input the number of days the organisms will be left to multiply
Number_of_Days = int(input("Number of days to multiply : "))
if (Number_of_Organisms <= 0) or (Average <= 0) or (Number_of_Days <= 0):
    print("Error: Some of the values you entered are invalid. Please proceed and try again")
else:
    # Display the table
    print('Day Approximate\t\t\tPopulation')
    print("-----------------------------------")
    # The value will stay the same at Day 1
    for Day_Approximate in range(1, 2):
        Day_Approximate += Number_of_Date
        Organisms = Number_of_Organisms
    print(f'{Day_Approximate}\t\t\t\t\t\t{Organisms}')
    # Calculates the increase of population from Day 2
    for Day_Approximate in range(2, Number_of_Days + 1):
        Number_of_Organisms = Number_of_Organisms + (Number_of_Organisms * (Average / 100))
        print(f'{Day_Approximate}\t\t\t\t\t\t{Number_of_Organisms}')
