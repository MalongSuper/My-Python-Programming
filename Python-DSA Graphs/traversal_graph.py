# Traverse a graph using Depth-First Search (DFS) and Breadth-First Search (BFS)
# Reference: https://favtutor.com/blogs/breadth-first-search-python
# https://favtutor.com/blogs/depth-first-search-python
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


def depth_first_search(visited_list, graph, node):  # Apply Recursion for DFS
    if node not in visited_list:
        print(node)
        visited_list.add(node)  # Add the node to the visited list
        for n in graph[node]:
            # Move to the neighboring vertices
            depth_first_search(visited_list, graph, n)


def breadth_first_search(visited_list, graph, node):
    queue = []  # Initialize the queue
    visited_list.append(node)
    queue.append(node)
    # Iterate each node in the queue
    while queue:
        value = queue.pop(0)
        print(value, end=" ")
        for n in graph[value]:
            if n not in visited_list:
                visited_list.append(n)
                queue.append(n)


def main():
    print("Graph Traversal - Depth First Search (DFS) "
          "and Breadth First Search (BFS)")
    v = int(input("Enter the number of vertices: "))
    # to keep track of the visited nodes
    adj_list = adjacency_list(adjacency_matrix(v))
    # Display the result as stack
    print("Depth-First Search:")
    visited_list1 = set()  # The visited list (as set)
    depth_first_search(visited_list1, adj_list, list(adj_list.keys())[0])
    visited_list2 = []  # The visited list (as list) and queue
    print("Breadth-First Search:")
    breadth_first_search(visited_list2, adj_list, list(adj_list.keys())[0])


main()
