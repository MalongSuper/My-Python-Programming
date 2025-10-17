# This program displays three integers in increasing order
# Input three integers
x, y, z = [int(xyz) for xyz in input("Enter three integers: ").split(",")]
# Assume the values
Integers = (x, y, z)
Integers_List = []
# Make a list contains the three integers
for Three_Integers in Integers:
    Integers_List.append(Three_Integers)
# Sort the integers in increasing order
Sorted_Integers = sorted(Integers_List, reverse=False)
# Display the results
print("The three integers without order: ", Integers_List)
print("The three integers with increasing order: ", Sorted_Integers)
