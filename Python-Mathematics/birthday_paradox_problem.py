# This program solves Birthday Paradox Problem
# Probability of at least two people share the same birthday
# among k people with n dates
# Formula: P (no matches) = (1 − 1/n) (1 − 2/n) … (1 − k-1/n)
# P (match) = 1 - P (no matches)


def solve_birthday_problem(number):
    n = 365
    a = 1
    for k in range(number):
        a *= (n - k)
    p_no_matches = a / (n ** number)
    p_match = 1 - p_no_matches
    return p_match


def main():
    print("Birthday Paradox Problem")
    number = int(input("Enter the number of people: "))
    p = solve_birthday_problem(number) * 100
    print(f"The probability of at least two people "
          f"share the same birthday among {number} people is:\n{p} %")


main()
