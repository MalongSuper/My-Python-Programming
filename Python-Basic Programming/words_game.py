# This program plays word game
import string
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


def main():
    used_words = set()  # Keep track of the already used word
    dictionary = dictionaries("Txt Files/Words.txt")
    selected_letter = random.choice(string.ascii_uppercase)
    letter = selected_letter.lower()
    print("Welcome to Word Game!")
    print("Rules:\n+ A random letter will be selected\n+ Then, you must enter a word that contains that letter\n"
          "+ You win $2.500 if you make it to 100 words")
    print("+ However, if you enter...")
    print(" * A duplicate word\n * A word that is not meaningful\n * A word that does not contain the letter")
    print("+ You will lose, the number of words you answered is the prize you get")
    time.sleep(3)
    print("Let's get started!!")
    print(f"Your letter is {selected_letter}")
    # Play word game
    count = 0
    prize = 0
    for i in range(1, 101):
        input_word = input(f"{i}. Enter a word: ")
        word = input_word.lower()  # Put the word in lowercase for consideration
        if word in used_words:
            print("================================")
            print("=> Duplicate Word\nYou Lose!!")
            break
        elif letter not in word:
            print("================================")
            print("=> Invalid Word\nYou Lose!!")
            break
        elif word not in dictionary:
            print("================================")
            print("=> Not Meaningful Word\nYou Lose!!")
            break
        else:
            # Increase the number of correct words and prize money
            count += 1
            prize += 25
        # Save the input word to the set
        used_words.add(word)
    # Display the result
    print(f"Number of words {count} / 100")
    if prize == 2500:
        print(f"Earned: $2500")
        print("Congratulations!! You won!!")
    else:
        print(f"Earned: ${prize}")
    print("================================")


main()
