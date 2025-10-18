# Hypothesis Testing in Probability and Statistics
# For Average Parameter
import random_sample_values as rsv
import parameter_estimation as pe


def hypothesis_testing(n, x, s, u0, sig):
    t = ((n ** 0.5) / s) * abs(x - u0)  # Find t
    z = pe.score_both_bounds(1 - sig)  # Find the z score using the parameter module
    print(f"t = {t}")
    print(f"z({sig}/2) = {z}")
    if t <= z:  # Not Reject / Accept H0 (u0)
        return True
    else:  # t > z -> Reject H0 / Accept H1: u ≠ u0
        return False


def main():
    # Input table
    print("Random Sample Table (Hypothesis Testing Average)")
    sequence = []
    n = int(input("Enter the length of the table: "))
    for i in range(n):
        # Input a value and its frequency
        x, f = eval(input(f"Enter x{i + 1} and its frequency: "))
        for j in range(f):
            sequence.append(x)
    # Display the results for the random sample values
    n = rsv.length(sequence)
    x = rsv.sample_mean(sequence)
    sd = rsv.sample_sd(sequence)
    # Enter u0 for hypothesis testing problem
    print("n:", n)
    print("sample mean x:", x)
    print("s:", sd)
    u0 = float(input("Enter u0: "))
    significance = float(input("Enter significance level: "))
    t = hypothesis_testing(n, x, sd, u0, significance)
    if t:  # If is True
        print(f"=> Not Reject H0 / Accept H0: u = {u0}")
    else:  # If is False
        print(f"=> Reject H0: u = {u0} / Accept H1: u ≠ {u0}")
        if x < u0:
            print(f"=> Accept u < {u0}")
        else:  # >= 0
            print(f"=> Accept u ≥ {u0}")


# Avoid running the main function
# when importing the 'module' to another program
if __name__ == "__main__":
    main()
