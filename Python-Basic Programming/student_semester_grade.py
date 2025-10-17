# This program calculates a student's final grade for a full semester
# List of subjects
print("Final Semester")
print("Enter your scores below")
subjects = ["Math", "Literature", "English", "Physics",
            "Chemistry", "Biology", "History",
            "Geography", "Civics", "Computer Science",
            "Technology", "Musics & Arts"]
# List of status
status_list = ["EXCELLENT", "GOOD", "INTERMEDIATE", "MARGINAL", "FAIL"]
# Input the score of each subject in the first-term, midterm, and final-term exam
average_list = []
first_list, mid_list, final_list = [], [], []
for i in subjects:
    first, mid, final = eval(input(f"+ {i}: "))
    # Append the score to the lists
    first_list.append(first)
    mid_list.append(mid)
    final_list.append(final)
    # Calculate the average (round by 1 decimal)
    average = (first + mid * 2 + final * 3) / 6
    average_list.append(average)  # Append the average values to the list
# Input PE
pe_status = ["Pass", "P", "PASS", "Fail", "F", "FAIL"]  # Valid inputs for PE
pe = input("+ PE: Pass or Fail? ")
# Check for invalid input
if pe not in pe_status:
    print("Error: Invalid Input. Please proceed and try again")
elif (any(fir > 10 for fir in first_list)
        or any(mid > 10 for mid in mid_list)
        or any(fin > 10 for fin in final_list)):
    print("Error: Invalid Input. Please proceed and try again")
elif (any(fir < 0 for fir in first_list)
        or any(mid < 0 for mid in mid_list)
        or any(fin < 0 for fin in final_list)):
    print("Error: Invalid Input. Please proceed and try again")
else:  # If the input is valid, we can proceed to next part
    # Where we determine the student's grade status
    # Calculate the total average
    status = ""  # Define status
    total_average = sum(average_list) / 12  # There are 12 subjects
    if total_average >= 8.0:  # Total average is 8.0 or higher
        if any(aver < 6.5 for aver in average_list):  # Any subject below 6.5 => Good
            status = status_list[1]
        elif pe == "Fail":  # IF PE is "Fail" => Intermediate
            status = status_list[2]
        else:  # If it does not fall into those conditions => Excellent
            status = status_list[0]
    elif total_average >= 6.5:  # Total average is 6.5 or higher
        if any(aver < 5.0 for aver in average_list):  # Any subject below 5.0 =>  Intermediate
            status = status_list[2]
        elif pe == "Fail":  # IF PE is "Fail" => Marginal
            status = status_list[3]
        else:  # If it does not fall into those conditions => Good
            status = status_list[1]
    elif total_average >= 5.0:  # Total average is 5.0 or higher
        if any(aver < 3.5 for aver in average_list):  # Any subject below 3.5 =>  Marginal
            status = status_list[3]
        elif pe == "Fail":  # IF PE is "Fail" => Fail
            status = status_list[4]
        else:  # If it does not fall into those conditions => Intermediate
            status = status_list[2]
    elif total_average >= 3.5:  # Total average is 3.5 or higher
        if any(aver < 2.0 for aver in average_list):  # Any subject below 2.0 =>  Fail
            status = status_list[4]
        elif pe == "Fail":  # IF PE is "Fail" => Fail
            status = status_list[4]
        else:  # If it does not fall into those conditions => Marginal
            status = status_list[3]
    elif total_average >= 2.0:  # Total average is 2.0 or higher
        status = status_list[4]  # The status is fail regardless of conditions
    else:
        status = status_list[4]  # In every lower case
    # Display a table (report card)
    print()
    print("\t\t\t\t\t\t\t\tReport Card\t\t\t\t\t\t")
    print("===========================================================================")
    print('{:<20}{:<15}{:<15}{:<16}{:<20}'
          .format("Subject", "First Term", "Mid Term", "Final Term", "Average"))
    print("===========================================================================")
    for j in range(len(subjects)):
        print('{:<25}{:<15.1f}{:<15.1f}{:<15.1f}{:<15.1f}'
              .format(subjects[j], first_list[j], mid_list[j], final_list[j], average_list[j]))
    print("{:<25}{:<15}".format("PE", pe))
    # Display the result
    print()
    print(f"Total Average: {total_average: .1f}")
    print(f"Status: {status}")
