# Longest Common Subsequence
# Using Advanced Recursion
import numpy as np


def LCS(s1, s2, m, n, dp):
    # If one of the string is empty LCS = 0
    if m == 0 or n == 0:
        return 0
    # Check the string
    if dp[m][n] != -1:
        return dp[m][n]

    if s1[m - 1] == s2[n - 1]:
        # Store all the string already calculated
        dp[m][n] = 1 + LCS(s1, s2, m - 1, n - 1, dp)
        return dp[m][n]

    dp[m][n] = max(LCS(s1, s2, m - 1, n, dp), LCS(s1, s2, m, n - 1, dp))
    return dp[m][n]


def main():
    print("Longest Common Subsequence (Recursion Advanced)")
    s1 = str(input("Enter String 1: "))
    s2 = str(input("Enter String 2: "))
    m = len(s1)
    n = len(s2)
    dp = np.full((m + 1, n + 1), -1)  # Contains -1
    print("Length of LCS:", LCS(s1, s2, m, n, dp))
    print(dp)


main()
