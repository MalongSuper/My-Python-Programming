# This program calculates the amount of money a person
# Would earn over a period of time
# Input the number of days
Days = 0
Salary_First = 0
Salary_Double = 2
Total_Salary = 0
Number_of_Days = int(input("Enter the number of days you have worked :"))
if Number_of_Days < 0:
    print("Error: The number of days cannot be negative. "
          "Please proceed and try again")
elif Number_of_Days == 0:
    print("You cannot earn salary with zero day work")
else:
    # For the first two days, You earn one penny for the first day
    if Number_of_Days == 1:
        print('Day\t\t\tSalary')
        print("--------------------")
        print(f'{1}\t\t\t{1}')
        print("The total salary you will earn :", "0.01 dollars")
    else:
        # You earn two pennies for day two
        print('Day\t\t\tSalary')
        print("--------------------")
        for Days in range(1, 3):
            Salary_First = Days
            print(f'{Days}\t\t\t{Salary_First}')
            # Calculate the salary in the first two days
            Total_Salary += Days
            # From each day, the penny continues to double
        for Days in range(3, Number_of_Days + 1):
            Salary_Double *= Salary_First
            print(f'{Days}\t\t\t{Salary_Double}')
            # Calculate the salary for every day after
            Total_Salary += Salary_Double
        # One penny = 0.01 dollars
        print("The total salary you will earn :", Total_Salary * 0.01, "dollars")
