# This program revises flipping coin game and calculate number of Heads and Tails
import random
Count_Heads = 0
Count_Tails = 0
# The time is one million
for Time in range(1, 1000001):
    # Randomly generated Heads or Tails
    Coin_Value = ('Heads', 'Tails')
    Coin = random.choice(Coin_Value)
    # Display the result
    print(f'{Time}\t\t\t{Coin}')
    # Calculate the number of Heads and Tails
    if Coin == 'Heads':
        Count_Heads += 1
    if Coin == 'Tails':
        Count_Tails += 1
# Display the result
print("Game: Flipping Coins for one million times")
print("The number of Heads: ", Count_Heads)
print("The number of Tails: ", Count_Tails)
