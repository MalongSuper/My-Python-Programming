# Equation of a plane passing through 3 points
# Ex: A(2;0;-1) B(1;-2;3) C(0;1;2)

def get_normal_vector(a, b):
    # n: The normal vector perpendicular to vector A and vector B
    # Compute n = cross product [vector A,  vector B] = vector AB * vector AC
    n1 = (a[1] * b[2]) - (a[2] * b[1])
    n2 = (a[2] * b[0]) - (a[0] * b[2])
    n3 = (a[0] * b[1]) - (a[1] * b[0])
    N = [n1, n2, n3]
    return N


def main():
    a1, a2, a3 = eval(input("Enter point A: "))
    b1, b2, b3 = eval(input("Enter point B: "))
    c1, c2, c3 = eval(input("Enter point C: "))
    # A, B, C = [a1, a2, a3], [b1, b2, b3], [c1, c2, c3]
    # Compute vector AB, AC
    AB = [b1 - a1, b2 - a2, b3 - a3]
    AC = [c1 - a1, c2 - a2, c3 - a3]
    print("AB =", AB)
    print("AC =", AC)
    N = get_normal_vector(AB, AC)
    print("N =", N)
    # Plane equation has a form of Ax + By + Cz + D = 0
    # Find D using Point A
    D = 0 - (N[0] * a1 + N[1] * a2 + N[2] * a3)
    # Display the plane equation
    print("The plane equation passing through 3 points A, B, C:")
    print(f"{N[0]}x + {N[1]}y + {N[2]}z + {D} = 0")


main()
