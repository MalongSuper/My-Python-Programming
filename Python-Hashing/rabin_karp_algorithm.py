# Rabin Karp Algorithm
# Improve the Rolling hash function using the formula:
# P1 * 10^m-1 + P2 * 10^m-2 + P3 * 10^m-3 + … Pn * 10^m-n

def rolling_hash_code(x, y, p):  # Return the hash code of X and Y
    res_y = {}
    # Calculate hash code for pattern Y
    n = 0
    for i in range(len(y)):
        n += ord(y[i]) * p ** (len(y) - (i + 1))
    res_y[y] = n  # Append to dictionary
    # Calculate hash code for every sub-string X
    sub_string = []
    for j, k in zip(range(len(x)), range(len(y), len(x) + 1, 1)):
        sub_string.append(x[j:k])
    res_x = {}
    for m in sub_string:
        res_x[m] = sum(ord(i) * p ** (len(y) - (s + 1))
                       for i, s in zip(m, range(len(y))))
    return res_x, res_y


def find_pattern(x, y, p):
    res_x, res_y = rolling_hash_code(x, y, p)
    match = []
    for i in res_x:
        # Find sub-string with the same hash code as the pattern
        if res_x[i] == res_y.get(y):
            match.append(i)
    return match


def main():
    print("Rabin-Karp Algorithm")
    X = str(input("Enter string X: "))
    Y = str(input("Enter pattern Y: "))
    result_x, result_y = rolling_hash_code(X, Y, 10)
    print(f"Y: {result_y}")
    print(f"X: {result_x}")
    match = find_pattern(X, Y, 10)
    print(f"Match at: {match}")


main()
