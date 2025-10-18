# Traveling salesman problem (sub-tour elimination constraint)
from ortools.linear_solver import pywraplp


# D: distances matrix; sub-tour[[]]: 2D-list, set of sub-tours
def solve_tsp_eliminate(d, sub_tours=None):
    if sub_tours is None:
        sub_tours = []
    solver = pywraplp.Solver('TSP', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    n = len(d)
    # Decision variables
    x = [[solver.IntVar(0, 0 if d[i][j] == 0 else 1, "x[%d,%d]" % (i, j))
          for j in range(n)] for i in range(n)]
    # Constraints
    for i in range(n):
        solver.Add(solver.Sum(x[i][j] for j in range(n)) == 1)
        solver.Add(solver.Sum(x[j][i] for j in range(n)) == 1)
        solver.Add(x[i][i] == 0)
    # Sub-tour elimination constraints
    # An arbitrary sub-tour => The total of arcs is equal to the vertex
    # Exclude forming sub-tour by constraining the total of arcs
    for sub in sub_tours:
        solver.Add(solver.Sum(x[i][j] for i in sub for j in sub) <= len(sub) - 1)
    # Objective function
    solver.Minimize(solver.Sum(x[i][j] * (0 if d[i][j] is None else d[i][j])
                               for i in range(n) for j in range(n)))
    status = solver.Solve()
    obj_val = solver.Objective().Value()
    sol_val = [[x[i][j].solution_value() for j in range(n)] for i in range(n)]
    # Convert to the matrix of decision variable x to a matrix of entry X
    X = sol_val
    tours = extract_tours(X, n)
    return status, obj_val, tours


def extract_tours(x, n):
    node = 0
    tours = [[0]]
    all_nodes = [0] + [1] * (n - 1)
    # Iterate until the remaining number of vertices = 0
    # Meaning the tours that the solver returns is 1
    while sum(all_nodes) > 0:
        next_node = [i for i in range(n) if x[node][i] == 1][0]
        if next_node not in tours[-1]:
            tours[-1].append(next_node)
            node = next_node
        else:
            node = all_nodes.index(1)
            tours.append([node])
        all_nodes[node] = 0
    return tours


def solve_tsp(D):
    sub_tours = []
    tours = []
    status, obj_val = 0, 0
    # When tours is only 1 tour then stops the iteration (the biggest tour)
    while len(tours) != 1:
        status, obj_val, tours = solve_tsp_eliminate(D, sub_tours)
        if status == 0:
            sub_tours.extend(tours)  # Add all tours to sub tours
            print("Set of sub tours:", tours)
    return status, obj_val, tours[0]


def check_extract_tours():
    # Consider an array below corresponding to the distance
    X = [[0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0]]
    print("Set of sub tours:", extract_tours(X, 7))


def read_data():
    # Data for the problem
    data = [
        [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
        [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
        [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
        [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
        [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
        [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
        [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
        [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
        [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
        [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
        [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
        [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
        [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0]]
    return data


def main():
    check_extract_tours()  # Display the sub tours
    # The source data: https://developers.google.com/optimization/routing/tsp
    D = read_data()
    print('Processing...')
    # dictionary of the city name
    cities = {0: 'New York', 1: 'Los Angeles', 2: 'Chicago', 3: 'Minneapolis', 4: 'Denver',
              5: 'Dallas', 6: 'Seattle', 7: 'Boston', 8: 'San Francisco',
              9: 'St.Louis', 10: 'Houston', 11: 'Phoenix', 12: 'Salt Lake City'}
    status, obj_val, tour = solve_tsp(D)
    print("Status:", status)
    print("Total distances:", obj_val, "miles")
    print("Route:", tour)
    # Display the city name based on tour
    print("Route:")
    for i in range(len(tour)):
        print(cities[tour[i]], end=" -> ")
    print(cities[tour[0]])  # Return to the starting city


main()
