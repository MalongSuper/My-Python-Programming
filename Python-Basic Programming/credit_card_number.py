# This program validates the credit card number by its digits
def is_valid(number):  # Define function for valid number
    separate = 0
    count = 0
    number_list = []
    valid_count = (13, 14, 15, 16)  # Valid number is between 13 and 16 digits
    while number > 0:
        digit = number % 10
        digit += separate
        number = number // 10
        number_list.append(digit)  # Make a list contains the digits
        count += 1  # Count the digits
    if count > 16:
        return False
    elif count in valid_count:
        return True


def sum_of_double_even_place(number):  # Define function to calculate the even place numbers
    if is_valid(number) is True:
        total_list = []
        count = 0
        while number > 0:  # Reverse the number
            digit = number % 10
            number = number // 10
            count += 1
            if (count % 2) == 0:
                total_list.append(get_digit(digit))  # Make a list contain the even digits
        return sum(total_list)


def get_digit(number):  # Define function to get digits from even numbers
    total = number * 2
    if total >= 10:
        digit1 = total % 10
        digit2 = total // 10
        total = digit1 + digit2
    return total


def sum_of_odd_place(number):  # Define function to calculates the odd place numbers
    odd_list = []
    count = 0
    while number > 0:  # Reverse the number
        digit = number % 10
        number = number // 10
        count += 1
        if (count % 2) != 0:
            odd_list.append(digit)  # Make a list contain the odd digits
    return sum(odd_list)


def final_sum(number):  # This special function sums the result of total list and odd list
    total_list = sum_of_double_even_place(number)
    even_list = sum_of_odd_place(number)
    result = total_list + even_list
    if result % 10 == 0:
        return True


def prefix_matched(number, d):  # Define function to determine the first digit
    num = str(number)
    prefix = str(d)  # The prefix is the first digit of the number
    return num.startswith(prefix)  # Use this function


def get_size(d):  # Define function to get the number size
    return len(str(d))


def get_prefix(number, k):  # Define function to get the prefix
    num = str(number)
    if len(num) < k:
        return number
    return int(num[:k])


def main():
    print("Credit Card Number Validation")
    # Input the number
    number = int(input("Enter a card number: "))
    # Check for all the invalid cases
    if number < 0:
        print("The Card is Invalid\nCard Number should be a positive")
    elif is_valid(number) is not True:
        print("The Card is Invalid\nCard Number should have between 13 and 16 digits.")
    elif (not prefix_matched(number, '4')
          and not prefix_matched(number, '5') and not prefix_matched(number, '37')
          and not prefix_matched(number, '6')):
        print("The Card is Invalid\nCard Number should start with the following")
        print("4 for Visa Card\n5 for MasterCard credit cards\n37 for American Express cards\n6 for Discover cards")
    elif final_sum(number) is not True:
        print("The Card is Invalid\nThe result is not divisible by 10")
    else:
        # Display if the number is valid
        print("The Card is Valid")
        if prefix_matched(number, '4'):
            print("Card Type: Visa")
        elif prefix_matched(number, '5'):
            print("Card Type: MasterCard")
        elif prefix_matched(number, '37'):
            print("Card Type: American Express")
        elif prefix_matched(number, '6'):
            print("Card Type: Discover")


# Display the result
main()
