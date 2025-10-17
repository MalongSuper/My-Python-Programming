# This program plays Word Crush Game
# The objective is to simply find the words that its first letter
# matches with the last letter of the previous word
# The game will be played with User vs Computer
import random
import time


def dictionaries(filename):  # Load a dictionary for the game
    try:
        with open(filename, 'r') as file:
            # Read the file and create a set of words, stripping whitespace
            words = {line.strip().lower() for line in file if line.strip()}
        return words
    except FileNotFoundError:
        print("File not found")


def valid_computer_word(available_words, last_letter):  # Computer's logic for words selection
    # Select a random from the available words that starts with the given letter
    possible_words = [word for word in available_words if word.startswith(last_letter)]
    if possible_words:  # The possible words are found
        return random.choice(possible_words)  # Randomly select one of the possible words
    return None


def is_valid_word(word, used_words, dictionary):  # Check if the user's word is valid
    if word not in dictionary:
        return False
    if word in used_words:
        return False
    return True


def main():
    print("Welcome to Word Crush Game!")
    print("Rules:\n+ Computer will select a word\n+ Then, you must enter a word "
          "that contains the last letter of the computer's word as the first letter")
    print("+ The computer must also follow the same rule")
    print("+ The player immediately loses when entering an invalid word")
    print("+ The maximum of 50 turns (25 rounds)")
    time.sleep(3)
    print("Let's get started!!")
    used_words = set()  # Keep track of the already used word
    dictionary = dictionaries("Txt Files/Words.txt")
    player_turn = False  # This means that the computer will start first
    current_round, max_rounds = 0, 25
    last_letter = ''  # Initialize the last letter
    # The iteration resumes when the current turn
    # has not reached the max turn
    while current_round < max_rounds:
        print(f"Round {current_round + 1} / {max_rounds}")
        for turn in range(2):  # Each round has two turns
            # The user's turn
            if player_turn:
                player_word = str(input("(Player) Enter a word: "))
                word = player_word.lower()  # Put the word in lowercase for consideration
                # The word is not alphabetical (contains special symbols)
                if not word.isalpha():
                    print("The word is invalid. You Lose!!")
                    return
                # If the word is either already used or not in the dictionary
                if not is_valid_word(player_word, used_words, dictionary):
                    print("The word is already used or not meaningful. You Lose!!")
                    return
                # If the first letter of the word
                # is not the last letter of the computer's word
                if last_letter and player_word[0] != last_letter:
                    print(f"The word does not start with '{last_letter}'. You Lose!!")
                    return
                # Save the input word to the set
                used_words.add(player_word)
                last_letter = player_word[-1]  # Get the last letter of the word
            else:
                # Starts with the computer
                # Make sure the computer does not select an already used word
                computer_word = valid_computer_word(dictionary - used_words, last_letter)
                if computer_word is not None:  # If the computer has a word to play
                    print(f"(Computer) Computer played: {computer_word}")
                    used_words.add(computer_word)  # Save the word to the set
                    last_letter = computer_word[-1]  # Get the last letter of the word
                else:
                    print("The computer has no word to play. You won!!")
                    return
            # Switch turn between the user and the computer
            player_turn = not player_turn
        # Update number of round
        current_round += 1
    # The loop ends when it reaches the max_round, thereby, display the result
    if current_round == max_rounds:
        print("=> Game over. It is a draw!!")
    else:  # In case the game ends early, either the player
        # Or the computer loses immediately
        print("=> Game ends early")


main()
