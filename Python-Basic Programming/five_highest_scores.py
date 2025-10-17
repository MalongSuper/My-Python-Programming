# This program displays five highest scores
# Highest score
Highest_Score = 0
SecondHighest_Score = 0
ThirdHighest_Score = 0
FourthHighest_Score = 0
FifthHighest_Score = 0
# Highest Student name
Highest_Name = []
Second_Highest_Name = []
Third_Highest_Name = []
Fourth_Highest_Name = []
Fifth_Highest_Name = []
# Input number pf students
print("Five highest scores")
Number_of_Students = int(input("Enter the number of students (>= 5): "))
if Number_of_Students <= 0:
    print("Error: Number of students cannot be negative. "
          "Please proceed and try again")
elif Number_of_Students < 5:
    print("Error: Number of students must be at least 5 or greater. "
          "Please proceed and try again")
else:
    for Student in range(1, Number_of_Students + 1):
        # Input the score of each student
        Score = float(input("Enter the score of student" + " " + str(Student) + ": "))
        while Score < 0:
            print("Error: The input is invalid")
            Score = float(input("Enter the score of student" + " " + str(Student) + ": "))
        # The program finds the highest score
        if Score > Highest_Score:
            FifthHighest_Score = FourthHighest_Score
            Fifth_Highest_Name = Fourth_Highest_Name
            FourthHighest_Score = ThirdHighest_Score
            Fourth_Highest_Name = Third_Highest_Name
            ThirdHighest_Score = SecondHighest_Score
            Third_Highest_Name = Second_Highest_Name
            SecondHighest_Score = Highest_Score
            Second_Highest_Name = Highest_Name  # This variable uses for second-highest score
            Highest_Score = Score
            Highest_Name = Student
        # The program finds the remaining highest scores
        elif Score > SecondHighest_Score:
            FifthHighest_Score = FourthHighest_Score
            Fifth_Highest_Name = Fourth_Highest_Name
            FourthHighest_Score = ThirdHighest_Score
            Fourth_Highest_Name = Third_Highest_Name
            ThirdHighest_Score = SecondHighest_Score
            Third_Highest_Name = Second_Highest_Name
            SecondHighest_Score = Score
            Second_Highest_Name = Student
        elif Score > ThirdHighest_Score:
            FifthHighest_Score = FourthHighest_Score
            Fifth_Highest_Name = Fourth_Highest_Name
            FourthHighest_Score = ThirdHighest_Score
            Fourth_Highest_Name = Third_Highest_Name
            ThirdHighest_Score = Score
            Third_Highest_Name = Student
        elif Score > FourthHighest_Score:
            FifthHighest_Score = FourthHighest_Score
            Fifth_Highest_Name = Fourth_Highest_Name
            FourthHighest_Score = Score
            Fourth_Highest_Name = Student
        elif Score > FifthHighest_Score:
            FifthHighest_Score = Score
            Fifth_Highest_Name = Student
    # Display the results
    print("===========================================================")
    print("Result:")
    print("Congratulations to five students with the highest score!!")
    print("Student", Highest_Name, ":", Highest_Score)
    print("Student", Second_Highest_Name, ":", SecondHighest_Score)
    print("Student", Third_Highest_Name, ":", ThirdHighest_Score)
    print("Student", Fourth_Highest_Name, ":", FourthHighest_Score)
    print("Student", Fifth_Highest_Name, ":", FifthHighest_Score)
    rint("===========================================================")
    