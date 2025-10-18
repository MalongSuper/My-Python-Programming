# Median of medians
# Finding the median of the sequence
from random_sample_values import median


def get_index_med(s):  # Get the index of the median of the sequence
    n = len(s)
    if n % 2 == 0:  # The length is even
        return int(0.5 * n)
    else:  # The length is odd
        return int(0.5 * (n - 1))


def med_of_medians(s):
    while True:
        n = len(s)
        j = 5
        med_list = []
        for i in range(0, n, j):
            # Divide into sub-sequence and find its median
            # Form a sequence
            med_list.append(median(s[i:i+j]))
        # Set the median of medians as pivot
        # Optional: If the length of the median sequence is even
        # Take the maximum element as pivot, or take the actual median
        if len(med_list) % 2 == 0:
            pivot = int(max(med_list))
        else:
            pivot = median(med_list)
        # Get the left and right half of the sequence
        left_half, right_half = [], []
        for k in range(n):
            if s[k] != pivot:
                # Move elements smaller than the pivot to the left
                if s[k] <= pivot:
                    left_half.append(s[k])
                else:  # Move elements greater than the pivot to the right
                    right_half.append(s[k])
        # Form a new sequence
        s = left_half + [pivot] + right_half
        print(f"Updated sequence: {s}")
        # If the index of the pivot == index of the median
        if s.index(pivot) == get_index_med(s):
            print(f"=> {pivot} is the median")
            break
        else:
            print(f"=> {pivot} is not the median")


def main():
    print("Median of Medians")
    sequence = []
    n = int(input("Enter the length of the random sample: "))
    for i in range(n):
        x = float(input(f"Enter x{i + 1}: "))
        sequence.append(x)
    print(f"The median is at index {get_index_med(sequence)}")
    med_of_medians(sequence)


# Avoid running the main function
# when importing the 'module' to another program
if __name__ == "__main__":
    main()
