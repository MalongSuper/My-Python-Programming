# Rolling Hash Function - Idea for Rabin-Karp algorithm
# String Matching
# Not efficient due to collision


def rolling_hash_code(x, y):  # Return the hash code of X and Y
    res_y = {}
    # Calculate hash code for pattern Y
    n = 0
    for i in range(len(y)):
        n += ord(y[i])
    res_y[y] = n  # Append to dictionary
    # Calculate hash code for every sub-string X
    sub_string = []
    for j, k in zip(range(len(x)), range(len(y), len(x) + 1, 1)):
        sub_string.append(x[j:k])
    res_x = {}
    for m in sub_string:
        res_x[m] = sum(ord(i) for i in m)   # Append to dictionary
    return res_x, res_y


def find_pattern(x, y):
    res_x, res_y = rolling_hash_code(x, y)
    match = []
    for i in res_x:
        # Find sub-string with the same hash code as te pattern
        if res_x[i] == res_y.get(y):
            match.append(i)
    return match


def main():
    print("Rolling Hash Function")
    X = str(input("Enter string X: "))
    Y = str(input("Enter pattern Y: "))
    result_x, result_y = rolling_hash_code(X, Y)
    print(f"Y: {result_y}")
    print(f"X: {result_x}")
    match = find_pattern(X, Y)
    print(f"Match at: {match}")


main()
