# This program will calculate the packages of hot dogs and buns needed for a cookout
# Assume the packages
HotDogs = 10
Buns = 8
# Input the number of people attending and the number of hot dogs given
People = int(input("Enter the number of people attending the cookout :"))
Pack = int(input("Enter the number of hot dogs each person will be given :"))
if People < 0 or Pack < 0:
    print("Error: The number of people and hot dogs cannot be negative. "
          "Please proceed and try again")
# Display the total number of hot dogs in the cookout
else:
    Total = People * Pack
    print("The total number of hot dogs in the cookout :",Total)
    # Calculate the minimum number of packages of hot dogs required
    Packages_HotDogs = Total // HotDogs
    print("=> The minimum number of packages of hot dogs required :",Packages_HotDogs)
    # Calculate the minimum number of packages of hot dog buns required
    Packages_Buns = Total // Buns
    print("=> The minimum number of packages of hot dog buns required :",Packages_Buns)
    # Calculate the number of hot dogs that will be left over
    Left_Over1 = Total % HotDogs
    if Left_Over1 != 0:
        print("=> The number of hot dogs that will be left over :",Left_Over1)
    else:
        print("=> There will be no hot dogs left over")
    # Calculate the number of hot dog buns that will be left over
    Left_Over2 = Total % Buns
    if Left_Over2 != 0:
        print("=> The number of hot dogs buns that will be left over :",Left_Over2)
    else:
        print("=> There will be no hot dog buns left over")



