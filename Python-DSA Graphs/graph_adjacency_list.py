# Graph using Adjacency List
# Reference: https://www.geeksforgeeks.org/graph-and-its-representations/


def add_edge(adj, i, j):
    adj[i].append(j)
    adj[j].append(i)  # For an undirected graph


def adj_list(adj):  # Display the adjacency list
    for i in range(len(adj)):
        print(f"Vertex {i}: ", end="")
        for j in adj[i]:
            print(j, end=" -> ")
        print("None")


def main():
    # Create a graph with input vertices and no edges
    vertices = int(input("Enter the number of vertices: "))
    adj = [[] for _ in range(vertices)]
    # Now add edges one by one
    for n in range(vertices):
        i, j = eval(input(f"{n + 1}. Enter pair of vertices i, j: "))
        add_edge(adj, i, j)
    print("Adjacency List Representation:")
    adj_list(adj)


main()
