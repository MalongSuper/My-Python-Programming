# This program calculates the average rainfall
# Assume the data
Year = 0
Total = 0
Average = 0
Number_Month = 0
Inches_of_Rainfall = 0
# The program should first ask the number of years
Number_of_Year = int(input("Enter the number of years :"))
if Number_of_Year < 0:
    print("Error: The number of years cannot be negative. "
          "Please proceed and try again")
else:
    # Display the year
    for Year in range(1, Number_of_Year + 1):
        print("Year", Year)
        Name_Month = ('January', 'February', 'March',
                      'April', 'May', 'June',
                      'July', 'August', 'September',
                      'October', 'November', 'December')
        # Create a loop
        for Month in Name_Month:
            # Ask the user for the inches of rainfall in the month
            Inches_of_Rainfall = float(input("Enter the inches of rainfall for"+" " + str(Month)+":"))
            while Inches_of_Rainfall <= 0:
                Inches_of_Rainfall = float(input("Error: Only positive number is allowed. "
                                                 "Please enter again :"))
            # Calculate the total inches of rainfall for all the periods
            Total += Inches_of_Rainfall
    # Calculate the number of months
    Number_Month = Year * 12
    # Calculate the average rainfall per month
    Average = Total / Number_Month
    # Display the results
    print("The number of months :", Number_Month)
    print("The total inches of rainfall :", Total)
    print("The average per month for the entire period :", Average)
