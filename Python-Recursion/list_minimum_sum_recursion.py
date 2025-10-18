# This program finds the list having a minimum sum

def list_sum(lst):  # This function calculates the sum of each list
    if len(lst) == 1:
        return lst[0]
    return lst[0] + list_sum(lst[1:])


def minimum_sum_list(n_lst):
    if len(n_lst) == 1:
        return n_lst[0]

    current_sum = list_sum(n_lst[0])
    next_list = minimum_sum_list(n_lst[1:])
    next_sum = list_sum(next_list)

    if current_sum < next_sum:
        return n_lst[0]
    else:
        return next_list


print("List with Minimum Sum (Recursion)")
num_list = []
num = int(input("Enter number of lists in list: "))
for i in range(num):
    element_list = []
    num_element = int(input(f"Enter number of elements in List {i + 1}: "))
    for j in range(num_element):
        element = float(input(f"Enter Number {j + 1}: "))
        element_list.append(element)
    num_list.append(element_list)

print("List:", num_list)
result = minimum_sum_list(num_list)
print("List with Minimum Sum:", result)
