# This program reverses the digits of given number

def digits(n):  # This function return the number of digits
    d = 1
    while n // 10 != 0:
        d += 1
        n = n // 10
    return d


def reverse_number(n):
    if digits(n) == 1:
        return n
    else:
        num = n // 10
        rev = reverse_number(num)
        dev = digits(rev)

        temp = (n % 10) * (10 ** dev) + rev
        return temp


print("Reversed Number (Recursion)")
number = int(input("Enter a number: "))
result = reverse_number(number)
print("The Reversed Number:", result)
