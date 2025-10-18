# Longest Common Subsequence using Recursion


def lcs(s1, s2, m, n):
    if m == 0 or n == 0:
        return ""
    elif s1[m - 1] == s2[n - 1]:
        return lcs(s1, s2, m - 1, n - 1) + s1[m - 1]
    else:
        lcs1 = lcs(s1, s2, m, n - 1)
        lcs2 = lcs(s1, s2, m - 1, n)
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2


def main():
    print("Longest Common Subsequence ")
    s1 = str(input("Enter String 1: "))
    s2 = str(input("Enter String 2: "))
    m = len(s1)
    n = len(s2)
    print("The Longest Common Subsequence:", lcs(s1, s2, m, n))


main()
