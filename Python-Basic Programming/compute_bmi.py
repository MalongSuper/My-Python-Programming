# This program computes BMI by entering weight in pounds and height in feet and inches
# Input the values
Weight_in_Pounds = float(input("Enter weight in pounds: "))
Height_Feet = float(input("Enter feet: "))
Height_Inches = float(input("Enter inches: "))
if (Weight_in_Pounds < 0) or (Height_Feet < 0) or (Height_Inches < 0):
    print("Error: Invalid values detected. "
          "Please proceed and try again")
else:
    # Assume 1 pound = 0.45359237 kilograms
    Pound = 0.45359237
    Weight_in_Kilograms = Weight_in_Pounds * Pound
    # Assume 1 foot = 12 inches
    Foot_to_Inches = 12
    Height_in_Inches = (Height_Feet * Foot_to_Inches) + Height_Inches
    # Assume 1 inch = 0.0254 meters
    Meter = 0.0254
    Height_in_Meters = Height_in_Inches * Meter
    # Calculate the BMI
    BMI = Weight_in_Kilograms / (Height_in_Meters ** 2)
    print("Your BMI is", BMI)
    if BMI < 18.5:
        print("You are Underweight")
    elif BMI < 25:
        print("You are Normal")
    elif BMI < 30:
        print("You are Overweight")
    else:
        print("You are Obese")
