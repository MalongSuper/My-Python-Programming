# Z-Score Scalar with numpy
import numpy as np

print("Z-Score Normalization")
x = []
n = int(input("Enter the number of values: "))
for k in range(n):
    number = float(input(f"Enter number {k + 1}: "))
    x.append(number)

x_normalized = []
x = np.array(x)
mean = np.mean(x)
sd = np.std(x)
print("Mean of X:", mean)
print("SD of X:", sd)

for i in range(len(x)):
    normalized_value = (x[i] - mean) / sd
    x_normalized.append(normalized_value)

print("Original\t Normalized")
for j in range(len(x_normalized)):
    print('{:<12} {:<15}'.format(x[j], x_normalized[j]))

# Return standard deviation and mean of the normalized dataset
mean_normalized = np.mean(x_normalized)
sd_normalized = np.std(x_normalized)
print("Mean of X Normalized:", mean_normalized)
print("SD of X Normalized:", sd_normalized)
