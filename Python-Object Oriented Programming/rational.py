# Class Rational

class Rational:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        if denominator == 0:
            raise ValueError("Divided by zero")

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    @staticmethod
    def lcm(numerator, denominator):  # Lowest Common Multiple
        # Initialize the value of the LCM
        if numerator > denominator:
            greater = numerator
        else:
            greater = denominator
        while True:
            # LCM is found
            if (greater % numerator == 0) and (greater % denominator == 0):
                lcm = greater
                break
            greater += 1  # Increment to 1 for the next iteration
        return lcm

    @staticmethod
    def gcd(numerator, denominator):
        if numerator == denominator:
            gcd = numerator
        else:
            if numerator > denominator:
                divisor = numerator
            else:
                divisor = denominator
            while True:
                if (denominator % divisor == 0) and (numerator % divisor == 0):
                    gcd = divisor
                    break
                divisor -= 1
        return gcd

    def add_rational(self, to_rational):  # Add two rationals, return the rational
        # Get the LCM for both fractions
        lcm = self.lcm(self.denominator, to_rational.denominator)
        self.numerator, self.denominator = (self.numerator * (lcm // self.denominator),
                                            self.denominator * (lcm // self.denominator))
        # Convert two components of the fraction to the same denominator
        to_rational.numerator, to_rational.denominator = (to_rational.numerator * (lcm // to_rational.denominator),
                                                          to_rational.denominator * (lcm // to_rational.denominator))
        res_numerator = self.numerator + to_rational.numerator
        res_denominator = self.denominator
        return (f"{res_numerator // self.gcd(res_numerator, res_denominator)}"
                f"/{res_denominator // self.gcd(res_numerator, res_denominator)}")

    def add_decimal(self, to_rational):  # Add two rationals, return the decimal
        return ((self.numerator / self.denominator)
                + (to_rational.numerator / to_rational.denominator))

    def subtract_rational(self, to_rational):  # Subtract two rationals, return the rational
        # Get the LCM for both fractions
        lcm = self.lcm(self.denominator, to_rational.denominator)
        self.numerator, self.denominator = (self.numerator * (lcm // self.denominator),
                                            self.denominator * (lcm // self.denominator))
        # Convert two components of the fraction to the same denominator
        to_rational.numerator, to_rational.denominator = (to_rational.numerator * (lcm // to_rational.denominator),
                                                          to_rational.denominator * (lcm // to_rational.denominator))
        res_numerator = self.numerator - to_rational.numerator
        res_denominator = self.denominator
        return (f"{res_numerator // self.gcd(res_numerator, res_denominator)}"
                f"/{res_denominator // self.gcd(res_numerator, res_denominator)}")

    def subtract_decimal(self, to_rational):  # Subtract two rationals, return the decimal
        return ((self.numerator / self.denominator)
                - (to_rational.numerator / to_rational.denominator))

    def multiply_rational(self, to_rational):  # Multiply two rationals, return the rational
        res_numerator = self.numerator * to_rational.numerator
        res_denominator = self.denominator * to_rational.denominator
        return (f"{res_numerator // self.gcd(res_numerator, res_denominator)}"
                f"/{res_denominator // self.gcd(res_numerator, res_denominator)}")

    def multiply_decimal(self, to_rational):  # Multiply two rationals, return the decimal
        return ((self.numerator / self.denominator)
                * (to_rational.numerator / to_rational.denominator))

    def divide_rational(self, to_rational):  # Divide two rationals, return the rational
        res_numerator = self.numerator * to_rational.denominator
        res_denominator = self.denominator * to_rational.numerator
        return (f"{res_numerator // self.gcd(res_numerator, res_denominator)}"
                f"/{res_denominator // self.gcd(res_numerator, res_denominator)}")

    def divide_decimal(self, to_rational):  # Divide two rationals, return the decimal
        return ((self.numerator / self.denominator)
                / (to_rational.numerator / to_rational.denominator))

    def to_string(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"


def main():
    rational = Rational()
    print(f"Initial: {rational.numerator}/{rational.denominator}")
    n1, d1 = eval(input("Enter a rational 1 (n1, d1): "))
    n2, d2 = eval(input("Enter a rational 2 (n2, d2): "))
    rational1 = Rational(n1, d1)
    rational2 = Rational(n2, d2)
    print(f"Rational 1: {rational1.to_string()}")
    print(f"Rational 2: {rational2.to_string()}")
    print(f"Add: {rational1.add_rational(rational2)}")
    print(f"Subtract: {rational1.subtract_rational(rational2)}")
    print(f"Multiply: {rational1.multiply_rational(rational2)}")
    print(f"Divide: {rational1.divide_rational(rational2)}")


main()
