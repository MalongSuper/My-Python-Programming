# This program plays rolling dice
# Add sound
import random
from playaudio import playaudio
dice_number = [1, 2, 3, 4, 5, 6]
# Rolling two dices
print("Rolling dice...")
dice1 = random.choice(dice_number)
dice2 = random.choice(dice_number)
playaudio('/Users/macbook/Documents/Audio Files/dice-142528.mp3')
print("Dice 1:", dice1)
print("Dice 2:", dice2)
print("=> Total:", dice1 + dice2)
print("=> Multiplication:", dice1 * dice2)
