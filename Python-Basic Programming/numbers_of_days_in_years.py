# This program displays number of days in the years
def number_of_days_in_a_year(year):  # Define function
    # Display the table
    for table_year in range(year, year + 11):  # Determine leap year
        if (((table_year % 100) == 0 and (table_year % 400) == 0)
                or ((table_year % 100) != 0 and (table_year % 4) == 0)):
            days = 366
            print(f'{table_year}\t\t\t{days}')
        else:
            days = 365
            print(f'{table_year}\t\t\t{days}')


def main():  # Define main function
    print("Number of Days in Year")
    print("Year\t\tNumber of Days")
    year = 2010
    number_of_days_in_a_year(year)


# Display the result
main()
