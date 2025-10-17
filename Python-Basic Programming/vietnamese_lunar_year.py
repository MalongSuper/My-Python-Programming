# Vietnamese Lunar Year
year = int(input("Enter a year: "))
if year < 1900:
    print("Invalid Input")
else:
    lunar_year = []
    # Using dictionary to store the values
    Thap_can = {"Giáp": 4, "Ất": 5, "Bính": 6, "Đinh": 7, "Mậu": 8,
               "Kỷ": 9, "Canh": 0, "Tân": 1, "Nhâm": 2, "Quý": 3}
    Thap_nhichi = {"Tý": 0, "Sửu": 1, "Dần": 2, "Mão": 3, "Thìn": 4, "Tỵ": 5,
                   "Ngọ": 6, "Mùi": 7, "Thân": 8, "Dậu": 9, "Tuất": 10, "Hợi": 11}
    # Retrieve the corresponding value for Thap Can
    Nam_Can = (year - 1900) % 10
    for i, j in Thap_can.items():
        if j == Nam_Can:
            lunar_year.append(i)
    # Retrieve the corresponding value for Thap Nhi Chi
    Nam_Chi = (year - 1900) % 12
    for m, n in Thap_nhichi.items():
        if n == Nam_Chi:
            lunar_year.append(m)
    # Display the result
    print(f"Year {year} is {lunar_year[0]} {lunar_year[1]}")
