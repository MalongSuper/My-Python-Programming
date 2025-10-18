# Implements Graph using an adjacency matrix
import numpy as np


def adjacency_matrix(V):
    # Create a zero matrix of order v x v
    M = np.zeros((V, V))
    for i in range(V):
        for j in range(V):
            if i < j:
                # If the edge exists in the graph, refer it as 1
                # Else, refer it as 0
                e = eval(input(f"+ Enter edge from {i} to {j} (1 or 0): "))
                while (e != 0) and (e != 1):
                    print("Invalid Input")
                    e = eval(input(f"+ Enter edge from {i} to {j} (1 or 0): "))
                M[i, j] = e  # Store the value in the matrix
                # Since it is symmetrical, we can assign matrix[j, i]
                # with the value stored in matrix[i, j]
                M[j, i] = M[i, j]
    return M  # Return the matrix


def adjacency_list(M):
    # Convert the adjacency matrix to an adjacency list
    adj_list = {}  # Each node is stored as a key of the dictionary
    for i in range(M.shape[0]):
        # A list can be created by storing the indices of
        # the corresponding row in the matrix in a list which
        # becomes the value for that particular key
        list1 = [j for j in range(M.shape[1]) if M[i, j] == 1]
        adj_list[i] = list1
    return adj_list


def is_edge_matrix(M, i, j):
    # Check if there is an edge from i to j
    # in the adjacency matrix
    if M[i, j] == 1:
        return True
    else:
        return False


def is_edge_list(adj_list, i, j):
    # Check if there is an edge from i to j
    # in the adjacency list
    if j in adj_list[i]:
        return True
    else:
        return False


def insert_edge(M, i, j):  # Insert an edge in the matrix
    M[i, j] = 1  # For directed graph


def main():
    # Input the number of vertices
    print("Graph represented by Adjacency Matrix and Adjacency List")
    v = int(input("Enter the number of vertices: "))
    # Display the result
    matrix = adjacency_matrix(v)
    print(f"Adjacency Matrix of order {v}:\n {matrix}")
    adj_list1 = adjacency_list(matrix)
    print(f"Adjacency List: {adj_list1}")
    # Insert 1 for the diagonal entries
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                insert_edge(matrix, i, j)
    print(f"\nAdjacency Matrix after insertion:\n {matrix}")
    adj_list2 = adjacency_list(matrix)
    print(f"Adjacency List after insertion: {adj_list2}")


main()
