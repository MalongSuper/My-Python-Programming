# This program performs QR Decomposition with Gram-Schmidt
# Require a transpose matrix of the input matrix
# Each row is treated as a column vector.
# Reference: https://www.math.ucla.edu/~yanovsky/Teaching/Math151B/handouts/GramSchmidt.pdf
import numpy as np


def gram_schmidt(matrix):
    n = len(matrix)
    # Find e1
    a1 = matrix[0]
    u1 = a1
    u1_norm = np.sqrt(sum([u1[j] ** 2 for j in range(len(u1))]))
    e1 = (1 / u1_norm) * u1
    ei, ai = [e1], [a1]  # Initially has e1 and a1
    # Find the remaining ei
    for i in range(1, n):
        a = matrix[i]
        # Apply the formula
        u = a - sum([np.dot(np.dot(a, e), e) for e in ei])
        u_norm = np.sqrt(sum([u[j] ** 2 for j in range(len(u))]))
        e = (1 / u_norm) * u
        # Append e value, useful for the calculation
        ei.append(e)
        # Append a value, use to form the matrix later
        ai.append(a)
    # Construct Q and R
    Q = np.array(ei).T
    R = np.zeros((n, n))
    # Convert to array
    ai, ei = np.array(ai), np.array(ei)
    # Start with the first column
    for j in range(len(ei)):
        ri = [np.dot(ai[k], ei[j]) for k in range(j, len(ai))]
        ''' 
        Explain: 
            for i in range(3):
                for j in range(i, 3):
                print(i, j, end=", ") 
        Output: 0 0, 0 1, 0 2, 1 1, 1 2, 2 2, 
        Workflow:
            + The first nested loop with i = 0, return j = 0, 1, 2
            + The second nested loop with i = 1, return j = 1, 2 corresponding to for j in range(1, 3)
            + The third nested loop with i = 2, return j = 2 corresponding to for j in range(2, 3)
        '''
        # Add to the R matrix
        R[j][j:len(ei)] = ri
    # Return the final result
    return Q, R


def main():
    print("QR Decomposition with Gram-Schmidt")
    # matrix = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
    n = int(input("Enter size of the matrix: "))
    matrix = np.random.randint(0, 10, size=(n, n))
    print("Matrix A:\n", matrix)
    Q, R = gram_schmidt(matrix.T)  # Transpose the matrix
    print("Q:\n", Q)
    print("R:\n", R)
    # Compute QR and Error
    QR = np.dot(Q, R)
    print("QR:\n", QR)
    print("Error:\n", np.linalg.norm(matrix - QR))


main()
