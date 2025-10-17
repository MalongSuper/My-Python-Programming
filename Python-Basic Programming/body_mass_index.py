# This program calculates a person's body mass index
# Input the weight and the height
Weight = float(input("Enter your weight in kilograms :"))
Height = float(input("Enter your height in centimeters :"))
if Weight < 0 or Height < 0:
    print("Error: The weight and height cannot be negative. "
          "Please proceed and try again")
else:
    # Calculate the person's body mass index (BMI)
    # To calculate BMI, Weight is measured in pounds and Height is measured in inches
    # 1 pound = 0.4535 kilograms
    Weight_in_pounds = Weight / 0.4535
    # 1 inch = 2.54 centimeters
    Height_in_inches = Height / 2.54
    BMI = Weight_in_pounds * (703 / (Height_in_inches ** 2))
    print("Your BMI is",BMI)
    # A person is considered optimal if the BMI is between 18.5 and 25
    if (BMI >= 18.5) and (BMI <= 25):
        print("You are optimal")
    elif BMI < 18.5:
        print("You are underweight")
    elif BMI > 25:
        print("You are overweight")
