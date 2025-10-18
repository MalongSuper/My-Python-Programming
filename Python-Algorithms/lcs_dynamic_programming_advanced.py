# Longest Common Subsequence
# Using Dynamic Programming Advanced
import numpy as np


def LCS(s1, s2):
    m = len(s1)
    n = len(s2)
    previous = np.zeros(n + 1, int)  # vector (n + 1) cột
    current = np.zeros(n + 1, int)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                # Length of LCS of string s
                current[j] = 1 + previous[j - 1]
            else:
                current[j] = max(previous[j], current[j - 1])
        # Chuẩn bị tính qua dòng mới
        previous = current.copy()
    return current


def main():
    print("Chuỗi Con Chung Dài Nhất (Dynamic Programming cải tiến)")
    s1 = str(input("Nhập chuỗi thứ 1: "))
    s2 = str(input("Nhập chuỗi thứ 2: "))
    current = LCS(s1, s2)
    print(current)
    # Phần tử cuối cùng của vector current
    print("Chiều dài của LCS: ", int(current[-1]))


main()

