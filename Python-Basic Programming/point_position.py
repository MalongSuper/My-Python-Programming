# This program checks the point position to other points
def left_of_the_line(x0, y0, x1, y1, x2, y2):  # Define function for left side
    position = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    if position > 0:
        return True


def on_the_same_line(x0, y0, x1, y1, x2, y2):  # Define function for same line
    position = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    if position == 0:
        return True


def on_the_line_segment(x0, y0, x1, y1, x2, y2):  # Define function for line segment(right side)
    position = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    if position < 0:
        return True


def main():  # Define main function
    print("Point Position")
    print("Enter the coordinates for the three points p0, p1, p2: ")
    x0, y0, x1, y1, x2, y2 = eval(input(""))
    if left_of_the_line(x0, y0, x1, y1, x2, y2) is True:
        print("p2 is on the left side of the line from p0 to p1")
    elif on_the_same_line(x0, y0, x1, y1, x2, y2) is True:
        print("p2 is on the same line from p0 to p1")
    elif on_the_line_segment(x0, y0, x1, y1, x2, y2) is True:
        print("p2 is on the right side of the line from p0 to p1")


# Display the result
main()
