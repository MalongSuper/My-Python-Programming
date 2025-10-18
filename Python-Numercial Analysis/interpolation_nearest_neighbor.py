# Find the curve of order 2 P(x) = a0 + a1x + a2x^2
# going through 3 points using the Least Square Fit Method
# Then use the Central Finite Difference to find the derivative
import numpy as np


# The function to use the central difference formula
def central_finite_difference(f, x, h, diff=1):
    if diff == 1:
        return (f(x + h) - f(x - h)) / (2 * h)
    elif diff == 2:
        return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)
    else:
        print("Only first and second derivatives are supported")


# Solve the above problem with the Polynomial Fit
# Y = AB, f0(x) = 1; f1(x) = x; f2(x) = x^2
# basic function: x^2, x^1, x^0
# Construct the matrix A with three column
def least_square_fit(x, fx):
    x, fx = np.array(x), np.array(fx)
    A = np.vstack([x ** 2, x, np.ones(len(x))]).T
    Y = fx.T
    # Use numpy.linalg.lstsq
    a = np.linalg.lstsq(A, Y, rcond=None)[0]
    print(f"f(x) = ({a[2]:.4f}) + ({a[1]:.4f}) * x + ({a[0]:.4f} * x^2)")
    # Store the function
    f_result = f'({a[2]}) + ({a[1]}) * x + ({a[0]}) * x^2'
    f = eval("lambda x:" + f_result.replace("^", "**"))
    return f


def main():
    # Sample Input:
    # Enter the x values: 1.5,1.9,2.1,2.4,2.6,3.1
    # Enter the f(x) values: 1.0628,1.3961,1.5432,1.7349,1.8423,2.0397
    # Enter the computed x: 2
    print("Least Square Fit Method - Nearest Neighbor Points")
    x = list(map(float, input("Enter the x values: ").split(",")))
    fx = list(map(float, input("Enter the f(x) values: ").split(",")))
    x_value = float(input("Enter the computed x: "))

    if len(x) != len(fx):
        raise ValueError("The length of x and y does not match")
    elif len(x) < 3 or len(fx) < 3:
        raise ValueError("At least three points are required for x and y")

    candidate_x, candidate_fx = [], []
    for i in range(len(x)):
        # Find all the three points
        if len(x[i:i+3]) == 3:
            # Take the one where the x_value might lie within
            # This number must be greater than the min
            # and lower than the max of that sub-data points
            if min(x[i:i + 3]) < x_value < max(x[i:i + 3]):
                candidate_x.append(x[i:i+3])
                candidate_fx.append(fx[i:i+3])
    # Once we have the candidate points, we need to pick the one whose points are the closest.
    minimum_distance = float('+inf')
    selected_x, selected_fx = [], []
    for j in range(len(candidate_x)):
        # Compute distance metric
        distance = (abs(candidate_x[j][0] - candidate_x[j][1])
                    + abs(candidate_x[j][1] - candidate_x[j][2]))
        if distance < minimum_distance:
            selected_x = candidate_x[j]
            selected_fx = candidate_fx[j]

    print("Selected data points: x =", selected_x)
    f = least_square_fit(selected_x, selected_fx)
    dx1 = central_finite_difference(f, x_value, 0.001, diff=1)
    dx2 = central_finite_difference(f, x_value, 0.001, diff=2)
    print(f"f'({x_value}) = {dx1}")
    print(f"f''({x_value}) = {dx2}")


main()
