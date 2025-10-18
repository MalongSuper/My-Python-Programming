# Prim's Algorithm for graph
import numpy as np


def adjacency_matrix(V):  # Create an adjacency matrix for a weighted graph
    # Create a zero matrix of order V x V
    M = np.zeros((V, V))
    for i in range(V):
        for j in range(V):
            if i < j:
                # If the edge exists in the graph, refer it as the cost value
                # Else, refer it as 0
                e = eval(input(f"+ Enter edge from {i} to {j}: "))
                M[i, j] = e  # Store the value in the matrix
                # Since it is symmetrical, we can assign matrix[j, i]
                # with the value stored in matrix[i, j]
                M[j, i] = M[i, j]
    return M  # Return the matrix


def prim_algorithm(V, matrix):
    # Initializing structures
    key = [float('inf')] * V  # The minimum weight edge to connect a vertex to the MST
    parent = [-1] * V  # Array to store the constructed MST
    in_mst = [False] * V  # Keep track of vertices included in MST
    key[0] = 0  # Start with vertex 0
    for _ in range(V):
        # Find the vertex with the minimum key value that is not yet included in MST
        u = min((key[i], i) for i in range(V) if not in_mst[i])[1]
        in_mst[u] = True  # Include u in MST
        # Update the key value and parent for the adjacent vertices
        for v in range(V):
            if matrix[u][v] != 0 and not in_mst[v] and matrix[u][v] < key[v]:
                key[v] = matrix[u][v]
                parent[v] = u
    mst_edges = []
    mst_weight = 0
    # Collect edges in the MST
    for i in range(1, V):
        if parent[i] != -1:
            mst_edges.append((parent[i], i, matrix[parent[i]][i]))
            mst_weight += matrix[parent[i]][i]
    return mst_edges, mst_weight


def main():
    # Input the number of vertices
    print("Graph represented by Adjacency Matrix and Prim's Algorithm for MST")
    v = int(input("Enter the number of vertices: "))
    # Create the adjacency matrix
    matrix = adjacency_matrix(v)
    print(f"Adjacency Matrix of order {v}:\n {matrix}")
    # Apply Prim's Algorithm
    mst_edges, mst_weight = prim_algorithm(v, matrix)
    # Output the MST
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst_edges:
        print(f"Edge ({u}, {v}) with weight {weight}")
    print(f"Total weight of MST: {mst_weight}")


main()
