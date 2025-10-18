# Predict House Price with Linear Regression
# Single feature "Area"


def find_regression(matrix, x, y):
    n = len(matrix)
    # Find the required values
    total_x = sum(x)
    total_y = sum(y)
    total_xy = sum([x[i] * y[i] for i in range(len(x))])
    total_squared_x = sum([x[i] ** 2 for i in range(len(x))])
    total_x_squared = sum(x) ** 2
    # Calculate B using the Regression formula
    b = (((n * total_xy) - (total_x * total_y)) /
         (n * total_squared_x - total_x_squared))
    a = (total_y - b * total_x) / n
    return a, b


def min_max_scalar(x):
    n = len(x)
    x_normal = []
    for i in range(n):
        xi_normal = (x[i] - min(x)) / (max(x) - min(x))
        x_normal.append(xi_normal)
    return x_normal


def compute_r2(original_y, original_x, a, b):  # For only one feature
    predict_y = []
    # Only use the testing data
    mean_y = sum(original_y) / len(original_y)  # Mean of Y
    for i in range(len(original_y)):
        # Get all the predicted_y
        pred_y = a + (b * original_x[i])
        predict_y.append(pred_y)
    # Determine R2 score
    ss_res = sum((original_y[i] - predict_y[i]) ** 2 for i in range(len(original_y)))
    ss_tot = sum((original_y[i] - mean_y) ** 2 for i in range(len(original_y)))
    if ss_tot == 0:
        return 0
    return 1 - (ss_res / ss_tot)


def main():
    print("Linear Regression House Pricing")
    matrix = []
    # These are the sample data to input
    # area = [2000, 1800, 2200, 1500, 3000, 2800, 1700, 1600, 2400, 2750]
    # price = [400, 330, 369, 232, 540, 500, 299, 260, 410, 485]
    print("(1) Training and R2 Score")
    number = int(input("Enter the length of the table: "))
    for k in range(number):
        Xi, Yi = eval(input(f"Enter Area{k + 1} and Price{k + 1}: "))
        matrix.append([Xi, Yi])  # Append tp list
    # X: The first column, Y: The second column
    area = [matrix[i][0] for i in range(len(matrix))]
    price = [matrix[i][1] for i in range(len(matrix))]
    area_normalized = min_max_scalar(area)  # Normalize the area
    # Take out the first and the last values
    matrix_normalized = []
    # Determine a train size, 80% Training, 20% Testing
    train_size = int(0.8 * len(matrix))
    area_train, price_train = area_normalized[:train_size], price[:train_size]
    area_test, price_test = area_normalized[train_size:], price[train_size:]
    for i in range(len(price_train)):
        # Form a matrix with the elements in price and area_normalized
        matrix_normalized.append([area_train[i], price_train[i]])
    # Find the slope (B) and intercept (A)
    A, B = find_regression(matrix_normalized, area_train, price_train)
    print(f"+ Linear Equation: Y = {A} + {B} * X")
    # Compute R2 for testing data
    print(f"+ R2 score (testing data): {compute_r2(price_test, area_test, A, B)}")
    # Testing the linear equation
    print("(2) Testing")
    input_test = float(input("Enter an area for testing: "))
    # Normalize this data
    input_test_normal = (input_test - min(area)) / (max(area) - min(area))
    price_predict = A + (B * input_test_normal)
    print(f"Predicted Price for area = {input_test}: {price_predict}")


main()
