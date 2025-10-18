# Insertion and Deletion of Vertex in Graph
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


def insert_vertex_from_matrix(M, v):
    # Insert the row and column of the removed vertex
    result_matrix = np.insert(np.insert(M, v, 0, axis=0), v, 0, axis=1)
    return result_matrix


def delete_vertex_from_matrix(M, v):
    # Delete the row and column of the removed vertex
    result_matrix = np.delete(np.delete(M, v, axis=0), v, axis=1)
    return result_matrix


def delete_vertex_from_adj_list(adj_list, v):
    # Remove the head node of that vertex from the adjacency list
    adj_list.pop(v)
    for key in adj_list:  # Delete the vertex from the list
        if v in adj_list[key]:
            adj_list[key].remove(v)
    return adj_list


def main():
    print("Insertion and Deletion of Vertex in Graph")
    v = int(input("Enter the number of vertices: "))
    # The initial matrix
    matrix = adjacency_matrix(v)
    print(f"Adjacency Matrix of order {v}:\n {matrix}")
    adj_list = adjacency_list(matrix)
    print(f"Adjacency List: {adj_list}")
    # Deletion of vertex
    vertex1 = random.randint(0, len(matrix) - 1)
    matrix1 = delete_vertex_from_matrix(matrix, vertex1)
    print(f"\nAdjacency Matrix after deletion of vertex {vertex1}:\n {matrix1}")
    adj_list1 = delete_vertex_from_adj_list(adj_list, vertex1)
    print(f"Adjacency List after deletion of vertex {vertex1}:\n {adj_list1}")
    # Insertion of vertex
    vertex2 = random.randint(0, len(matrix) - 1)
    matrix2 = insert_vertex_from_matrix(matrix, vertex2)
    print(f"\nAdjacency Matrix after insertion of vertex {vertex2}:\n {matrix2}")
    adj_list2 = adjacency_list(matrix2)
    print(f"Adjacency List after insertion of vertex {vertex2}:\n {adj_list2}")
    # Insert new edge
    i, j = eval(input("Enter new edge for i, j: "))
    insert_edge(matrix2, i, j)
    print(f"Adjacency Matrix after insertion of edge {i}, {j}:\n {matrix2}")
    adj_list3 = adjacency_list(matrix2)
    print(f"Adjacency List: {adj_list3}")


main()
