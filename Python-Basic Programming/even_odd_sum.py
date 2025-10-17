# Sum of numbers from n1 to n2
n1 = int(input("Enter integer n1: "))
n2 = int(input("Enter integer n2: "))
odd, even = [], []
for i in range(n1, n2 + 1):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("+ Sum of even:", sum(even))
print("+ Sum of odd:", sum(odd))
