# Class Number
from math import sin, cos, tan, log, isqrt


class Number:
    def __init__(self, number):
        self.__number = number

    def __str__(self):
        return f'{type(self.__number)} = {self.__number}'

    @property
    def getNumber(self):
        return self.__number

    @property
    def SquareRoot(self):
        return self.__number ** 0.5

    @property
    def Sin(self):
        return sin(self.__number)

    @property
    def Cos(self):
        return cos(self.__number)

    @property
    def Tan(self):
        return tan(self.__number)

    @property
    def Abs(self):
        return abs(self.__number)

    @property
    def isOdd(self):
        number = int(self.__number)
        if number < 0:
            return False
        if number % 2 != 0:
            return True
        return False

    @property
    def isEven(self):
        number = int(self.__number)
        if number < 0:
            return False
        if number % 2 == 0:
            return True
        return False

    @property
    def isPrime(self):
        number = int(self.__number)
        if number <= 1:
            return False
        if number == 2:
            return True
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    @property
    def isNegative(self):
        number = int(self.__number)
        if number < 0:
            return True
        return False

    @property
    def Reversed(self):
        reverse_number = 0
        # Create a loop that will do continuous calculation
        number = int(self.__number)
        if number < 0:
            return None
        while number > 0:
            digit = number % 10
            reverse_number = (reverse_number * 10) + digit
            number = number // 10
        return reverse_number

    @property
    def nextPrime(self):  # Get the next prime number
        # closest to the current number
        number = int(self.__number) + 1  # Start with the next number
        while True:
            if Number(number).isPrime:
                break
            number += 1  # Increment the number until a prime is found
        return number

    @property
    def Factorial(self):
        number = int(self.__number)
        if number < 0:
            return "Undefined"
        if number > 1500:  # Handle to large number
            return "Undefined"
        fact = 1
        for n in range(1, number + 1):
            # Formula : n! = n * (n-1) * (n-2) *...1
            fact *= n
        return fact

    @property
    def getDivisors(self):  # Get all divisors of the number
        divisor = []
        number = int(self.__number)
        for i in range(1, number + 1):
            if number % i == 0:
                divisor.append(i)
        return divisor

    @property
    def isPalindrome(self):  # The number is Palindrome
        # when the reverse of the number is the number itself
        number = int(self.__number)
        if Number(number).Reversed == number:
            return True
        return False

    @property
    def isPerfect(self):  # The number is perfect
        # When the sum of the divisors (excluding itself) is equal to
        # that number itself.
        divisor = []
        number = int(self.__number)
        if number < 0:
            return False
        for i in range(1, number + 1):
            if number % i == 0 and number != i:
                divisor.append(i)
        if sum(divisor) == number:
            return True
        return False

    @property
    def isFibonacci(self):  # Check if a number
        # is in Fibonacci sequence
        number = int(self.__number)
        if number < 0:
            return False
            # A number is Fibonacci if one of these expressions is a perfect square
            # Check if either 5 * n^2 + 4 or 5 * n^2 - 4 is a perfect square
        x1 = 5 * number * number + 4
        x2 = 5 * number * number - 4
        if (isqrt(x1) ** 2 == x1) or (isqrt(x2) ** 2 == x2):
            return True
        return False

    @property
    def SumOfDigits(self):
        number = int(self.__number)
        digits = [int(digit) for digit in list(str(abs(number)))]
        return sum(digits)

    @property
    def NumberOfDigits(self):
        number = int(self.__number)
        digits = [int(digit) for digit in list(str(abs(number)))]
        return len(digits)

    def isDivisible(self, divisor):  # Check if the number
        # is divisible by an input number
        number = int(self.__number)
        if number % divisor == 0:
            return True
        return False

    def Add(self, number):
        number = number.getNumber
        return self.__number + number

    def Subtract(self, number):
        number = number.getNumber
        return self.__number - number

    def Multiply(self, number):
        number = number.getNumber
        return self.__number * number

    def Divide(self, number):
        number = number.getNumber
        if number == 0:
            return "Undefined"
        return self.__number / number

    def FullDivide(self, number):
        number = number.getNumber
        if number == 0:
            return "Undefined"
        return self.__number // number

    def Exponent(self, number):
        return self.__number ** number

    def Log(self, base):
        if base < 2:
            return "Undefined"
        if self.__number < 1:
            return "Undefined"
        return log(self.__number, base)

    def RoundTo(self, decimals):
        return round(self.__number, decimals)

    @staticmethod
    def LCM(num1, num2):  # Lowest Common Multiple
        # Num1, Num2 are instances
        # Operands only support int or float, not class object
        num1 = int(num1.getNumber)  # Retrieve by getter method
        num2 = int(num2.getNumber)
        if num1 <= 0 or num2 <= 0:
            return None
        # Initialize the value of the LCM
        greater = max(num1, num2)
        while True:
            # LCM is found
            if (greater % num1 == 0) and (greater % num2 == 0):
                lcm = greater
                break
            greater += 1  # Increment to 1 for the next iteration
        return lcm

    @staticmethod
    def GCD(num1, num2):
        num1 = int(num1.getNumber)  # Retrieve by getter method
        num2 = int(num2.getNumber)
        if num1 <= 0 or num2 <= 0:
            return None
        if num1 == num2:
            gcd = num1
        else:
            divisor = max(num1, num2)
            while True:
                if (num1 % divisor == 0) and (num2 % divisor == 0):
                    gcd = divisor
                    break
                divisor -= 1
        return gcd

    # Optional methods
    @property
    def CubicRoot(self):
        return self.__number ** (1/3)

    @property
    def isArmstrong(self):  # a number is Armstrong where the
        # sum of the power of its digits equals the number itself
        # the power depends on the number of digits
        number = int(self.__number)
        if number < 0:
            return False
        digits = [int(digit) ** len(str(number)) for digit in list(str(number))]
        if sum(digits) == number:
            return True
        return False

    @property
    def isAbundant(self):  # A number is abundant
        # when the sum of its divisors, excluding itself, is greater
        # than the number itself
        number = int(self.__number)
        if number < 0:
            return False
        divisors = Number(number).getDivisors
        if sum(divisors[0:len(divisors) - 1]) > number:
            return True
        return False

    @property
    def isDeficient(self):  # A number is deficient
        # when the sum of its divisors, excluding itself, is smaller
        # than the number itself
        number = int(self.__number)
        if number < 0:
            return False
        divisors = Number(number).getDivisors
        if sum(divisors[0:len(divisors) - 1]) < number:
            return True
        return False


