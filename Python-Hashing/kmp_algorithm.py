# Knutt-Morris-Pratt Algorithm for String Matching


def kmp_method(S, P):
    m, n = len(P), len(S)  # Initial length for pattern P and string S
    i, j = 0, 0  # Initial pointers i, j pointing the index 0
    Pi = compute_pi(P)  # Find the pi values
    while (n - i) >= (m - j):
        print(f"+ i = {i}, j = {j} => S[i] = {S[i]}, P[j] = {P[j]}")
        if P[j] == S[i]:
            print("S[i] = P[j] -> Match, increment both i and j")
            i += 1
            j += 1
        if j == m:
            print(f"=> Pattern found at {i - j}, and set j as Pi[j - 1] = {Pi[j - 1]}")
            j = Pi[j - 1]
        # In case of mismatch
        elif i < n and P[j] != S[i]:
            print(f"S[i] != P[j] -> Mismatch -> Set j at Pi[j - 1] = {Pi[j - 1]}. "
                  f"If j returns to index 0 -> increment i")
            if j != 0:
                j = Pi[j - 1]
            else:
                i += 1


def compute_pi(P):  # Creation of Pi Table of Pattern Y
    i, j, m = 1, 0, len(P)  # Length of the match so far
    Pi = [0] * m  # Initial Pi table with Pi values 0
    Pi[0] = 0
    # Calculate Pi[0]
    while i < m:
        # i = {i},  = {j}, P[i], P[j] = {P[i]}, {P[j]}
        if P[i] == P[j]:
            j += 1
            Pi[i] = j
            i += 1
        else:
            if j != 0:
                # P[i] != P[j] = {P[i]} != {P[j]}, and j is not 0,
                # set j as Pi[j - 1], {Pi[j - 1]}
                j = Pi[j - 1]
            else:
                # P[i] != P[j] = {P[i]} != {P[j]}, and j is 0,
                # set j as Pi[i] = 0 and increment i
                Pi[i] = 0
                i += 1
    return Pi


def main():
    print("KMP Algorithm")
    S = str(input("Enter a string: "))
    P = str(input("Enter a pattern: "))
    # Display the Pi value
    pi = compute_pi(P)
    print(f"Pi values: {pi}")
    # Check for matching
    kmp_method(S, P)


main()
