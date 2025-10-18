# Finite Difference Approximations with approximate O(n^2)

# f[i]: value of f(x) at x[i]
# f[i + 1]: value of f(x) at x[i + 1]
def difference_first(f, h, i, method='forward'):
    if method == "forward":
        return (f[i + 1] - f[i]) / h
    elif method == "backward":
        return (f[i] - f[i - 1]) / h
    elif method == "center":
        return (f[i + 1] - f[i - 1]) / (2 * h)


def difference_second(f, h, i, method='forward'):
    if method == "forward":
        return (f[i + 2] - 2 * f[i + 1] + f[i]) / (h ** 2)
    elif method == "backward":
        return (f[i] - 2 * f[i - 1] + f[i - 2]) / (h ** 2)
    elif method == "center":
        return (f[i + 1] - 2 * f[i] + f[i - 1]) / (h ** 2)


def main():
    print("Finite Difference Approximations")
    # Enter values
    n = int(input("Enter number of values: "))
    x_values, fx_values = [], []
    for i in range(n):
        x, fx = map(float, input(f"Enter x[{i}], f(x[{i}]): ").split(","))
        x_values.append(x)
        fx_values.append(fx)

    h = float(input("Enter h: "))
    x_point = float(input("Enter point x: "))
    # Find index of value x
    try:
        index_x_point = x_values.index(x_point)
    except ValueError as e:
        print(e)
        return
    # Check the condition
    if index_x_point == 0:  # Use difference forward
        f1 = difference_first(fx_values, h, index_x_point, 'forward')
        f2 = difference_second(fx_values, h, index_x_point, 'forward')
    elif index_x_point == n - 1:  # Use difference backward
        f1 = difference_first(fx_values, h, index_x_point, 'backward')
        f2 = difference_second(fx_values, h, index_x_point, 'backward')
    else:  # Use difference center
        f1 = difference_first(fx_values, h, index_x_point, 'center')
        f2 = difference_second(fx_values, h, index_x_point, 'center')
    # Display the result
    print(f"* f'({x_point}) = {f1}")
    print(f"* f''({x_point}) = {f2}")


main()
