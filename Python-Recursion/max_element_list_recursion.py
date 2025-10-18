# This program finds the maximum element from a list using recursion


def find_max(L):
    if len(L) == 1:
        return L[0]
    else:
        rest = find_max(L[1:])
        if L[0] > rest:
            return L[0]
        else:
            return rest


print("Maximum Element in List (Recursion)")
n_list = []
number = int(input("Enter number of elements in List: "))
for i in range(number):
    n = float(input(f"Enter Number {i + 1}: "))
    n_list.append(n)
result = find_max(n_list)
print(f"The Maximum Element in List: {result}")
