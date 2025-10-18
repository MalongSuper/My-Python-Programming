# Richardson Extrapolation with approximate O(n^4)

def richardson_extrapolation(fx, h1, h2):
    # Compute g(h1) and g(h2) using Finite Difference
    g_h1 = (fx[1] - fx[0]) / h1  # f'(0) with h1
    g_h2 = (fx[2] - fx[0]) / h2  # f'(0) with h2
    # Apply Richardson Extrapolation with p = 2
    p = 2
    G = (p ** 2 * g_h1 - g_h2) / 3
    return G


def main():
    print("Richardson Extrapolation")
    # Enter values
    n = int(input("Enter number of values: "))
    x_values, fx_values = [], []
    for i in range(n):
        x, fx = map(float, input(f"Enter x[{i}], f(x[{i}]): ").split(","))
        x_values.append(x)
        fx_values.append(fx)
    # Enter step size h1 and h2
    h1, h2 = map(float, input(f"Enter h1 and h2: ").split(","))
    # h2 must be greater than h1
    if h2 <= h1:
        print("Error: h2 must be greater than h1")
        return
    # Richardson Extrapolation
    f1 = richardson_extrapolation(fx_values, h1, h2)
    print(f"f'(0): {f1}")


main()
