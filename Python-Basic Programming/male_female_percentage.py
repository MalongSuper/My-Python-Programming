# Male and Female Percentages in class
# Input
Class = (str(input("Enter the Class Name =")))
Male = (int(input("Enter the number of males registered in the class =")))
Female = (int(input("Enter the number of females registered in the class =")))
# Calculate
Student = Male + Female
print("There are",Student,"students in Class",Class)
PerMale = Male / Student
PerFemale = Female / Student
# Display Results
print("The percentages of males in the class =",round(PerMale * 100),"%")
print("The percentages of females in the class =",round(PerFemale * 100),"%")
