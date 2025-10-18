# Interesting Problem: Find A such that AAAA + AAA + AA + A = Any integer
# Advanced: Using string manipulation to form numbers -> Increase the digits
# A + AA + AAA + AAAA = Any integer

"""
Previous code: Solve AAAA + AAA + AA + A = 8638
    for i in range(1, 10):
        digit1 = i
        digit2 = int(str(i) + str(i))
        digit3 = int(str(i) + str(i) + str(i))
        digit3 = int(str(i) + str(i) + str(i) + str(i))
        if sum([digit1, digit2, digit3, digit4]) == 8638:
            print(i)
    # Output is 7
"""


def find_A(target_number, max_digits=4):  # Default to 4 if not specified
    combined_numbers = []
    number = 1
    for i in range(1, 10):
        # Form the numbers by combining them as strings and convert to integer
        for j in range(1, max_digits + 1):
            combined_numbers.append(int(str(i) * j))
        if sum(combined_numbers) == target_number:
            number = i
            break  # Exit the loop if found

        # Reset for the next digit
        combined_numbers = []

        # If we do not reset, the combined_numbers will keep accumulating
        # For example, if we do not reset, when i = 2, 
        # combined_numbers will append the next sets, but i = 1's sets are still there
        # Might include the sum of 1's sets and 2's sets together -> Incorrect result

    return number  # There is only one solution


def main():
    global target
    print("Find A such that A + AA + AAA + AAAA + ... = any integer")
    try:
        # Sample input: 8638 and max_digits = 4
        target = int(input("Enter the target number: "))
        max_digits = int(input("Enter the maximum digits (default is 4): "))
    # Handle invalid input for max_digits
    except ValueError:
        max_digits = 4

    result = find_A(target, max_digits)

    # A = 1, max_digits = 4 means 1 + 11 + 111 + 1111 = 1234
    # Also means no solution for the input number
    if result == 1 and sum(int(str(1) * j) for j 
                           in range(1, max_digits + 1)) != target:
        print("No solution found")
    else:
        print(f"The value of A is: {result}")


main()
