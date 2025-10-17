# Multiplication Table
number = int(input("Enter table's size (0-9): "))
if number not in range(1, 9):
    number = 9
print("\t\tMULTIPLICATION TABLE")
print("* |", end=" ")
for i in range(1, number + 1):
    print(i, end="\t")
print()
print("---------------------------------------")
for j in range(1, number + 1):
    print(j, "|", end=" ")
    for k in range(1, number + 1):
        print(j * k, end=" ")
        print(end="\t")
    print()
