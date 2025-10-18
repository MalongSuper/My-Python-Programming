# This program finds all the values in a random sample
# Probability and Statistics problem

def length(s):  # Length of the sequence
    length = len(s)
    return length


def maximum(s):  # The maximum of the sequence
    maxi = max(s)
    return maxi


def minimum(s):  # The minimum of the sequence
    mini = min(s)
    return mini


def total(s):  # Total
    total = sum(s)
    return total


def total_square(s):  # Power Total (with the value power by 2)
    pow_s = []
    for i in range(len(s)):
        x = s[i] ** 2
        pow_s.append(x)
    total_power = sum(pow_s)
    return total_power


def sample_mean(s):  # Sample Mean
    mean = sum(s) / len(s)
    return mean


def median(s):  # Median
    s = sorted(s)
    if len(s) % 2 == 0:  # If length is even
        k = len(s) // 2  # n = 2k
        return 0.5 * (s[k - 1] + s[k])
    else:  # If length is odd
        k = (len(s) - 1) // 2  # n = 2k + 1
        return s[k]


def quartiles(s):
    if len(s) < 2:  # If the sequence has less than 2 values, it has no quartiles
        return None
    else:
        m = median(s)
        q2 = m  # Quartile 2 is the median
        if len(s) % 2 == 0:  # If length is even
            left_half = s[: len(s) // 2]  # Quartile 1 is the median of the left half
            right_half = s[len(s) // 2:]  # Quartile 3 is the median of the right half
            q1 = median(left_half)
            q3 = median(right_half)
        else:  # If length is odd
            for i in range(len(s)):
                if (i == ((len(s) - 1) / 2) - 0.5
                        and s[i] == m):  # Exclude the median
                    s.pop(i)
            left_half = s[: (len(s) // 2)]
            right_half = s[(len(s) // 2):]
            q1 = median(left_half)
            q3 = median(right_half)

        return q1, q2, q3


def left_quartile(s):  # Return the left quartile
    quartile = quartiles(s)
    return quartile[0]


def right_quartile(s):  # Return the right quartile
    quartile = quartiles(s)
    return quartile[2]


def medium_quartile(s):  # Return the medium quartile
    quartile = quartiles(s)
    return quartile[1]


def mode(s):  # Mode
    occur = 0
    count = 0
    occur_dict = {}  # Use dictionary
    if len(s) == 0:  # If length == 0, there is no mode
        return None
    else:
        for i in range(len(s)):  # Try each of the number k
            for j in range(len(s)):  # Compare the number with every number in the sequence
                if s[i] == s[j]:
                    occur += 1
                count += 1  # Increase the count
                if count == len(s):  # All the elements have been considered with the number
                    occur_dict[s[i]] = occur  # Add the number of occurrences to the dict
                    occur, count = 0, 0  # Restart occur and count for the next number k
        # Get the dict and obtain the result
        occur_values = max(occur_dict.values())  # Get the maximum occurrence in the dict
        occur_list = []
        for k, v in occur_dict.items():
            if v == occur_values:
                occur_list.append(k)

        return str(occur_list)[1: -1]


def get_occur(s):  # Return a dictionary with the number and its occurrence
    occur = 0
    count = 0
    occur_dict = {}  # Use dictionary
    for i in range(len(s)):  # Try each of the number k
        for j in range(len(s)):  # Compare the number with every number in the sequence
            if s[i] == s[j]:
                occur += 1
            count += 1  # Increase the count
            if count == len(s):  # All the elements have been considered with the number
                occur_dict[s[i]] = occur  # Add the number of occurrences to the dict
                occur, count = 0, 0  # Restart occur and count for the next number k
    return occur_dict


def occurrence(s, n):  # Return the occurrence of a number
    occur = 0
    for i in range(len(s)):
        if s[i] == n:
            occur += 1  # Increase the occurrence
    return occur


def geometric_mean(s):  # Geometric mean
    product = 1
    for i in range(len(s)):
        product = product * s[i]  # Product of all the elements in the sequence
    geometric_mean = product ** (1 / len(s))  # Power the product by 1/n
    return geometric_mean


def sample_variance(s):  # Sample variance
    var_s = []
    mean = sample_mean(s)
    for i in range(len(s)):
        x = (s[i] - mean) ** 2
        var_s.append(x)
    variance = sum(var_s) / (len(s) - 1)
    return variance


def sample_sd(s):  # Sample standard deviation
    variance = sample_variance(s)
    sd = variance ** 0.5
    return sd


def main():
    # The main function, it is not the part of the module
    print("Random Sample Values")
    sequence = []
    n = int(input("Enter the length of the random sample: "))
    for i in range(n):
        x = float(input(f"Enter x{i + 1}: "))
        sequence.append(x)
    print("Result:")
    print("Length:", length(sequence))
    print("Max:", maximum(sequence), "Min:", minimum(sequence))
    print("Total:", total(sequence))
    print("Total Power:", total_square(sequence))
    print("Sample Mean:", sample_mean(sequence))
    print("Median:", median(sequence))
    print("Quartiles:", quartiles(sequence))
    print("Mode:", mode(sequence))
    print("Geometric Mean:", geometric_mean(sequence))
    print("Sample Variance:", sample_variance(sequence))
    print("Sample SD:", sample_sd(sequence))


# Avoid running the main function
# when importing the 'module' to another program
if __name__ == "__main__":
    main()
