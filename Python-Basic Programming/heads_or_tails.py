# This program simulates Heads or Tails game
# The integer 0 or 1 represents Heads or Tails
import random
Heads_or_Tails = random.randint(0, 1)
print("Heads or Tails Game Simulation")
Guess = str(input("Heads or Tails ? "))
if (Guess != 'Heads') and (Guess != 'Tails'):
    print("Error: Invalid value")
else:
    # Make a List
    List = {0: 'Heads', 1: 'Tails'}
    # If the user guesses Head
    if Guess == 'Heads':
        if Guess == List.get(Heads_or_Tails):
            print("The program has generated:", Heads_or_Tails, "for", List.get(Heads_or_Tails))
            print("Your Guess is Correct")
        else:
            print("The program has generated:", Heads_or_Tails, "for", List.get(Heads_or_Tails))
            print("Your Guess is Incorrect")
    # If the user guesses Tail
    if Guess == 'Tails':
        if Guess == List.get(Heads_or_Tails):
            print("The program has generated:", Heads_or_Tails, "for", List.get(Heads_or_Tails))
            print("Your Guess is Correct")
        else:
            print("The program has generated:", Heads_or_Tails, "for", List.get(Heads_or_Tails))
            print("Your Guess is Incorrect")
