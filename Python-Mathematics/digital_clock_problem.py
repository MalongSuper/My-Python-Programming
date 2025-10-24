# Digital Clock Problem

""" 1. Find the maximum number of digital clocks and segments
    Input: integer n
    Determine the number of digital clocks required,
     and the number of segments that will be colored to make that number.
     E.g., input = 10, we need 2 digital clocks,
     and since 1 needs 2 segments, and 0 needs 6 segments,
     the total number of segments is 2 + 6 = 8. """


def solve_num_segments(n):
    num_dict = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    digits = str(n)
    number_of_digital_clocks = len(str(n))
    number_of_segments = sum(num_dict[int(i)] for i in digits)

    return number_of_digital_clocks, number_of_segments


"""2. The greatest number that can be displayed with a given number of segments.
    The input is now the number of segments $s$
    Determine the greatest number that can be displayed with $s$ segments given."""


def solve_greatest_number_segments(s):
    num_dict = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    key_list = []
    # If the total number of segments is small enough to form a single digit
    if s <= 7:
        # Find all digits that can be formed using exactly 's' segments
        for k, v in num_dict.items():
            if v == s:
                key_list.append(k)
        # If no digit matches the exact number of segments, return None
        if len(key_list) == 0:
            return None
        # Return the largest digit that can be formed
        return max(key_list)
    # If the number of segments is large, we may need multiple digits
    else:
        sublist = []  # store 7 and the leftover segments
        # Subtract 7 segments at a time (since 8 uses all 7 segments)
        # until fewer than 7 segments remain
        while s >= 7:
            s = s - 7
            sublist.append(s)
        # Take the last number as left over
        leftover = sublist[-1]
        # Replace all segment counts in the list with 7
        for i in range(len(sublist)):
            sublist[i] = 7
        # Append the leftover segments at the end
        sublist.append(leftover)
        # For each number of segments in sublist, find the largest digit possible
        for j in range(len(sublist)):
            temp_key_list = []
            for k, v in num_dict.items():
                if v == sublist[j]:
                    temp_key_list.append(k)
            # Add the largest digit that can be made with that segment count
            if temp_key_list:  # If it is not empty
                key_list.append(max(temp_key_list))
    # Join all digits together into a single number string
    return ''.join(str(k) for k in key_list)


n = int(input("Enter any number: "))
num_clocks, num_segments = solve_num_segments(n)
print("Number of digital clocks:", num_clocks)
print("Number of segments:", num_segments)

s = int(input("Enter segments: "))
print("Best number:", solve_greatest_number_segments(s))

