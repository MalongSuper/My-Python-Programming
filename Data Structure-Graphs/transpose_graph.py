# This program transposes a directed graph
import numpy as np


def adjacency_matrix(V):
    # Create a zero matrix of order v x v
    M = np.zeros((V, V))
    for i in range(V):
        for j in range(V):
            if i != j:  # Avoid Self-loops since they are 0s
                # If the edge exists in the graph, refer it as 1
                # Else, refer it as 0
                e = eval(input(f"+ Enter edge from {i} to {j} (1 or 0): "))
                while (e != 0) and (e != 1):
                    print("Invalid Input")
                    e = eval(input(f"+ Enter edge from {i} to {j} (1 or 0): "))
                M[i, j] = e  # Store the value in the matrix
    return M  # Return the matrix


def transpose_graph(matrix):  # Transpose the graph
    V = len(matrix)
    # Create a transpose matrix to store the entries
    transpose_matrix = np.zeros((V, V))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            # Swap the entries
            transpose_matrix[i, j] = matrix[j, i]
    return transpose_matrix


def main():
    # Input the number of vertices
    print("Transpose Graph")
    v = int(input("Enter the number of vertices: "))
    # Display the result
    matrix = adjacency_matrix(v)
    print(f"Adjacency Matrix of order {v}:\n {matrix}")
    transpose_matrix = transpose_graph(matrix)
    print(f"Transpose Adjacency Matrix:\n {transpose_matrix}")


main()
