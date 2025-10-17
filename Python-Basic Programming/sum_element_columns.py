# This program displays the sum of a column in a matrix
def sum_column(column_index):  # Define function to return the sum of columns
    sum_of_the_column = sum(column_index)
    return sum_of_the_column


def main():  # Define main function
    print("Sum elements column by column")
    a0, b0, c0, d0 = eval(input("Enter a 3-by-4 matrix row for row 0: "))
    a1, b1, c1, d1 = eval(input("Enter a 3-by-4 matrix row for row 1: "))
    a2, b2, c2, d2 = eval(input("Enter a 3-by-4 matrix row for row 2: "))
    # Make a matrix
    matrix = [[a0, b0, c0, d0], [a1, b1, c1, d1], [a2, b2, c2, d2]]
    # Make a list contain the values of every column
    column0 = [matrix[0][0], matrix[1][0], matrix[2][0]]
    print("Sum of the elements for column 0 is", end=" ")
    print(sum_column(column0))
    column1 = [matrix[0][1], matrix[1][1], matrix[2][1]]
    print("Sum of the elements for column 1 is", end=" ")
    print(sum_column(column1))
    column2 = [matrix[0][2], matrix[1][2], matrix[2][2]]
    print("Sum of the elements for column 2 is", end=" ")
    print(sum_column(column2))
    column3 = [matrix[0][3], matrix[1][3], matrix[2][3]]
    print("Sum of the elements for column 3 is", end=" ")
    print(sum_column(column3))


# Display the result
main()
