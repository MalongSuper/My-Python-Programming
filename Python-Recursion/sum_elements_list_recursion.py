# This program finds the sum of elements of a given list using recursion.


def find_sum(s):
    if len(s) == 1:
        return s[0]
    else:
        total = s[0] + find_sum(s[1:])
        return total


print("Sum of Elements in List (Recursion)")
n_list = []
number = int(input("Enter number of elements in List: "))
for i in range(number):
    n = float(input(f"Enter Number {i + 1}: "))
    n_list.append(n)
result = find_sum(n_list)
print(f"The Sum of the list: {result}")
