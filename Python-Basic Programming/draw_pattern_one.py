# This program uses nested loops to draw a specific pattern
for P in range(7, 0, -1):
    for S in range(P):
        print("*", end="")
    print("")