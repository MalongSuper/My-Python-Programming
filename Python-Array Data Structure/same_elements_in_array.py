# Given two arrays, find if none of the elements in the
# two arrays is the same
import numpy as np


def no_same_element(arr_1, arr_2):
    set_1 = set(arr_1)
    set_2 = set(arr_2)
    intersection = set_1.intersection(set_2)
    return len(intersection) == 0


def main():
    print("Same elements in two arrays")
    size_x = int(input("Enter size of the array X: "))
    size_y = int(input("Enter size of the array Y: "))
    array_x = np.random.randint(1, 20, size=size_x)
    array_y = np.random.randint(1, 20, size=size_y)
    print(f"Array X: {array_x}\nArray Y: {array_y}")
    result = no_same_element(array_x, array_y)
    if result is True:
        print("=> X and Y have no common elements")
    else:
        print("=> X and Y have some common elements")


main()
