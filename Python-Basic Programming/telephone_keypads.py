# This program simulates numbers and letters typed for telephones
def get_number(uppercase_letter):  # Define function to get the number
    # Make a list
    one_list = ['A', 'B', 'C', 'a', 'b', 'c']
    two_list = ['D', 'E', 'F', 'd', 'e', 'f']
    three_list = ['G', 'H', 'I', 'g', 'h', 'i']
    four_list = ['J', 'K', 'L', 'j', 'k', 'l']
    five_list = ['M', 'N', 'O', 'm', 'n', 'o']
    six_list = ['P', 'Q', 'R', 'S', 'p', 'q', 'r', 's']
    seven_list = ['T', 'U', 'V', 't', 'u', 'v']
    eight_list = ['W', 'X', 'Y', 'Z', 'w', 'x', 'y', 'z']
    upper_list = list(uppercase_letter)
    # Checking each index by for loop
    for index in range(len(upper_list)):
        # Indicate if statement to change the characters to numeric values
        if upper_list[index] in one_list:
            upper_list[index] = '2'
        if upper_list[index] in two_list:
            upper_list[index] = '3'
        if upper_list[index] in three_list:
            upper_list[index] = '4'
        if upper_list[index] in four_list:
            upper_list[index] = '5'
        if upper_list[index] in five_list:
            upper_list[index] = '6'
        if upper_list[index] in six_list:
            upper_list[index] = '7'
        if upper_list[index] in seven_list:
            upper_list[index] = '8'
        if upper_list[index] in eight_list:
            upper_list[index] = '9'

    result = ''.join(map(str, upper_list))
    print(result)


def main():  # Define main function
    print("Telephone Number")
    tele_num = str(input("Enter a String: "))
    print("The Telephone Number is", end=" ")
    get_number(tele_num)


# Display the result
main()