# This program finds the longest common prefix
def prefix(s1, s2):  # Define the function to find the longest common prefix
    prefix_list = []
    # Find the minimum of length
    min_length = min(len(s1), len(s2))
    # Use loop to find the prefix
    for mint in range(min_length):
        if s1[mint] != s2[mint]:  # Break the loop when the value is different
            break
        else:
            # If value in the index is the same
            prefix_list.append(s1[mint])  # Append it to the list

    return ''.join(prefix_list)


def main():  # Define main function
    print("Longest Common Prefix")
    string1 = str(input("String 1: "))
    string2 = str(input("String 2: "))
    prefix_result = prefix(string1, string2)
    if prefix_result:
        print("The Longest Common Prefix is:", prefix_result)
    else:
        print("No Longest Common Prefix Found")


# Display the result
main()
