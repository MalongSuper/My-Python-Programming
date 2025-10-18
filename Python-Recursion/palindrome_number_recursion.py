# This program checks if a given number is a palindrome using recursion.


def check_palindrome(n, temp):
    if n == 0:
        return temp
    temp = (temp * 10) + (n % 10)

    return check_palindrome(n // 10, temp)


print("Palindrome Number (Recursion)")
number = int(input("Enter a number: "))
result = check_palindrome(number, 0)
if result == number:
    print(f"{number} is a Palindrome")
else:
    print(f"{number} is not a Palindrome")
