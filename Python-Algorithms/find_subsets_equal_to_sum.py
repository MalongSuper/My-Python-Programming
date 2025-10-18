# This program find subsets of a given list which are equal to V
print("Find Subsets")


def find_subsets():
    subsets_list = []
    m = len(L)
    for t in range(1, 2 ** m):
        # This part is used to find all the subsets
        subset = [L[j] for j in range(m) if (t >> j) & 1]
        if sum(subset) == V:
            subsets_list.append(subset)
    return subsets_list


num_per_line = 3
count = 0
n = int(input("Enter number of elements in L: "))
V = float(input("Enter V: "))
L = []
for i in range(1, n + 1):
    s = float(input(f"Enter number {i}: "))
    L.append(s)
print(f"All subsets equal to {int(V)} in L: ")
subsets = find_subsets()
for s in subsets:
    print(s, end=" ")
    count += 1
    if (count % num_per_line) == 0:
        print()
