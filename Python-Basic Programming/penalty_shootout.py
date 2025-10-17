# This program creates game Penalty Shootout
import time
import random
# Initial value
striker = ["Left", "Right", "Middle"]
goalkeeper = ["Left", "Right", "Middle"]
score_A, score_B = 0, 0
count_shot = 0
attempt = 1
team = 0
game_over = False
print("Penalty Shootout", end="")
# The main game system using loop
while not game_over:
    if team == 0:
        print("\nAttempt", attempt)
    print(f"Team A turns" if team == 0 else "Team B turns")
    shoot = input("Striker choose your position: ")
    keeper = random.choice(goalkeeper)
    if shoot not in striker:
        print("The striker attempts to shoot")
        time.sleep(2)
        print("The ball is sent to the crowd. MISSED!!")
        count_shot += 1
    else:
        if shoot == keeper:
            print(f"The striker shoots to the {shoot.upper()}")
            time.sleep(2)
            print(f"The goalkeeper dives to the {keeper.upper()}. SAVED!!")
            count_shot += 1
        else:
            print(f"The striker shoots to the {shoot.upper()}")
            time.sleep(2)
            print(f"The goalkeeper dives to the {keeper.upper()}. GOAL!!")
            if team == 0:  # Add the score for a specific team
                score_A += 1
            else:
                score_B += 1
            count_shot += 1
    # Switch teams
    team += 1
    team = team % 2
    # Update the attempt
    if team == 0:
        attempt += 1
    # Maximum shot per team is 5, so it is 10 in total
    if count_shot == 10:
        game_over = True

# Display the result
print("======================================")
print("Result:")
print(f"Team A {score_A} - {score_B} Team B")
if score_A > score_B:
    print("Team A wins!!")
elif score_A < score_B:
    print("Team B wins!!")
else:
    print("Draw!!")
print("======================================")
