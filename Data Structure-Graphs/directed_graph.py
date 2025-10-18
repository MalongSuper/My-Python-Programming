# Implements Graph using an adjacency matrix - directed Graph
# The matrix for a directed graph might not be symmetrical
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


def main():
    # Input the number of vertices
    print("Directed Graph represented by Adjacency Matrix")
    v = int(input("Enter the number of vertices: "))
    # Display the result
    matrix = adjacency_matrix(v)
    print(f"Adjacency Matrix of order {v}:\n {matrix}")


main()
