# This program checks whether a number is divisible by 5 or 6
# Input an integer
Integer = int(input("Enter an integer: "))
# Check if the number is divisible by both 5 and 6
print("Is", Integer, "divisible by 5 and 6?", end=" ")
if (Integer % 5) == 0 and (Integer % 6) == 0:
    print("True")
else:
    print("False")
# Check if the number is divisible by either 5 or 6
print("Is", Integer, "divisible by 5 or 6?", end=" ")
if (Integer % 5) == 0 or (Integer % 6) == 0:
    print("True")
else:
    print("False")
# Check if the number is divisible by either 5 or 6, but not both
print("Is", Integer, "divisible by 5 or 6, but not both?", end=" ")
if (((Integer % 5) == 0 and (Integer % 6) != 0)
        or ((Integer % 5) != 0 and (Integer % 6) == 0)):
    print("True")
else:
    print("False")
