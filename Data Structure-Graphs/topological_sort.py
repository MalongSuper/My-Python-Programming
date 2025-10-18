# Implement Basic Graph - Topological Sort
# Reference: https://www.youtube.com/watch?v=00Al-jAIiYk
from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def insert_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        in_degree = [0] * self.v
        # in_degree for all the vertices
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1
        # Select vertices with in_degree 0
        queue = []
        for i in range(self.v):
            if in_degree[i] == 0:
                queue.append(i)
        cycle = 0
        # Display result
        sequence = []
        while queue:
            x = queue.pop()
            sequence.append(x)  # Added x in the result
            for vertex in self.graph[x]:  # All the adjacent vertices of x
                in_degree[vertex] -= 1  # Remove x, now it has lost the connection with x
                if in_degree[vertex] == 0:
                    queue.append(vertex)
            cycle += 1
        # Check for cycle
        if cycle != self.v:
            print("Graph contains a cycle. Topological Sort is not possible")
            return
        print("The resultant sequence:", sequence)


def main():
    print("Topological Sort")
    v = int(input("Enter the number of vertices: "))
    graph = Graph(v)
    for i in range(v):
        for j in range(v):
            if i != j:
                # Prompt user for edge existence between vertex i and vertex j
                e = int(input(f"Enter edge from {i} to {j} (0 or 1): "))
                if e == 1:
                    graph.insert_edge(i, j)
    graph.topological_sort()


main()
