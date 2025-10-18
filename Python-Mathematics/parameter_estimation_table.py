# Probability and Statistics: Parameter Estimation
# For a table of sample
import RandomSampleValues as rsv
import ParameterEstimation as pe


def main():
    # Input table
    print("Random Sample Table (Estimation for the population)")
    sequence = []
    n = int(input("Enter the length of the table: "))
    for i in range(n):
        # Input a value and its frequency
        x, f = eval(input(f"Enter x{i + 1} and its frequency: "))
        for j in range(f):
            sequence.append(x)
    # Display the results for the random sample values (used for estimation problem)
    print("n:", rsv.length(sequence))
    print("sample mean x:", rsv.sample_mean(sequence))
    print("s:", rsv.sample_sd(sequence))
    # Input values required for the estimation population
    conf = float(input("Enter Confidence: "))
    # Display the estimation interval results
    est_mean = pe.est_mean_both_bounds(sequence, conf)
    print(f"Estimation of u: ({est_mean[1]}, {est_mean[2]})")
    # Input values required for the estimation ratio
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
    est_ratio = pe.est_ratio_both_bounds(sequence, x, conf)
    print(f"Estimation ratio of p: ({est_ratio[1]}, {est_ratio[2]})")


# Avoid running the main function
# when importing the 'module' to another program
if __name__ == "__main__":
    main()
