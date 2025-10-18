# This program creates wave-like array from an unsorted array
# Simplifying the code
import numpy as np


def wave_one_array(arr, n):
    def wave_temp_array(a):
        a.sort()
        for i in range(0, len(a) - 1, 2):
            a[i], a[i + 1] = a[i + 1], a[i]
        return a

    if n < 2:
        return arr
    elif n == 2:
        arr[0], arr[1] = sorted(arr[:2], reverse=True)
    elif n == 3:
        arr[:3] = wave_temp_array(arr[:3])
    else:
        arr[:3] = wave_temp_array(arr[:3])
        for j in range(2, n - 1, 2):
            arr[j: j + 3] = wave_temp_array(arr[j:j + 3])
        if n % 2 and arr[-1] > arr[-2]:
            arr[-1], arr[-2] = arr[-2], arr[-1]

    return arr


print("Wave-like Array")
size = int(input("Enter the size of the array: "))
array = np.random.randint(0, 101, size=size)
print(array)
number = int(input("Enter a number: "))
try:
    result = wave_one_array(array, number)
except IndexError:
    print("Error: Out of Bound")
else:
    print(f"Array after wave: \n{result}")
