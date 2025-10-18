# Insertion and Deletion of Edge in Graph
# Using adjacency list and adjacency matrix
import numpy as np
import random


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


def insert_edge(M, i, j):  # Insert an edge in the matrix
    M[i, j] = 1
    M[j, i] = 1  # For undirected graph


def delete_edge(M, i, j):  # Delete an edge in the matrix
    M[i, j] = 0
    M[j, i] = 0  # For undirected graph


def main():
    print("Insertion and Deletion of Edge in Graph")
    v = int(input("Enter the number of vertices: "))
    # The initial matrix
    matrix = adjacency_matrix(v)
    print(f"Adjacency Matrix of order {v}:\n {matrix}")
    adj_list = adjacency_list(matrix)
    print(f"Adjacency List: {adj_list}")
    # Insertion of edge
    row_insert, column_insert = [], []
    for i1 in range(len(matrix)):
        for j1 in range(len(matrix)):
            if matrix[i1, j1] == 0:
                row_insert.append(i1)
                column_insert.append(j1)
    # Randomize an entry with 0 and turn it to 1
    i1, j1 = random.choice(row_insert), random.choice(column_insert)
    insert_edge(matrix, i1, j1)
    print(f"\nAdjacency Matrix after insertion of edge ({i1}, {j1}):\n {matrix}")
    adj_list1 = adjacency_list(matrix)
    print(f"Adjacency List: {adj_list1}")
    # Deletion of edge
    row_delete, column_delete = [], []
    for i2 in range(len(matrix)):
        for j2 in range(len(matrix)):
            if matrix[i2, j2] == 1:
                row_delete.append(i2)
                column_delete.append(j2)
    # Randomize an entry with 1 and turn it to 0
    i2, j2 = random.choice(row_delete), random.choice(column_delete)
    delete_edge(matrix, i2, j2)
    print(f"\nAdjacency Matrix after deletion of edge ({i2}, {j2}):\n {matrix}")
    adj_list2 = adjacency_list(matrix)
    print(f"Adjacency List: {adj_list2}")


main()
