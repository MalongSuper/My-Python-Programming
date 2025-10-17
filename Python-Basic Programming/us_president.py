# This program prompts the user to enter a number
# And display a US President
# The presidents list are in a txt file
with open("Txt Files/USPresident.txt", "r") as file:
    lines = file.readlines()  # Read lines

print("US Presidents")
number = int(input("Enter a number: "))
if number > 46 or number <= 0:
    print("Error: No president found")
else:
    print(lines[number - 1])
