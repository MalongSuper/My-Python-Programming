# This program will calculate the grade of a student's examination
# The examination includes two tests worth 25pts and a main exam worth 50pts
# Input the grades of each tests
Test1 = int(input("Enter the point of Test 1 :"))
Test2 = int(input("Enter the point of Test 2 :"))
Exam = int(input("Enter the point of the main exam :"))
# The point of an exam cannot be negative or higher than its maximum point
if Test1 > 25 or Test1 < 0:
    print("Error: The point of Test 1 should only be around 0 to 25."
          "Please proceed and try again")
elif Test2 > 25 or Test2 < 0:
    print("Error: The point of Test 2 should only be around 0 to 25."
          "Please proceed and try again")
elif Exam > 50 or Exam < 0:
    print("Error: The point of the main exam should only be around 0 to 50." 
          "Please proceed and try again")
else:
    Final = int(Test1 + Test2 + Exam)
    print("The Overall Score is", Final, "points")
# If the main exam's point is below 50, the student will be graded fail
    if Exam < 25:
        print("Grade : FAIL")
# If the overall score for all the exams is below 50, the student will be graded fail
    else:
        if Final < 50:
            print("Grade : FAIL")
# If the student passes, a certain grade level is received based on the points
        elif Final >= 80:
            print("Grade : DISTINCTION")
        elif (Final < 80) and (Final >= 60):
            print("Grade : CREDIT")
        elif (Final < 60) and (Final >= 50):
            print("Grade : PASS")