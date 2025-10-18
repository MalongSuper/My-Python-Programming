# Given a string, find out repeated characters

def repeated_chars(strings):
    char_count = {}
    repeated_list = []
    # Count occurrence of each character in string
    for s in strings:  # A dictionary will be created
        # Keys are characters, Items are set to 1 as default
        if s in char_count:
            char_count[s] += 1
        else:
            char_count[s] = 1  # Add 1 count as the item of the key
    # Check if there are any repeated characters
    for char, count in char_count.items():
        if count > 1:
            repeated_list.append(char)
    if len(repeated_list) > 0:
        return repeated_list
    else:
        return None


def main():
    print("Find out repeated characters in String")
    string = str(input("Enter a String: "))
    print("String:", string)
    result = repeated_chars(string)
    if result is not None:
        print(f"Repeated characters: {result}")
    else:
        print(f"No repeated characters found")


main()
