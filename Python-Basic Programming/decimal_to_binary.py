# This program converts decimal to binary
print("Decimal to Binary")
# Input the value
Number = int(input("Enter an integer: "))
if Number <= 0:
    print("Error: Invalid Number. Please try again")
else:
    print("The Binary Number is", end=" ")
    # Calculate the binary using loops
    while Number > 0:
        Binary = Number % 2
        Number = Number // 2
        Binary = round(Binary)
        # Display the result
        print(Binary, end="")
