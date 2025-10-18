# Hypothesis Testing in Probability and Statistics
# For Ratio
import random_sample_values as rsv
import parameter_estimation as pe


def hypothesis_testing(n, f, p0, sig):
    t = (n / (p0 * (1 - p0))) ** 0.5 * abs(f - p0)  # Find t
    z = pe.score_both_bounds(1 - sig)  # Find the z score using the parameter module
    print(f"t = {t}")
    print(f"z({sig}/2) = {z}")
    if t <= z:  # Not Reject / Accept H0 (p0)
        return True
    else:  # t > z -> Reject H0 / Accept H1: u ≠ u0
        return False


def main():
    # Input table
    print("Random Sample Table (Hypothesis Testing Ratio)")
    sequence = []
    n = int(input("Enter the length of the table: "))
    for i in range(n):
        # Input a value and its frequency
        x, f = eval(input(f"Enter x{i + 1} and its frequency: "))
        for j in range(f):
            sequence.append(x)
    # Display the results for the random sample values
    n = rsv.length(sequence)
    print("n:", n)
    number = int(input("Enter the satisfied number: "))
    bound = int(input("Choose bound (0 - Lower; Any key - Higher): "))
    x = []
    if bound == 0:  # Lower
        for k in range(len(sequence)):
            # Get the number of events satisfying the satisfied number (higher case)
            if sequence[k] < number:
                x.append(sequence[k])
    else:  # Higher
        for k in range(len(sequence)):
            # Get the number of events satisfying the satisfied number (lower case)
            if sequence[k] >= number:
                x.append(sequence[k])
    print("Number of satisfied elements:", rsv.length(x))
    f = pe.ratio(sequence, x)  # Get the ratio f
    # Enter p0 for hypothesis testing problem
    p0 = float(input("Enter p0: "))
    significance = float(input("Enter significance level: "))
    t = hypothesis_testing(n, f, p0, significance)
    if t:  # If is True
        print(f"=> Not Reject H0 / Accept H0: p = {p0}")
    else:  # If is False
        print(f"=> Reject H0: p = {p0} / Accept H1: u ≠ {p0}")
        if f < p0:
            print(f"=> Accept p < {p0}")
        else:  # >= 0
            print(f"=> Accept p ≥ {p0}")


# Avoid running the main function
# when importing the 'module' to another program
if __name__ == "__main__":
    main()
