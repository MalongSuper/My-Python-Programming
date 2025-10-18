# Longest Common Subsequence
# Using Dynamic Programming
import numpy as np


def LCS(s1, s2):
    m = len(s1)
    n = len(s2)
    table = np.zeros((m + 1, n + 1), int)

    def update_lcs_table(i, j):
        if s1[i - 1] == s2[j - 1]:
            table[i][j] = 1 + table[i - 1][j - 1]
        else:
            table[i][j] = max(table[i - 1][j], table[i][j - 1])

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            update_lcs_table(i, j)
    return table


def main():
    print("Longest Common Subsequence (Dynamic Programming)")
    s1 = str(input("Enter String 1: "))
    s2 = str(input("Enter String 2: "))
    table = LCS(s1, s2)
    print(table)
    # Last element in the table
    print("Length of LCS:", table[-1, -1])


main()
