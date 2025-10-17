# This program displays a random uppercase letter
import time
# Using the time.time() function
Letter = time.time()
# ASCII code has 26 uppercase letters from A to Z
# The alphabet starts with A is 65 to Z is 90
Ascii_Code = (ord('A'))
# ASCII uppercase letter is between 65 and 90, so there are 25 values from A to Z
Value = round(Letter % 25)
# Combine the two functions so that the number generated will be from 65 to 90
Number = Ascii_Code + Value
# Display the results
# Convert to character using chr()
print("ASCII Code Generator")
print("-------------------------")
print("The random number is", Number)
print("The uppercase letter is", chr(Number))
