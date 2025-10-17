# This program plays Subtraction Quiz by generating ten random subtraction questions
import random
import time
CorrectCount = 0
Count = 0
Number_of_Question = 10
print("Subtraction Quiz Game with Time Count")
StartTime = time.time()
# The limit is 10 questions
for Count in range(1, Number_of_Question + 1):
    print("Question", Count, ":",  end=" ")
    Number1 = random.randint(0, 9)
    Number2 = random.randint(0, 9)
    if Number1 < Number2:
        Number1, Number2 = Number2, Number1
    # Input the answer
    Answer = int(input("What is " + str(Number1) + " - " + str(Number2) + " ? "))
    # Check if the answer is correct
    if Answer == Number1 - Number2:
        print("Your answer is correct")
        CorrectCount += 1  # Count only the correct answers
    else:
        print("Your answer is incorrect")
EndTime = time.time()
# Calculate the time
Time = int(EndTime - StartTime)
# Display the result
print("Result")
print("------------------------------")
print("Correct Answer: ", CorrectCount, "out of", Count)
print("Time: ", Time, 'seconds')
