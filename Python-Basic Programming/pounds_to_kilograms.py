# This program converts pounds into kilograms
Pound = float(input("Enter a value in pounds: "))
if Pound < 0:
    print("Error: You cannot enter a negative number. "
          "Please proceed and try again")
else:
    # One pound is 0.454 kilograms
    One_Pound = 0.454
    Kilograms = Pound * One_Pound
    print(Pound, "pounds is", Kilograms, "kilograms")
