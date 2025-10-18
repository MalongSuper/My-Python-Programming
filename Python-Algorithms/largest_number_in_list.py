# Finding the largest in a given list
number_list = []
maximum = float('-inf')
print("Largest number in a given list")
n = int(input("Enter length n: "))
for b in range(1, n + 1):
    number = float(input(f"Enter number {b}: "))
    number_list.append(number)
    if number > maximum:
        maximum = number
print("The largest number:", int(maximum))
print("Number of comparisons (worse case):", n - 1)
print("Number of comparisons (best case when the values are sorted):", 0)
    
