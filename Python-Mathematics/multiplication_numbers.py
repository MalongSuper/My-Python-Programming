# Multiplication numbers
print("Multiplication")
n = int(input("Enter n: "))
multi = 1
for i in range(1, n + 1):
    number = eval(input(f"({i}) Enter number: "))
    multi *= number
print("Multiplication:", multi)
