# Maximize a function subject to the following constraints
# 0 ≤ x ≤ 1; 0 ≤ y ≤ 2; x + y ≤ 2
# Using experimental methods


def experimental_methods(f):  # f: objective function
    # x in [0, 1]; y in [0, 2]; x + y <= 2: Decision variables
    # With constraints x + y ≤ 2, what is max(f(x,y))
    # Try (x = 0, y = 0); (x = 0, y = 1); (x = 0, y = 2);
    # (x = 1, y = 0); (x = 1, y = 1); (x = 1, y = 2)
    max_value = float('inf')
    res = 0
    xy = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1]]
    for i in range(len(xy)):
        res = f(xy[i][0], xy[i][1])
        if res < max_value:
            max_value = res
    print(res)


def main():
    print("Find maximize in equation (Constraints)")
    fxy = input("Enter exact equation f(x): ")
    fxy_lambda = eval(f"lambda x, y: {fxy}")
    print("The maximum of this function is", end=" ")
    experimental_methods(fxy_lambda)


main()
