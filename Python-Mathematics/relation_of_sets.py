# This program checks if a relation in set X
# That are reflexive, symmetric, antisymmetric and transitive
# For example: We have {1, 2, 3}
# ==> Set of order pairs:
# {(1, 1), (1, 2), (1,3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)}
# Then, we select sub-pairs in among these pairs (which is the relation)
# and determine its properties

def get_all_order_pairs(set_items):
    n = len(set_items)
    order_pairs = set()  # Initialize
    for i in range(n):
        for j in range(n):
            order_pairs.add((int(set_items[i]), int(set_items[j])))
    return order_pairs


def get_sub_order_pairs(number, set_items):
    # Get subsets of ordered pairs by the user
    # This is the relation that will be considered
    order_pair_sets = get_all_order_pairs(set_items)
    sub_set = set()  # Initialize
    for i in range(number):
        while True:
            sub = input(f"Enter pair {i + 1}: ").split(",")
            sub_S = tuple(int(s) for s in sub)  # Convert to tuple
            if sub_S in order_pair_sets:
                sub_set.add(sub_S)  # Add the tuples to the set
                break  # Exit the while loop
            else:
                print("The pair does not exist in the set")
    return sub_set  # Return the relation (set of tuples)


def check_reflexive(order_pairs, relation_set):  # Check for reflexive
    # The relation is reflexive when there exists all pairs (a, b)
    # With a = b {note that a, b must be in set X} => pair (a, a)
    for i in order_pairs:
        # If there is any missing value (a, a) in the relation
        if i[0] == i[1] and i not in relation_set:
            return False
    return True


def check_symmetric(relation_set):  # Check for symmetric
    # The relation is symmetric when: if there exists pair (a, b)
    # there exists a pair (b, a) {note that a, b must be in set X}
    for i in relation_set:
        # If the reverse of the tuple does not exist in the relation
        if i[::-1] not in relation_set:
            return False
    return True


def check_antisymmetric(relation_set):  # Check for antisymmetric
    # The relation is antisymmetric when there does not exist
    # any pair (a, b) and (b, a) with a ≠ b
    # {note that a, b must be in set X}
    for i in relation_set:
        # If the reverse of the tuple exists in the relation
        # And no pair (a, a) exists in the relation
        if i[::-1] in relation_set and i[0] != i[1]:
            return False
    return True


def check_transitive(relation_set):  # Check for transitive
    # The relation is transitive when: if there exists pair (a, b) and (b, c)
    # there exists a pair (a, c) {note that a, b must be in set X}
    for i in relation_set:
        for j in relation_set:
            # If there exists two pairs
            # that the index 0 of pair 1 == index 1 of pair 2
            # And there does not exist the transitive pair in the relation
            if i[1] == j[0] and (i[0], j[1]) not in relation_set:
                return False
    return True


def main():
    print("Relation Properties")
    S = input("Enter set: ").split(",")
    order_pair_sets = get_all_order_pairs(S)
    number = int(input("Enter the length of the subset: "))
    relation = get_sub_order_pairs(number, S)
    print("Relation:", relation)
    print("- Reflexive:", check_reflexive(order_pair_sets, relation))
    print("- Symmetric:", check_symmetric(relation))
    print("- Antisymmetric:", check_antisymmetric(relation))
    print("- Transitive:", check_transitive(relation))


# Avoid running the main function
# when importing the 'module' to another program
if __name__ == "__main__":
    main()
