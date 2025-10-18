# Longest Common Subsequence using Recursion


def LCS(s1, s2, m, n):
    # If one of the sequences is empty, LSC = 0
    if m == 0 or n == 0:
        return 0
    elif s1[m - 1] == s2[n - 1]:
        return 1 + LCS(s1, s2, m - 1, n - 1)
    else:
        return max(LCS(s1, s2, m - 1, n), LCS(s1, s2, m, n - 1))


def main():
    print("Longest Common Subsequence (Recursion)")
    s1 = str(input("Enter String 1: "))
    s2 = str(input("Enter String 2: "))
    m = len(s1)
    n = len(s2)
    print("Length of LCS:", LCS(s1, s2, m, n))


main()
