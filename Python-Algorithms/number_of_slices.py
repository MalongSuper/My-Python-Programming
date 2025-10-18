# This program calculates the number of slices of a cake
import math
print("Number of slices needed to get a certain number of pieces of cake")
p = int(input("Enter number of pieces needed: "))
k = math.log(p, 2)  # Find k using logarithm
if k == int(k):
    print("Number of slices needed:", int(k))
else:
    print("Cannot be sliced into equal pieces")
