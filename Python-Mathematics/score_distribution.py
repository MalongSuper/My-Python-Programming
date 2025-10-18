# Probability and Statistics problem
# Analyze the average score in two classes
# Compare two students selected from each class
# Which student performed better
# Method using: Normal Distribution, Empirical Rule
import numpy as np
import matplotlib.pyplot as plt

print("Score Distribution")
mean1, sd1 = eval(input("Enter the mean and standard deviation of Class 1: "))
mean2, sd2 = eval(input("Enter the mean and standard deviation of Class 2: "))
# Find the score distribution
lower1, upper1 = mean1 - sd1, mean1 + sd1
lower2, upper2 = mean2 - sd2, mean2 + sd2
# Display the distribution
print("Class 1")
print(f"The score of the student in range [{lower1}, {upper1}] "
      f"=> Meet expectation (68.26 %)")
print("Class 2")
print(f"The score of the student in range [{lower2}, {upper2}] "
      f"=> Meet expectation (68.26 %)")
# Enter the score of Student 1 and Student 2
a = float(input("Enter score of Student A: "))
b = float(input("Enter score of Student B: "))
# Calculate Z-Score, the student is Z standard deviations above the mean
Za = (a - mean1) / sd1
Zb = (a - mean2) / sd2
print(f"=> Student A is {Za: .2f} standard deviations above the mean")
print(f"=> Student B is {Zb: .2f} standard deviations above the mean")
if Za > Zb:
    print("=> Student A did better in the test")
elif Za < Zb:
    print("=> Student B did better in the test")
else:
    print("=> Student A and B did equally")

# Draw bell curves
x1 = np.linspace(mean1 - 4 * sd1, mean1 + 4 * sd1, 1000)  # Range for Class 1
x2 = np.linspace(mean2 - 4 * sd2, mean2 + 4 * sd2, 1000)  # Range for Class 2
# Normal distributions for Class 1 and Class 2
y1 = (1 / (sd1 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x1 - mean1) / sd1) ** 2)
y2 = (1 / (sd2 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x2 - mean2) / sd2) ** 2)
# Plotting the bell curves
plt.figure(figsize=(10, 6))
plt.plot(x1, y1, label=f'Class 1 (mean={mean1}, sd={sd1})', color='blue')
plt.plot(x2, y2, label=f'Class 2 (mean={mean2}, sd={sd2})', color='red')
# Mark the students' scores on the plot
plt.scatter(a, (1 / (sd1 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((a - mean1) / sd1) ** 2), color='blue', zorder=5)
plt.scatter(b, (1 / (sd2 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((b - mean2) / sd2) ** 2), color='red', zorder=5)
# Add labels and title
plt.title('Score Distribution for Two Classes')
plt.xlabel('Score')
plt.ylabel('Density')
plt.legend()
# Show the plot
plt.grid(True)
plt.show()
