# Given two arrays X and Y
# find the elements which are in Y, but not in X
import numpy as np


def element_in_arrays(arr_1, arr_2):
    result_list = []
    set_x, set_y = set(arr_1), set(arr_2)
    result_set = list(set_y - set_x)
    for res in result_set:
        result_list.append(int(res))
    return result_list


def main():
    print("Same elements in two arrays")
    size_x = int(input("Enter size of the array X: "))
    size_y = int(input("Enter size of the array Y: "))
    array_x = np.random.randint(1, 20, size=size_x)
    array_y = np.random.randint(1, 20, size=size_y)
    print(f"Array X: {array_x}\nArray Y: {array_y}")
    result = element_in_arrays(array_x, array_y)
    print("Elements in Y but not in X: ", result)


main()
