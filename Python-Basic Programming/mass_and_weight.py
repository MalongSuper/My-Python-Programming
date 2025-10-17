# This program will calculate an object's weight by its mass
# Input
Mass = float(input("Enter the object's mass :"))
if Mass < 0:
    print("Error: The object's mass cannot be negative. "
          "Please proceed and try again")
else:
    Weight = Mass * 9.8
    print("The object weighs",Weight,"newtons")
    # The object is too heavy when it weighs more than 500 newtons
    if Weight > 500:
        print("The object is too heavy")
    # The object is too light when it weighs less than 100 newtons
    elif Weight < 100:
        print("The object is too light")