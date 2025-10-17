# This program counts all the possible combinations for two-digit numbers from 1 to 7
Number_per_Line = 6
CountNumber = 0
Count = 0
Reverse_Combination = []
# Display the table
print("Possible Combination for two-digit numbers from 1 to 7")
print("-------------------------------------------------------")
# The range is from 1 to 7
for Number in range(1, 8):
    A = Number
    for Number2 in range(1, 8, 1):
        B = Number2
        # Only count the combinations with two different digits
        if A != B:
            # Check the reversed combination
            ReverseNumber = str(B) + str(A)
            # If it is not in the reverse list, count the number
            if ReverseNumber not in Reverse_Combination:
                # Display all the possible combinations in table
                PossibleNumber = str(A) + str(B)
                print(format(int(PossibleNumber), '8d'), end="")
                Count += 1
                if (Count % Number_per_Line) == 0:
                    print()
                # Count the number
                CountNumber += 1
                # Add the combination and its reversed version to the list
                Reverse_Combination.append(PossibleNumber)
                Reverse_Combination.append(ReverseNumber)
# Display the result
print()
print("The total number of all combinations is", CountNumber)
