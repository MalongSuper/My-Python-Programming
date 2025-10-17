# This program calculates the multiplication of two matrices
def multiply_matrix(a, b):  # Define function to multiply the matrices
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # Use loop to iterate the row of matrix a
    for i in range(len(a)):
        # Use loop to iterate the column of matrix b
        for j in range(len(b[0])):
            # Use loop to iterate the row of matrix b
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result


def main():
    print("Multiply two matrices")
    a11, a12, a13, a21, a22, a23, a31, a32, a33 = eval(input("Enter Matrix 1: "))
    b11, b12, b13, b21, b22, b23, b31, b32, b33 = eval(input("Enter Matrix 2: "))
    a = [[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]]
    b = [[b11, b12, b13], [b21, b22, b23], [b31, b32, b33]]
    print("The multiplication of the two matrices:")
    print("Matrix 1\t\tMatrix 2\t\t\tResult")
    result = multiply_matrix(a, b)
    for matrix_a, matrix_b, res in zip(a, b, result):
        print(f'{matrix_a}\t\t{matrix_b}\t\t\t{res}')


# Display the result
main()
