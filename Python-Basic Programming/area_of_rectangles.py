# This program will measure the areas of two rectangles and then compare them
# Input the first rectangle
Length1 = float(input("Enter the length of Rectangle A :"))
Width1 = float(input("Enter the width of Rectangle A :"))
# Input the second rectangle
Length2 = float(input("Enter the length of Rectangle B :"))
Width2 = float(input("Enter the width of Rectangle B :"))
if (Length1 < 0) or (Length2 < 0) or (Width1 < 0) or (Width2 < 0):
    print("Error: The length and the width cannot be negative. "
          "Please proceed and try again")
else:
    # Calculate the two rectangles
    RectangleA = Length1 * Width1
    RectangleB = Length2 * Width2
    # Display the results of the two rectangles
    print("The area of Rectangle A :",RectangleA)
    print("The area of Rectangle B :",RectangleB)
    # Compare the two rectangles
    if RectangleA > RectangleB:
        print("Rectangle A has the greater area")
    else:
        if RectangleA < RectangleB:
            print("Rectangle B has the greater area")
        else:
            if RectangleA == RectangleB:
                print("Both the rectangles have the same areas")

