# This program plays Millionaire Math Quiz Game
import random
import time
operators = ["+", "-", "*", "/"]
money = 0
count = 0
print("Welcome to Millionaire Math Quiz")
print("+ There are 30 basic math questions")
print("+ For every correct answer, you receive $1000")
print("+ The game ends when you get a wrong answer")
print("+ Best prize: $30.000")
time.sleep(3)
ready = str(input("Are you ready (Press Yes or No) ? "))
if ready == "Y" or ready == "Yes":
    print("Let's get started!!")
    for i in range(30):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operator = random.choice(operators)
        result = ""
        if number1 < number2:  # Swap position of number1 and number2 for subtraction
            number1, number2 = number2, number1
        if operator == "+":
            result = number1 + number2
        elif operator == "-":
            result = number1 - number2
        elif operator == "*":
            result = number1 - number2
        elif operator == "/":
            result = number1 // number2
        answer = int(input(f"What is {number1} {operator} {number2} ? "))
        if answer == result:
            print("Correct Answer")
            money += 1000
            count += 1
        else:
            print("Incorrect Answer")
            break
    # Display result
    print("=====================================")
    # If the user answers all 30 questions correctly
    if count == 30:
        print("CONGRATULATION!! YOU WON")
        print("You earned:", "$", money)
    else:
        print("GAME OVER")
        print("You earned:", "$", money)
    print("=====================================")
elif ready == "N" or ready == "No":
    print("The game is terminated. Please read the introduction "
          "and rerun the code if you are ready")
else:
    print("The game is terminated. Please enter properly next time")
