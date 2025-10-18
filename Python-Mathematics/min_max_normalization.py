# Min Max Scalar with Python

print("Min Max Normalization")
x = []
n = int(input("Enter the number of values: "))
for k in range(n):
    number = float(input(f"Enter number {k + 1}: "))
    x.append(number)

x_normalized = []
x_min, x_max = min(x), max(x)
for i in range(len(x)):
    normalized_value = (x[i] - x_min) / (x_max - x_min)
    x_normalized.append(normalized_value)

print("Original\t Normalized")
for j in range(len(x_normalized)):
    print('{:<12} {:<15}'.format(x[j], x_normalized[j]))