def main():
    num1 = Number(float(input("Enter Number 1: ")))
    num2 = Number(float(input("Enter Number 2: ")))
    print(f"+ Add: {num1.Add(num2)}")
    print(f"+ Subtract: {num1.Subtract(num2)}")
    print(f"+ Multiply: {num1.Multiply(num2)}")
    print(f"+ Divide: {num1.Divide(num2)}")
    print(f"+ Full Divide: {num1.FullDivide(num2)}")
    print(f"+ Square Root Num1: {num1.SquareRoot}; Num2: {num2.SquareRoot}")
    print(f"+ Sin: Num1: {num1.Sin}; Num2: {num2.Sin}")
    print(f"+ Cos: Num1: {num1.Cos}; Num2: {num2.Cos}")
    print(f"+ Tan: Num1: {num1.Tan}; Num2: {num2.Tan}")
    print(f"+ Abs: Num1: {num1.Abs}; Num2: {num2.Abs}")
    print(f"+ Exponential: Num1: {num1.Exponent(3)}; Num2: {num2.Exponent(2)}")
    print(f"+ Factorial: Num1: {num1.Factorial}; Num2: {num2.Factorial}")
    print(f"+ Log: Num1: {num1.Log(2)}; Num2: {num2.Log(10)}")
    print(f"+ GCD: {Number.GCD(num1, num2)}")
    print(f"+ LCM: {Number.LCM(num1, num2)}")
    print(f"+ Reversed: Num1: {num1.Reversed}; Num2: {num2.Reversed}")
    print(f"+ Round to 2 decimals: {num1.RoundTo(2)}; Num2: {num2.RoundTo(2)}")
    print(f"+ Is Odd? Num1: {num1.isOdd}; Num2: {num2.isOdd}")
    print(f"+ Is Even? Num1: {num1.isEven}; Num2: {num2.isEven}")
    print(f"+ Is Negative? Num1: {num1.isNegative}; Num2: {num2.isNegative}")
    print(f"+ Is Prime? Num1: {num1.isPrime}; Num2: {num2.isPrime}")
    print(f"+ Is Palindrome? Num1: {num1.isPalindrome}; Num2: {num2.isPalindrome}")
    print(f"+ Is Perfect? Num1: {num1.isPerfect}; Num2: {num2.isPerfect}")
    print(f"+ Is Fibonacci? Num1: {num1.isFibonacci}; Num2: {num2.isFibonacci}")
    print(f"+ Is Divisible by 2? Num1: {num1.isDivisible(2)}; Num2: {num2.isDivisible(2)}")
    print(f"+ Is Divisible by 3? Num1: {num1.isDivisible(3)}; Num2: {num2.isDivisible(3)}")
    print(f"+ Is Divisible by 4? Num1: {num1.isDivisible(4)}; Num2: {num2.isDivisible(4)}")
    print(f"+ Is Divisible by 5? Num1: {num1.isDivisible(5)}; Num2: {num2.isDivisible(5)}")
    print(f"+ Is Divisible by 9? Num1: {num1.isDivisible(9)}; Num2: {num2.isDivisible(9)}")
    print(f"+ Get Divisors: Num1: {num1.getDivisors}; Num2: {num2.getDivisors}")
    print(f"+ Next Prime? Num1: {num1.nextPrime}; Num2: {num2.nextPrime}")
    print(f"+ Sum of Digits: Num1: {num1.SumOfDigits}; Num2: {num2.SumOfDigits}")
    print(f"+ Number of Digits: Num1: {num1.NumberOfDigits}; Num2: {num2.NumberOfDigits}")
    print(f"+ Cubic Root: Num1: {num1.CubicRoot}; Num2: {num2.CubicRoot}")
    print(f"+ Is Armstrong? Num1: {num1.isArmstrong}; Num2: {num2.isArmstrong}")
    print(f"+ Is Abundant? Num1: {num1.isAbundant}; Num2: {num2.isAbundant}")
    print(f"+ Is Deficient? Num1: {num1.isDeficient}; Num2: {num2.isDeficient}")


if __name__ == "__main__":
    main()
