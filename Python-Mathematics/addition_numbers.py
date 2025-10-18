# Addition numbers
print("Addition")
n = int(input("Enter n: "))
add = 0
for i in range(1, n + 1):
    number = eval(input(f"({i}) Enter number: "))
    add += number
print("Addition:", add)
