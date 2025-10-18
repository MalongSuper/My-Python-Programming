# Find k-th smallest and largest elements in a sequence


def median(s):  # Median
    s = sorted(s)
    if len(s) % 2 == 0:  # If length is even
        k = len(s) // 2  # n = 2k
        return 0.5 * (s[k - 1] + s[k])
    else:  # If length is odd
        k = (len(s) - 1) // 2  # n = 2k + 1
        return s[k]


def basic_approach(arr, k):
    arr = sorted(arr)
    # arr[k - 1] is the smallest element, arr[len(arr) - K] is the largest element
    return arr[k - 1], arr[len(arr) - k]


def get_index_kth(s, k_element):  # Get the index of the k-th smallest and largest element
    n = len(s)
    return k_element - 1, n - k_element


def kth_largest(s, k_element):  # Using median of medians to find the k-th largest element
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
        if s.index(pivot) == get_index_kth(s, k_element)[1]:
            print(f"=> {pivot} is the {k_element}-th largest element")
            return pivot
        else:
            print(f"=> {pivot} is not the {k_element}-th largest element")
            # Set the new sequence to the left or right half
            if s.index(pivot) < get_index_kth(s, k_element)[1]:
                s = right_half
            else:
                s = left_half


def kth_smallest(s, k_element):  # Using median of medians to find the k-th smallest element
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
        if s.index(pivot) == get_index_kth(s, k_element)[0]:
            print(f"=> {pivot} is the {k_element}-th smallest element")
            return pivot
        else:
            # Set the new sequence to the left or right half
            if s.index(pivot) < get_index_kth(s, k_element)[0]:
                s = right_half
            else:
                s = left_half


def main():
    array = []
    n = int(input("Enter the length of the array: "))
    for i in range(n):
        x = float(input(f"Enter x{i + 1}: "))
        array.append(x)
    print("Array:", sorted(array))
    k = int(input("Enter a value for k: "))
    # Find k-th smallest and largest elements using the basic approach
    print("Basic Approach")
    smallest_k, largest_k = basic_approach(array, k)
    print(f"{k}-th smallest element: {smallest_k}")
    print(f"{k}-th largest element: {largest_k}")
    # Find the k-th largest element using the median of medians approach
    print("\nMedian of Medians Approach - Kth Largest Element")
    print(f"The {k}-th largest element is at index {get_index_kth(array, k)[1]}")
    print(f"The {k}-th largest element is {kth_largest(array, k)}")
    print("\nMedian of Medians Approach - Kth Smallest Element")
    print(f"The {k}-th smallest element is at index {get_index_kth(array, k)[0]}")
    print(f"The {k}-th smallest element is {kth_smallest(array, k)}")


main()
