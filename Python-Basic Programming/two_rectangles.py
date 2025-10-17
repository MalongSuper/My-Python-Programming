# This program determines whether two rectangles overlap or are inside each other
# Input the values
X1, Y1, W1, H1 = eval(input("Enter r1's center x-, y-coordinates, width, and height:\n"))
X2, Y2, W2, H2 = eval(input("Enter r2's center x-, y-coordinates, width, and height:\n"))
# Determine if Rectangle 2 is inside Rectangle 1
if (((X1 + W1) > (X2 + W2)) and ((X1 - W1) < (X2 - W2))
        and ((Y1 + H1) > (Y2 + H2)) and ((Y1 - H1) < (Y2 - H2))):
    print("r2 is inside r1")
# Determine if Rectangle 2 overlaps Rectangle 1
elif ((X1 + W1) < (X2 + W2)) and (X1 + W1) > (X2 - W2):
    print("r2 overlaps r1")
elif ((X1 + W1) > (X2 + W2)) and ((X1 + W1) < (X2 - W2)):
    print("r2 overlaps r1")
elif ((Y1 + H1) < (Y2 + H2)) and ((Y1 + H1) > (Y2 - H2)):
    print("r2 overlaps r1")
elif ((Y1 + H1) > (Y2 + H2)) and ((Y1 + H1) < (Y2 - H2)):
    print("r2 overlaps r1")
else:
    print("r2 does not overlap r1")
