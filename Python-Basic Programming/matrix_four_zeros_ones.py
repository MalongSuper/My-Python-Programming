# This program displays the 4x4 matrix with only 0s and 1s
# Then find the rows and columns with the most 1s
import random


def print_number(n):  # Define function
    matrix = []
    # The line of the matrix depends on the number
    for _ in range(n):
        # Display the number
        row = [random.randint(0, 1) for _ in range(n)]
        matrix.append(row)
        print(' '.join(map(str, row)))
    return matrix


def find_rows_columns(m):  # Define function to find the rows and columns with the most 1s
    # Count the 1s of every row and column
    count_rows = [rows.count(1) for rows in m]
    count_columns = [columns.count(1) for columns in zip(*m)]
    # Find the maximum count of 1s
    max_count_rows = max(count_rows)
    max_count_columns = max(count_columns)
    # Create a list of most rows and columns
    most_rows = [row for row, count in enumerate(count_rows) if count == max_count_rows]
    most_columns = [col for col, count in enumerate(count_columns) if count == max_count_columns]
    # Display the indexes of rows and columns
    return most_rows, most_columns


def main():  # Define main function
    print("Largest Rows and Columns of Matrix")
    n = 4
    matrix = print_number(n)
    most_rows, most_columns = find_rows_columns(matrix)
    print("The largest row index:", ', '.join(map(str, most_rows)))
    print("The largest column index:", ', '.join(map(str, most_columns)))


# Display the result
main()
