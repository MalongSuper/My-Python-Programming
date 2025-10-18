# Longest Common Subsequence (Display the longest subsequence)
# Using Dynamic Programming
import numpy as np


def lcs(s1, s2, m, n):
    dp = np.zeros((m + 1, n + 1), int)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    longest_com = ""

    i = m
    j = n
    while i > 0 and j > 0:
        # If S1 and S2 is the same then it is LCS
        if s1[i - 1] == s2[j - 1]:
            longest_com += s1[i - 1]
            i -= 1
            j -= 1
        # If not, find the better value 
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse to get the correct LCS 
    longest_com = longest_com[::-1]
    print("Longest Common Subsequence:", longest_com)


def main():
    print("Find the Longest Common Subsequence")
    s1 = str(input("Enter String 1: "))
    s2 = str(input("Enter String 2: "))
    m = len(s1)
    n = len(s2)
    lcs(s1, s2, m, n)


main()
