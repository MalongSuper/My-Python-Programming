# This program simulates picking a card game
import random
# List of a deck of 52 cards
Card_Rank = ('Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
Card_Suit = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
# Random generated the card
Random_CardRank = random.choice(Card_Rank)
Random_CardSuit = random.choice(Card_Suit)
# Display the result
print("Random Card Generator")
print("The card you picked is the " + str(Random_CardRank) + " of " + str(Random_CardSuit))
