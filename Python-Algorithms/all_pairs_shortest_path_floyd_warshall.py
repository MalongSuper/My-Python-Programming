# This program solves All Pairs Shortest Path
# Using Floyd-Warshall Algorithm
import numpy as np


def floyd_warshall_algorithm(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Check if there exists shorter path in vertex k
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph


def main():
    # Initialize the table A0
    infinity = float('inf')
    A = np.array([[0, 3, infinity, 7],
                   [8, 0, 2, infinity],
                   [5, infinity, 0, 1],
                   [2, infinity, infinity, 0]])
    solution = floyd_warshall_algorithm(A)
    print(solution)


main()
