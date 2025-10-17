# This program displays a pyramid
print("Display a pyramid")
Number = int(input("Enter the number of lines: "))
if Number < 0:
    print("Error: Cannot display a pyramid with the input number. "
          "Please proceed and try again")
else:
    for P in range(1, Number + 1):
        for S in range(Number, P, -1):
            print(" ", end=" ")
        for S in range(P, 0, -1):  # Left side pyramid
            print(S, end=" ")
        for S in range(2, P + 1):  # Right side pyramid
            print(S, end=" ")
        print()
