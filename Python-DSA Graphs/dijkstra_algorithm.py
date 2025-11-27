# Dijkstra Algorithm using SciPy
import sys
import numpy as np
from scipy.sparse import csr_matrix


def dijkstra(graph_sparse, source=0):
    """
    Compute the shortest paths from source to all vertices using Dijkstra
    on a sparse adjacency matrix (CSR).

    Parameters:
        graph_sparse: csr_matrix
            Sparse adjacency matrix with weights (0 means no edge)
        source: int
            Index of the source vertex

    Returns:
        distances: list of shortest distances from source
    """
    num_of_vertices = graph_sparse.shape[0]
    visited = np.zeros(num_of_vertices, dtype=bool)
    distances = np.full(num_of_vertices, sys.maxsize)
    distances[source] = 0

    for _ in range(num_of_vertices):
        # Pick the unvisited vertex with the smallest distance
        unvisited_indices = np.where(~visited)[0]
        if len(unvisited_indices) == 0:
            break
        current = unvisited_indices[np.argmin(distances[unvisited_indices])]
        visited[current] = True

        # Get neighbors (non-zero entries)
        start_ptr = graph_sparse.indptr[current]
        end_ptr = graph_sparse.indptr[current + 1]
        neighbors = graph_sparse.indices[start_ptr:end_ptr]
        weights = graph_sparse.data[start_ptr:end_ptr]

        # Update distances
        for neighbor, weight in zip(neighbors, weights):
            if not visited[neighbor]:
                new_distance = distances[current] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances


def main():
    # Example usage
    array = np.array([
        [0, 4, 5, 0, 0, 0],
        [4, 0, 11, 9, 7, 0],
        [5, 11, 0, 0, 3, 0],
        [0, 9, 0, 0, 13, 2],
        [0, 7, 3, 13, 0, 6],
        [0, 0, 0, 2, 6, 0]
    ])
    graph_sparse = csr_matrix(array)

    n = len(array)
    adjacency_matrix = np.zeros(shape=(n, n))

    for i in range(n):
        print(f"Vertex {i}:")
        distances = dijkstra(graph_sparse, source=i)
        for k, d in enumerate(distances):
            print(f"- Distance from vertex {i} to vertex {k}: {d}")
            adjacency_matrix[i, k] = d
    print("\nAdjacency Matrix:\n", adjacency_matrix)


main()
