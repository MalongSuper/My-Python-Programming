# This program displays the sum of major diagonal
def sum_major_diagonal(major_diagonal):  # Define function to return the sum of the major diagonal
    sum_of_major_diagonal = sum(major_diagonal)
    return sum_of_major_diagonal


def main():  # Define main function
    print("Sum of the Major Diagonal")
    a0, b0, c0, d0 = eval(input("Enter a 4-by-4 matrix row for row 1: "))
    a1, b1, c1, d1 = eval(input("Enter a 4-by-4 matrix row for row 2: "))
    a2, b2, c2, d2 = eval(input("Enter a 4-by-4 matrix row for row 3: "))
    a3, b3, c3, d3 = eval(input("Enter a 4-by-4 matrix row for row 4: "))
    matrix = [[a0, b0, c0, d0], [a1, b1, c1, d1], [a2, b2, c2, d2], [a3, b3, c3, d3]]
    # Determine the major diagonal from the top left to bottom right
    major_diagonal = [matrix[0][0], matrix[1][1], matrix[2][2], matrix[3][3]]
    print("The sum of the elements in the major diagonal is", end=" ")
    print(sum_major_diagonal(major_diagonal))


main()
