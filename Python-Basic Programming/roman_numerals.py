# This program will display the Roman Numerals for the numbers
Number = int(input("Enter a number :"))
# The number entered must be between 1 and 10
if Number > 10 or Number < 1:
    print("Error: You must enter a number within the range of 1 through 10. "
          "Please proceed and try again")
# Display Results for every number
elif Number == 1:
    print("The Roman Numeral of 1 is I")
elif Number == 2:
    print("The Roman Numeral of 2 is II")
elif Number == 3:
    print("The Roman Numeral of 3 is III")
elif Number == 4:
    print("The Roman Numeral of 4 is IV")
elif Number == 5:
    print("The Roman Numeral of 5 is V")
elif Number == 6:
    print("The Roman Numeral of 6 is VI")
elif Number == 7:
    print("The Roman Numeral of 7 is VII")
elif Number == 8:
    print("The Roman Numeral of 8 is VIII")
elif Number == 9:
    print("The Roman Numeral of 9 is IX")
elif Number == 10:
    print("The Roman Numeral of 10 is X")
