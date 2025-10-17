# This program converts between Celsius and Fahrenheit
def celsius_to_fahrenheit(celsius):  # Define function
    # Calculate the Fahrenheit
    fahrenheit = (9 / 5) * celsius + 32
    fahrenheit = round(fahrenheit, 2)
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    # Calculate the Celsius
    celsius = (5 / 9) * (fahrenheit - 32)
    celsius = round(celsius, 2)
    return celsius


def main():  # Define main function
    print("Table of Conversions between Celsius and Fahrenheit")
    print("{:<15}{:<15}{:<5}{:<15}{:<15}".format("Celsius", "Fahrenheit", "|", "Fahrenheit", "Celsius"))
    # Assume these values for the table
    celsius = 41
    fahrenheit = 130
    # Display the table
    for table in range(1, 11):
        celsius = celsius - 1
        celsius = celsius / 1
        print("{:<15}{:<15}".format(celsius, celsius_to_fahrenheit(celsius)), end="")
        fahrenheit = fahrenheit - 10
        fahrenheit = fahrenheit / 1
        print("{:<5}{:<15}{:<25}".format("|", fahrenheit, fahrenheit_to_celsius(fahrenheit)))


# Display the result
main()
