# Probability Distribution for random variables
from math import factorial, e
from cumulative_density_function import cumulative_density


def binomial_dist(n, k, p):  # Binomial Distribution
    C = factorial(n) // (factorial(k) * factorial(n - k))
    res = C * (p ** k) * ((1 - p) ** (n - k))
    return res


def poisson_dist(k, lamb):  # Poisson Distribution
    res = (e ** -lamb) * ((lamb ** k) / factorial(k))
    return res


def normal_dist(a, b, u, sd):  # Normal Distribution
    mui_a = cumulative_density((a - u) / sd)
    mui_b = cumulative_density((b - u) / sd)
    res = mui_b - mui_a
    return res


def main():
    print("Distribution for Random Variables")
    print("(1): Binomial Distribution")
    print("(2): Poisson Distribution")
    print("(3): Normal Distribution")
    d = int(input("Enter Distribution: "))
    if d == 1:
        print("Binomial Distribution X ~ B(n, p)")
        # n: the total number of trials
        # k: the number of events that satisfy the total trials
        n, k = eval(input("Enter n, k: "))
        # p: The probability in one trial
        p = float(input("Enter p: "))
        print(f"P(X = {k}) = {binomial_dist(n, k, p)}")
    elif d == 2:
        print("Poisson Distribution X ~ P(lambda)")
        k = int(input("Enter k: "))
        lamb = float(input("Enter lambda: "))
        print(f"P(X = {k}) = {poisson_dist(k, lamb)}")
    elif d == 3:
        print("Normal Distribution X ~ N(u, sd^2)")
        u = float(input("Enter expectation u: "))
        sd = float(input("Enter standard deviation sd: "))
        a, b = eval(input("Enter a, b: "))
        print(f"P({a} ≤ X ≤ {b}) = {normal_dist(a, b, u, sd)}")


# Avoid running the main function
# when importing the 'module' to another program
if __name__ == "__main__":
    main()
