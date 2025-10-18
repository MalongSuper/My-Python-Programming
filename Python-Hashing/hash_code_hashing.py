# Calculate Hash Code for string

def find_index(key, n):  # Find the index of the hash code
    return key % n


def hash_code(s):  # Calculate the hash code
    # Formula ord(s[0]) * 31^(n – 1) + ord(s[1]) * 31^(n – 2)
    # + … + ord(s[n - 1])] * 31^(n – n)
    n = len(s)
    result = 0
    for i in range(n):
        result += ord(s[i]) * 31 ** (n - (i + 1))
    return result


def main():
    print("Hash Table - Hash Code")
    string = str(input("Enter a string: "))
    res = hash_code(string)
    print(f"+ Hash Code: {res}")
    print(f"+ Hash Table Index: {find_index(res, 10)}")


if __name__ == "__main__":
    main()
