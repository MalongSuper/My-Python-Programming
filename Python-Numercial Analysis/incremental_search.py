# Incremental Search Method to find solutions of equation
# Find the incremental, each increment is a dx
# To understand about this method
# Watch this video: https://www.youtube.com/watch?v=Dl5NkWdLTEE
import numpy as np
import matplotlib.pyplot as plt


def root_search(f, a, b, dx):
    x1 = a
    f1 = f(x1)
    x2 = a + dx
    f2 = f(x2)
    while np.sign(f1) == np.sign(f2):
        if x1 >= b:
            return None, None
        x1 = x2
        f1 = f2
        x2 = x1 + dx
        f2 = f(x2)
    return x1, x2


def main():
    print("Incremental Search Method")
    # Input equation
    fx = input("Enter equation f(x): ")
    a, b = eval(input("Select interval (a, b): "))
    dx = float(input("Select dx: "))
    # Draw a plot
    func = eval("lambda x:" + fx.replace("^", "**"))
    x = np.linspace(-10, 10, 400)
    y = func(x)

    plt.figure(figsize=(10, 6))
    plt.title(f"Function f(x) = {fx}")
    plt.plot(x, y, label=f"f(x) = {fx}")
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()
    # Find the solutions
    root = root_search(func, a, b, dx)
    if root != (None, None):
        print(f"Solutions for f(x): {root}")
        plt.plot(root, [func(root[0]), func(root[1])], 'ro')
        plt.text(root[0], func(root[0]), f"{root}", fontsize=12, verticalalignment='bottom')
    else:
        print("The equation has no solution")

    plt.show()


main()
