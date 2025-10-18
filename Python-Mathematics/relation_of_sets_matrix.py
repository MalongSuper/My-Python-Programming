# This program checks if a relation in set X
# That are reflexive, symmetric, antisymmetric and transitive
# Using matrix
from relation_of_sets import get_all_order_pairs, get_sub_order_pairs
from numpy import array, zeros, dot


def get_matrix(number_set, relation):
    relation = list(relation)  # Convert the relation to list for iteration
    element_in_relation = []
    n = len(number_set)  # The matrix is obtained based on the length of the set
    rn = len(relation)  # Get the length of the relation for iteration
    matrix = zeros((n, n))  # Initialize the matrix
    for i in range(rn):  # Iterate through the list (from set) to get the tuple
        element_in_relation.append(list(relation[i]))  # Convert it to list
    for j in element_in_relation:
        matrix[j[0] - 1][j[1] - 1] = 1  # Change the corresponding index to 1
    # Return the matrix
    return matrix


def reflexive_matrix(matrix):  # Check if the matrix is reflexive
    # The relation is reflexive if in the matrix
    # all the diagonal entries are 1
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == j and matrix[i][j] != 1:
                return False
    return True


def symmetric_matrix(matrix):  # Check if the matrix is symmetric
    # The relation is reflexive if in the matrix
    # The entry ij is equivalent to entry ji, both are 1 (eij = eji = 1)
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1 and matrix[i][j] != matrix[j][i]:
                return False
    return True


def antisymmetric_matrix(matrix):  # Check if the matrix is antisymmetric
    # The relation is reflexive if in the matrix
    # the entry ij is 1 and entry ji is 0 (with i ≠ j)
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1 and matrix[j][i] != 0 and i != j:
                return False
    return True


def transitive_matrix(matrix):  # Check if the matrix is transitive
    # If the entry 1 of the matrix
    # and the entry 1 of the square of that matrix
    # are all in the same position
    matrix = array(matrix, dtype=float)
    prod_matrix = dot(matrix, matrix)
    n = len(prod_matrix)
    for i in range(n):
        for j in range(n):
            if prod_matrix[i][j] == 1 and matrix[i][j] != 1:
                return False
    return True


def main():
    print("Relation Properties (Using Matrix)")
    S = input("Enter set: ").split(",")
    number = int(input("Enter the length of the subset: "))
    relation = get_sub_order_pairs(number, S)
    matrix = get_matrix(S, relation)
    print("Matrix of Relation:\n", matrix)
    print("- Reflexive:", reflexive_matrix(matrix))
    print("- Symmetric:", symmetric_matrix(matrix))
    print("- Antisymmetric:", antisymmetric_matrix(matrix))
    print("- Transitive:", transitive_matrix(matrix))


# Avoid running the main function
# when importing the 'module' to another program
if __name__ == "__main__":
    main()
