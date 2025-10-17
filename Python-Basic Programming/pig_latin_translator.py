# Translate a word to Pig Latin
from string import punctuation
# Input the string and lowercase it
print("Word to Pig Latin")
string = str(input("Enter a string: ")).split()
string = [s.lower() for s in string]
# Create the list of consonants
special_case = ["wh", "sh", "ch", "ph",
                "gl", "bl", "sl", "cl", "pl", "fl",
                "ch", "ph", "gh", "th", "sh", "tr",
                "br", "fr", "gr", "cr", "st", "sk"]
for sub_string in string:
    # Check if the first character is a vowel
    if sub_string[0] in ["a", "e", "i", "o", "u"]:
        sub_string = list(sub_string)  # Convert to list
        sub_string.append("yay")  # Add "yay" after the string
    # Check if the string contains "special cases" above
    elif sub_string[:2] in special_case:
        sub_string = list(sub_string)  # Convert to list
        # Move the two first characters to the last position
        first_char, second_char = sub_string[0], sub_string[1]
        sub_string.pop(0)
        sub_string.pop(0)
        sub_string.append(first_char)
        sub_string.append(second_char)
        sub_string.append("ay")  # Add "ay" to the end
    else:
        sub_string = list(sub_string)  # Convert to list
        # Move the first character to the last position
        first_char = sub_string[0]
        sub_string.pop(0)
        sub_string.append(first_char)
        sub_string.append("ay")  # Add "ay" to the end
    # Display the result
    print("".join(sub_string), end=" ")
print()
