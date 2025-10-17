# This program calculates the projected semester tuition amount for the next 5 years.
# The tuition for a full-time student is $8,000 per semester
Tuition_Amount = 0
Semester_per_Year = 0
# Display the table
print('Semester\t\tTuition Amount')
print("-------------------------------")
# For the first semester, the tuition should be $8000
for Semester in range(1, 2):
    Semester += Tuition_Amount
    Semester_per_Year = 8000
    print(f'{Semester}\t\t\t\t $ {Semester_per_Year}')
# The tuition will increase by 3 percent each year for the next 5 years
for Semester in range(2, 6):
    Semester_per_Year = Semester_per_Year + (Semester_per_Year * 0.03)
    print(f'{Semester}\t\t\t\t $ {Semester_per_Year}')
