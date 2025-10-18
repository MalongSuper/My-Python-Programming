# Cartesian Product of two sets
# All ordered pairs (a, b) where "a" is in A and "b" is in B
print("Cartesian Product")
A = input("Enter A: ").split(",")
B = input("Enter B: ").split(",")
# Convert to set
set1 = set(int(x) for x in A)
set2 = set(int(y) for y in B)
print("Set 1:", set1)
print("Set 2:", set2)
set1, set2 = list(set1), list(set2)  # Convert set to list
print("All ordered pairs (a, b):")
for i in range(len(set1)):
    for j in range(len(set2)):
        # Display all the ordered pairs
        print(f"({set1[i]}, {set2[j]})")
