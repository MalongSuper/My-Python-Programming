# This program reads information and display the payroll statement
# Input the information
Employee_Name = str(input("Enter employee's name: "))
Hours_Worked = int(input("Enter number of hours worked in a week: "))
Pay_Rate = float(input("Enter hour pay rate: "))
Federal_Tax = float(input("Enter federal tax withholding rate: "))
State_Tax = float(input("Enter state tax withholding rate: "))
if (Hours_Worked < 0) or (Pay_Rate < 0) or (Federal_Tax < 0) or (State_Tax < 0):
    print("Error: The values you entered are invalid. "
          "Please proceed and try again")
else:
    # Calculate using formulas
    Gross_Pay = Pay_Rate * 10
    Federal_Withholding = Gross_Pay * Federal_Tax
    State_Withholding = Gross_Pay * State_Tax
    Total_Reduction = Federal_Withholding + State_Withholding
    Net_Pay = Gross_Pay - Total_Reduction
    # Display the results
    print("PAYROLL STATEMENT")
    print("------------------")
    print("Employee Name:", Employee_Name)
    print("Pay Rate:", "$", Pay_Rate)
    print("Gross Pay:", "$", Gross_Pay)
    print("Deductions:")
    print("\tFederal Withholding", "(", (Federal_Tax * 100), "% )", ":", "$", round(Federal_Withholding, 2))
    print("\tState Withholding", "(", (State_Tax * 100), "% )", ":",  "$", round(State_Withholding, 2))
    print("\tTotal Deduction:", round(Total_Reduction, 2))
    print("Net Pay:", "$", round(Net_Pay, 2))
