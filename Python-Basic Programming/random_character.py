# This program generates a random uppercase letter
# In Ascii Code is between 65 and 90
import random
# Randomized a number from 65 to 90
Random_Number = random.randint(65, 90)
# Convert the number to string in Ascii Code
# Display the result
print("Random Uppercase Letter Generator")
print("The uppercase letter is", chr(Random_Number))
