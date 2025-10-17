# Draw Tic-Tac-Toe board (m x n) --> Row x Column
print("Draw Tic-Tac-Toe Board")
n = int(input("Enter column: "))
m = int(input("Enter row: "))
if n not in range(1, 10) or m not in range(1, 10):
    print("Invalid Input. Please restart the program")
else:
    for i in range(1, n + 1):
        print("\t", i, end=" ")
    print()
    for j in range(1, m + 2):
        if j != 1:
            print(j - 1, end=" ")
            for e in range(1, n + 2):
                print("\t|", end=" ")
            print()
        for k in range(n + 1):
            if k == 0:  # A blank line
                print("    ", end="")
            else:
                print("+---", end="")
        print("+")
