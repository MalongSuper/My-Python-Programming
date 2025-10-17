# This program converts decimal to hexadecimal
print("Decimal to Hexadecimal")
# Input the value
Number = int(input("Enter an integer: "))
if Number <= 0:
    print("Error: Invalid Number. Please try again")
else:
    HexValue = ''
    Hex = 0
    print("The Hexadecimal Value is", end=" ")
    # List of Hex Value
    List = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
            7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: "E", 15: "F"}
    # Calculate the Hex value
    while Number > 0:
        # The digits in the calculation are not Hex
        NotHex = Number % 16
        Number = Number // 16
        NotHex = round(NotHex)
        # Combine all the Hex value
        # Convert the number to the string in the list given above
        HexValue += List.get(NotHex)
        # Reverse the number to get the correct Hex value
        Hex = HexValue[::-1]
    # Display the result
    print(Hex)
