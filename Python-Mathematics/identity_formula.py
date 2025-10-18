# This program convert a formula to its identity

def identity(n, a, b):  # There are 7 identities
    if n == 1:
        print(f"1. ({a} + {b})^2 =", end=" ")
        print(f"({a})^2 + (2 * {a} * {b}) + ({b})^2", end=" ")
        print(f"= {a ** 2 + (2 * a * b) + b ** 2}")
    elif n == 2:
        print(f"2. ({a} - {b})^2 =", end=" ")
        print(f"({a})^2 - (2 * {a} * {b}) + ({b})^2", end=" ")
        print(f"= {a ** 2 - (2 * a * b) + b ** 2}")
    elif n == 3:
        print(f"3. ({a})^2 - ({b})^2 =", end=" ")
        print(f"({a} - {b}) * ({a} + {b})", end=" ")
        print(f"= {(a - b) * (a + b)}")
    elif n == 4:
        print(f"4. ({a} + {b})^3 =", end=" ")
        print(f"({a})^3 + (3 * ({a})^2 * {b}) + (3 * {a} * ({b})^2) + ({b})^3", end=" ")
        print(f"= {a ** 3 + (3 * a ** 2 * b) + (3 * a * b ** 2) + b ** 3}")
    elif n == 5:
        print(f"5. ({a} - {b})^3 =", end=" ")
        print(f"({a})^3 - (3 * ({a})^2 * {b}) + (3 * {a} * ({b})^2) - ({b})^3", end=" ")
        print(f"= {a ** 3 - (3 * a ** 2 * b) + (3 * a * b ** 2) - b ** 3}")
    elif n == 6:
        print(f"6. ({a})^3 + ({b})^3 =", end=" ")
        print(f"({a} + {b}) * (({a})^2 - ({a} * {b}) + ({b})^2)", end=" ")
        print(f"= {(a + b) * (a ** 2 - (a * b) + b ** 2)}")
    elif n == 7:
        print(f"7. ({a})^3 - ({b})^3 =", end=" ")
        print(f"({a} - {b}) * (({a})^2 + ({a} * {b}) + ({b})^2)", end=" ")
        print(f"= {(a - b) * (a ** 2 + (a * b) + b ** 2)}")
    else:
        print("Invalid Input")


def main():
    print("Identity")
    a, b = eval(input("Enter a, b: "))
    number = int(input("Identity number: "))
    identity(number, a, b)


main()
