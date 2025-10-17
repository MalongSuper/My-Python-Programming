# This program displays the sequence of Fibonacci (as table)
# Every number is the sum of the two previous numbers in the sequence
# From 0 to 100 (The first 100 numbers in the Fibonacci sequence)

def get_fibonacci():
    # Initial sequence with only 0
    sequence = []
    for i in range(0, 101):
        sequence.append(0)
    # Base case: The number at index 1 is 1
    sequence[1] = 1
    # Get the Fibonacci number
    for j in range(2, len(sequence)):
        sequence[j] = sequence[j - 1] + sequence[j - 2]
    # Return the sequence
    return sequence


def main():
    Number_per_Line = 6
    Count = 0
    sequence = get_fibonacci()
    # Display the table
    print("\t\t\tFibonacci Sequence Table")
    print("---------------------------------------------------")
    for k in range(len(sequence)):
        print(format(sequence[k], '4d'), end=", ")
        Count += 1
        if (Count % Number_per_Line) == 0:
            print()


main()
