# This program displays two highest scores
Highest_Score = 0
SecondHighest_Score = 0
Highest_Name = []
Second_Highest_Name = []
# Input number pf students
print("Find the highest and second-highest score")
Number_of_Students = int(input("Enter the number of students: "))
if Number_of_Students <= 0:
    print("Error: Number of students cannot be negative. "
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
            Second_Highest_Name = Highest_Name
            SecondHighest_Score = Highest_Score  # This variable uses for second-highest score
            Highest_Score = Score
            Highest_Name = Student
        # The program finds the second-highest score
        # The elif removes the highest score above and find the remaining highest score
        elif Score > SecondHighest_Score:
            SecondHighest_Score = Score
            Second_Highest_Name = Student
    # Display the results
    print("Result:")
    print("Student", str(Highest_Name), "got the highest score")
    print("The highest score is", Highest_Score)
    print("Student", str(Second_Highest_Name), "got the second highest score")
    print("The second-highest score is", SecondHighest_Score)
