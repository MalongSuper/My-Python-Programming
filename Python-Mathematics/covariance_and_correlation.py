# Covariance and Correlation Matrix 3x3
from random_sample_values import total, sample_mean


def covariance_matrix(x, y, z):
    cov_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    n = len(x)  # Assume the length of every matrix is similar

    # Find the squared difference of x[i] and mean
    var_x = [(x[i] - sample_mean(x)) ** 2 for i in range(n)]
    var_y = [(y[i] - sample_mean(y)) ** 2 for i in range(n)]
    var_z = [(z[i] - sample_mean(z)) ** 2 for i in range(n)]
    # Cov(X, X); Cov(Y, Y); (Cov(Z, Z))
    cov_x = total(var_x) / (n - 1)
    cov_y = total(var_y) / (n - 1)
    cov_z = total(var_z) / (n - 1)
    # Substitute to the diagonal entries
    cov_matrix[0][0], cov_matrix[1][1], cov_matrix[2][2] = cov_x, cov_y, cov_z

    # Calculate the other entries
    var_xy = [(x[i] - sample_mean(x)) * (y[i] - sample_mean(y)) for i in range(n)]
    cov_xy = total(var_xy) / (n - 1)
    cov_matrix[0][1], cov_matrix[1][0] = cov_xy, cov_xy

    var_xz = [(x[i] - sample_mean(x)) * (z[i] - sample_mean(z)) for i in range(n)]
    cov_xz = total(var_xz) / (n - 1)
    cov_matrix[0][2], cov_matrix[2][0] = cov_xz, cov_xz

    var_yz = [(y[i] - sample_mean(y)) * (z[i] - sample_mean(z)) for i in range(n)]
    cov_yz = total(var_yz) / (n - 1)
    cov_matrix[1][2], cov_matrix[2][1] = cov_yz, cov_yz

    return cov_matrix


def correlation_matrix(cov_matrix):
    # The diagonal entry is 1
    corr_matrix = [[1.0, 0, 0], [0, 1.0, 0], [0, 0, 1.0]]
    # Take the diagonal entries
    cov_x, cov_y, cov_z = cov_matrix[0][0], cov_matrix[1][1], cov_matrix[2][2]
    # Standard Deviation
    sd_x, sd_y, sd_z = cov_x ** 0.5, cov_y ** 0.5, cov_z ** 0.5

    # Calculate the correlation and substitute to the corr_matrix
    cov_xy = cov_matrix[1][0]
    corr_xy = cov_xy / (sd_x * sd_y)
    corr_matrix[1][0], corr_matrix[0][1] = corr_xy, corr_xy

    cov_xz = cov_matrix[2][0]
    corr_xz = cov_xz / (sd_x * sd_z)
    corr_matrix[2][0], corr_matrix[0][2] = corr_xz, corr_xz

    cov_yz = cov_matrix[1][2]
    corr_yz = cov_yz / (sd_y * sd_z)
    corr_matrix[1][2], corr_matrix[2][1] = corr_yz, corr_yz

    return corr_matrix


def main():
    print("Covariance and Correlation Matrix")
    number = int(input("Enter number of values: "))
    matrix = []
    for i in range(number):
        xi, yi, zi = eval(input(f"Enter X{i + 1}, Y{i + 1}, Z{i + 1}: "))
        matrix.append([xi, yi, zi])
    x = [matrix[i][0] for i in range(len(matrix))]
    y = [matrix[i][1] for i in range(len(matrix))]
    z = [matrix[i][2] for i in range(len(matrix))]

    # Get the covariance matrix and display it
    cov_matrix = covariance_matrix(x, y, z)
    print("Covariance Matrix: [")
    for i in cov_matrix:
        print(i)
    print("]")
    # Get the correlation matrix and display it
    print()
    corr_matrix = correlation_matrix(cov_matrix)
    print("Correlation Matrix: [")
    for j in corr_matrix:
        print(j)
    print("]")


# Avoid running the main function
# when importing the 'module' to another program
if __name__ == "__main__":
    main()
