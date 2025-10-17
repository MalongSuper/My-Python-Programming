# This program displays Ascii Code Table
# Assume these for lines of the table
Number_per_Line = 10
Count = 0
print("\t\tASCII Code Table")
print("--------------------------------------")
# In Ascii Code, the character ! to ~ is from 33 to 126
for Character in range(33, 127):
    # Display using format()
    print(format(chr(Character)), end="\t")
    # Count the next number
    Count += 1
    # When the count reaches 10
    if (Count % Number_per_Line) == 0:
        # Display the next ten numbers into the next line
        print()
