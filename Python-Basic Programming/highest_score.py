# This program displays the student's highest score
Highest_Score = 0
Highest_Name = []
# Input number pf students
print("Find the highest score")
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
        # The program finds the highest number in the loop
        if Score > Highest_Score:
            Highest_Score = Score
            Highest_Name = Student
    # Display the result
    print("Result:")
    print("Student", str(Highest_Name), "got the highest score")
    print("The highest score is", Highest_Score)
