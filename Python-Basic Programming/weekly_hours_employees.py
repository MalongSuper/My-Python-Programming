# This program computes the weekly hours for all employees
def main():
    print("Employees Weekly Hours")
    a1, a2, a3, a4, a5, a6, a7 = eval(input("Enter Employee 0 weekly hours: "))
    b1, b2, b3, b4, b5, b6, b7 = eval(input("Enter Employee 1 weekly hours: "))
    c1, c2, c3, c4, c5, c6, c7 = eval(input("Enter Employee 2 weekly hours: "))
    d1, d2, d3, d4, d5, d6, d7 = eval(input("Enter Employee 3 weekly hours: "))
    e1, e2, e3, e4, e5, e6, e7 = eval(input("Enter Employee 4 weekly hours: "))
    f1, f2, f3, f4, f5, f6, f7 = eval(input("Enter Employee 5 weekly hours: "))
    g1, g2, g3, g4, g5, g6, g7 = eval(input("Enter Employee 6 weekly hours: "))
    h1, h2, h3, h4, h5, h6, h7 = eval(input("Enter Employee 7 weekly hours: "))
    # Heading of the table
    print()
    print("\t\t\tSu Mo Tu We Th Fr Sa\tTotal Hours")
    # Make a list of employee number
    employee_list = ['Employee 0', 'Employee 1', 'Employee 2', 'Employee 3',
                     'Employee 4', 'Employee 5', 'Employee 6', 'Employee 7']
    # Make a list contain the hour
    hour_matrix = [[a1, a2, a3, a4, a5, a6, a7],
                   [b1, b2, b3, b4, b5, b6, b7],
                   [c1, c2, c3, c4, c5, c6, c7],
                   [d1, d2, d3, d4, d5, d6, d7],
                   [e1, e2, e3, e4, e5, e6, e7],
                   [f1, f2, f3, f4, f5, f6, f7],
                   [g1, g2, g3, g4, g5, g6, g7],
                   [h1, h2, h3, h4, h5, h6, h7]]
    # Calculate the sum of hours
    sum_hour_matrix = [sum(hours) for hours in hour_matrix]
    # Sort the values based on the sum of the hours
    sorted_hour_matrix = sorted(zip(employee_list, hour_matrix, sum_hour_matrix),
                                key=lambda x: sum(x[1]), reverse=True)
    # Display the table
    for employee, hours, total in sorted_hour_matrix:
        print(employee, "\t", '  '.join(map(str, hours)), "\t\t", total)


# Display the result
main()
