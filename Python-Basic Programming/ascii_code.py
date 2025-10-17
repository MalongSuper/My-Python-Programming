# This program finds the character of an ASCII code
Ascii_Code = int(input("Enter an ASCII code: "))
if (Ascii_Code > 127) or (Ascii_Code < 0):
    print("Error: The number you entered is not in the ASCII Code Table. "
          "Please proceed and try again")
else:
    # Use chr() function to convert an integer to a character in ASCII Code
    Ascii_Character = chr(Ascii_Code)
    # Display the results
    print("The character is", "\"", Ascii_Character, "\"")
