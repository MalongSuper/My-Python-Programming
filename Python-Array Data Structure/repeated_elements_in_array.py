# This is finds all the repeated elements in an array
import numpy as np
new_list = []
dup_list = []
print("Repeated Elements in an array")
number = int(input("Enter number of elements: "))
array = np.random.randint(0, 101, size=number)
# Find for repeated elements in an array
for m in array:
    if m not in new_list:
        new_list.append(m)
    else:
        dup_list.append(m)
print(array)
if len(dup_list) == 0:
    print("No Repeated Elements")
else:
    print(f"Repeated Elements: {', '.join(map(str, dup_list))}")
