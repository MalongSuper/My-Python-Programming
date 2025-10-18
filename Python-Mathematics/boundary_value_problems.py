# Solve the Boundary Value Problem - BVP
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import bisect
import matplotlib.pyplot as plt


# Convert to ODE system
def ode_system(x, Y, f_lambda):
    y, v = Y
    return [v, f_lambda(x, y)]


# Shooting Method
def shooting_method(f_lambda, a, b, y_a, v_b, g1, g2):
    # Residual Function
    def residual(s):
        x_init = [a, b]
        y_init = [y_a, s]
        sol = solve_ivp(lambda x, Y: ode_system(x, Y, f_lambda),
                        x_init, y_init, dense_output=True)
        yb, vb = sol.y[:, -1]
        return vb - v_b

    # Correct slope with bisection
    s_star = bisect(residual, g1, g2)
    x_init = [a, b]
    y_init_new = [y_a, s_star]
    x_eval = np.linspace(a, b, 200)
    sol = solve_ivp(lambda x, Y: ode_system(x, Y, f_lambda),
                    x_init, y_init_new, t_eval=x_eval)

    return sol, s_star


def main():
    # Sample: -4 * y + 4 * x, y(0) = 0; y'(np.pi/2) = 3
    f = input("Enter equation f(x): ")
    f_lambda = eval(f"lambda x, y: {f}")
    # a = 0; b = np.pi
    a, b = eval(input("Enter interval a, b: "))
    # y(a) = 0; y'(b) = 3
    y_a, v_b = eval(input("Enter y(a) and y'(b): "))
    # Take initial guesses for y'(0)
    guess1, guess2 = -5.0, 5.0
    sol, slope = shooting_method(f_lambda, a, b, y_a, v_b, guess1, guess2)
    print(f"Optimal initial slope y'(0): {slope:.6f}")
    print(f"Final y(b): {sol.y[0, -1]:.6f}; y'(b) = {sol.y[1, -1]:.6f}")

    # Plot numerical solution
    plt.plot(sol.t, sol.y[0], label="Shooting solution")
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.legend()
    plt.grid()
    plt.show()


main()
