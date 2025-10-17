# This program play Addition and Subtraction Quiz
# There are 50 questions
import random
import time
correct_answer = 0
number_of_question = 50
print("Addition & Subtraction Quiz")
start = time.time()
for i in range(number_of_question):
    equation = random.choice(["+", "-"])
    number1, number2 = random.randint(1, 999), random.randint(10, 999)
    if number1 < number2:
        number1, number2 = number2, number1
    answer = int(input(f"Question {i + 1}: What is {number1} {equation} {number2}? "))
    # Check for the answer by comparing it to the result
    if equation == "+":
        if answer == number1 + number2:
            print("=> Correct")
            correct_answer += 1
        else:
            print("=> Incorrect")
    elif equation == "-":
        if answer == number1 - number2:
            print("=> Correct")
            correct_answer += 1
        else:
            print("=> Incorrect")
# End time count
end = time.time()
# Display end result
print("------------------------------")
print("The quiz is over")
print(f"Correct Answer: {correct_answer} / 50")
print(f"Time: {round(end - start, 2)}")
print("------------------------------")






