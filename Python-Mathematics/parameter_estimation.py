# Probability and Statistics: Parameter Estimation
import numpy as np
from random_sample_values import sample_mean, sample_sd, total, length
from math import pi, sqrt


def ratio(n, x):  # Estimate point (or ratio)
    # n: total number of samples
    # x: the number of elements that satisfy sample
    f = length(x) / length(n)
    return f


def alpha(conf):  # Confidence = 1 - alpha
    a = 1 - conf
    return a


def score_both_bounds(conf):  # Find Z score
    a = float(alpha(conf) / 2)
    x = round(1 - a, 4)  # Get up to four decimal places
    # Load Table A1 values
    table = {}
    with open("TableA1.txt", "r") as file:
        for line in file:
            z_score, prob = map(float, line.strip().split(","))
            table[prob] = z_score
    # Find the closest probability to x
    closest_prob = min(table.keys(), key=lambda p: abs(p - x))
    z = table[closest_prob]
    return z


def score_one_bound(conf):  # Find Z score
    a = float(alpha(conf))
    x = round(1 - a, 4)  # Get up to four decimal places
    # Load Table A1 values
    table = {}
    with open("TableA1.txt", "r") as file:
        for line in file:
            z_score, prob = map(float, line.strip().split(","))
            table[prob] = z_score
    # Find the closest probability to x
    closest_prob = min(table.keys(), key=lambda p: abs(p - x))
    z = table[closest_prob]
    return z


def est_mean_both_bounds(n, conf):  # Estimate Interval Mean of both bounds
    number = length(n)
    mean = sample_mean(n)
    sd = sample_sd(n)
    z = score_both_bounds(conf)
    error = z * (sd / (number ** 0.5))
    return error, mean - error, mean + error


def est_mean_bound_left(n, conf):  # Estimate Interval Mean of the left bounds
    number = length(n)
    mean = sample_mean(n)
    sd = sample_sd(n)
    z = score_one_bound(conf)
    error = z * (sd / (number ** 0.5))
    return error, mean - error


def est_mean_bound_right(n, conf):  # Estimate Interval Mean of the right bound
    number = length(n)
    mean = sample_mean(n)
    sd = sample_sd(n)
    z = score_one_bound(conf)
    error = z * (sd / (number ** 0.5))
    return error, mean + error


def est_ratio_both_bounds(n, x, conf):  # Estimate Interval Ratio of both bounds
    f = ratio(n, x)
    number = length(n)
    z = score_both_bounds(conf)
    error = z * ((f * (1 - f) / number) ** 0.5)
    return error, f - error, f + error


def est_ratio_bound_left(n, x, conf):  # Estimate Interval Ratio of the left bounds
    f = ratio(n, x)
    number = length(n)
    z = score_one_bound(conf)
    error = z * ((f * (1 - f) / number) ** 0.5)
    return error, f - error


def est_ratio_bound_right(n, x, conf):  # Estimate Interval Ratio of the right bounds
    f = ratio(n, x)
    number = length(n)
    z = score_one_bound(conf)
    error = z * ((f * (1 - f) / number) ** 0.5)
    return error, f + error


def main():
    print("Parameter Estimation")
    n = int(input("Enter the length of the random sample: "))
    sample = np.random.randint(100, 999, n)
    print("Sample:\n", sample)
    # Get the value require for calculation
    confidence = float(input("Enter Confidence level: "))
    score_one_bound(confidence)
    if confidence < 0 or confidence > 1:
        print("Error: Confidence level is invalid. Please proceed and try again")
        return
    # Calculate Interval Estimation of Mean
    x = sample_mean(sample)
    e, lower_bound, upper_bound = est_mean_both_bounds(sample, confidence)
    e_left, e_right = (est_mean_bound_left(sample, confidence),
                       est_mean_bound_right(sample, confidence))
    left_bound, right_bound = e_left[1], e_right[1]
    print("x:", x)
    print("e:", e)
    print("Interval Estimation of Mean:")
    print(f"Both Bounds: ({lower_bound}, {upper_bound})")
    print(f"Left Bound: ({float("-inf")}, {right_bound})")
    print(f"Right Bound: ({left_bound}, {float("-inf")})")
    # Get the satisfied number
    number_of_event = int(input("Enter a satisfied number: "))
    event = []
    for k in range(len(sample)):
        # Get the number of events satisfying the satisfied number (use higher case)
        if sample[k] >= number_of_event:
            event.append(sample[k])
    # Interval Estimation of Ratio
    f = ratio(sample, event)
    ef, ef_lower_bound, ef_upper_bound = est_ratio_both_bounds(sample, event, confidence)
    ef_left, ef_right = (est_ratio_bound_left(sample, event, confidence),
                         est_ratio_bound_right(sample, event, confidence))
    ef_left_bound, ef_right_bound = ef_left[1], ef_right[1]
    print(f"There are {length(event)} that satisfy {length(sample)} number of sample")
    print("f:", f)
    print("e:", e)
    print("Interval Estimation of Ratio:")
    print(f"Both Bounds: ({ef_lower_bound}, {ef_upper_bound})")
    print(f"Left Bound: ({float("-inf")}, {ef_right_bound})")
    print(f"Right Bound: ({ef_left_bound}, {float("-inf")})")


# Avoid running the main function
# when importing the 'module' to another program
if __name__ == "__main__":
    main()
