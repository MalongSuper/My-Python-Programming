# This program imports RandomSampleValues.py
# To find values of the random sample given as a table of
# The values and the frequencies
# Probability and Statistics problem
import random_sample_values as rsv


def main():
    print("Random Sample Table")
    sequence = []
    n = int(input("Enter the length of the table: "))
    for i in range(n):
        # Input a value and its frequency
        x, f = eval(input(f"Enter x{i + 1} and its frequency: "))
        for j in range(f):
            sequence.append(x)
    # Display result
    print("Result:")
    print("sample mean x:", rsv.sample_mean(sequence))
    print("total:", rsv.total(sequence))
    print("total^2:", rsv.total_square(sequence))
    print("s^2:", rsv.sample_variance(sequence))
    print("s:", rsv.sample_sd(sequence))
    print("n:", rsv.length(sequence))
    print("min:", rsv.minimum(sequence))
    print("max:", rsv.maximum(sequence))
    print("median:", rsv.median(sequence))
    print("q1, q2, q3:", rsv.quartiles(sequence))
    print("geo mean:", rsv.geometric_mean(sequence))


# Avoid running the main function
# when importing the 'module' to another program
if __name__ == "__main__":
    main()
