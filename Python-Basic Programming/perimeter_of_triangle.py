# This program computes the perimeter of a triangle
# Input three edges
a, b, c = eval(input("Enter three edges: "))
if (a < 0) or (b < 0) or (c < 0):
    print("Error: You cannot enter a negative number. "
          "Please proceed and try again")
else:
    # The sum of every pair of two edges must be greater than the remaining edge
    if (a + b > c) and (b + c > a) and (a + c > b):
        # Computes the three edges
        Perimeter = a + b + c
        # Display the result
        print("The perimeter is", Perimeter)
    else:
        print("The input is invalid")
