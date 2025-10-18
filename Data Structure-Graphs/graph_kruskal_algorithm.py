# Kruskal's Algorithm for graph
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


def find(parent, u):  # Find the representative (or root) of a node
    if parent[u] != u:
        parent[u] = find(parent, parent[u])  # Path compression
    return parent[u]


def union(parent, rank, u, v):  # Unite two sets
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u != root_v:
        # Union by rank
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1


def kruskal_algorithm(V, M):  # Apply Kruskal's algorithm
    edges = []
    # Create an edge list from the adjacency matrix
    for i in range(V):
        for j in range(i + 1, V):
            if M[i][j] != 0:  # If there is an edge
                edges.append((M[i][j], i, j))
    # Sort edges by weight
    edges.sort()
    # Initialize the parent and rank for union-find
    parent = list(range(V))
    rank = [0] * V
    mst = []
    mst_weight = 0
    for weight, u, v in edges:
        # Find the roots of u and v
        if find(parent, u) != find(parent, v):
            # If they belong to different sets, add the edge to the MST
            mst.append((u, v, weight))
            mst_weight += weight
            # Union the two sets
            union(parent, rank, u, v)
    return mst, mst_weight


def main():
    # Input the number of vertices
    print("Graph represented by Adjacency Matrix and Kruskal's Algorithm for MST")
    v = int(input("Enter the number of vertices: "))
    # Create the adjacency matrix
    matrix = adjacency_matrix(v)
    print(f"Adjacency Matrix of order {v}:\n {matrix}")
    # Apply Kruskal's Algorithm
    mst, mst_weight = kruskal_algorithm(v, matrix)
    # Display the MST
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"- Edge ({u}, {v}) with weight {weight}")
    print(f"=> Total weight of MST: {mst_weight}")


main()
