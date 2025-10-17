# This program computes Taxes
# To give the complete source code for the other filing statuses
# Input the filling status
Filling_Status_List = (0, 1, 2, 3)
Status = eval(input("(0-single filler, 1-married jointly,\n" +
                    "2-married separately, 3-head of household)\n" +
                    "Enter the filling status: "))
# Input taxable income
Income = eval(input("Enter the taxable income: "))
if Status not in Filling_Status_List:
    print("Error: Invalid status")
elif Income < 0:
    print("Error: Negative number is not allowed")
else:
    # Compute tax
    Tax = 0
    if Status == 0:  # Compute tax for single filers
        if Income <= 8350:
            Tax = Income * 0.10
        elif Income <= 33950:
            Tax = 8350 * 0.10 + (Income - 8350) * 0.15
        elif Income <= 82250:
            Tax = (8350 * 0.10 + (33950 - 8350) * 0.15 +
                   (Income - 33950) * 0.25)
        elif Income <= 171550:
            Tax = (8350 * 0.10 + (33950 - 8350) * 0.15 +
                   (82250 - 33950) * 0.25 + (Income - 82250) * 0.28)
        elif Income <= 372950:
            Tax = (8350 * 0.10 + (33950 - 8350) * 0.15 +
                   (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 +
                   (Income - 171550) * 0.33)
        else:
            Tax = (8350 * 0.10 + (33950 - 8350) * 0.15 +
                   (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 +
                   (372950 - 171550) * 0.33 + (Income - 372950) * 0.35)
    if Status == 1:  # Compute tax for married jointly
        if Income <= 16700:
            Tax = Income * 0.10
        elif Income <= 67900:
            Tax = 16700 * 0.10 + (Income - 16700) * 0.15
        elif Income <= 137050:
            Tax = (16700 * 0.10 + (67900 - 16700) * 0.15 +
                   (Income - 67900) * 0.25)
        elif Income <= 208850:
            Tax = (16700 * 0.10 + (67900 - 16700) * 0.15 +
                   (137050 - 67900) * 0.25 + (Income - 137050) * 0.28)
        elif Income <= 372950:
            Tax = (16700 * 0.10 + (67900 - 16700) * 0.15 +
                   (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 +
                   (Income - 208850) * 0.33)
        else:
            Tax = (16700 * 0.10 + (67900 - 16700) * 0.15 +
                   (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 +
                   (372950 - 208850) * 0.33 + (Income - 372950) * 0.35)
    if Status == 2:  # Compute tax for married separately
        if Income <= 8350:
            Tax = Income * 0.10
        elif Income <= 33950:
            Tax = 8350 * 0.10 + (Income - 8350) * 0.15
        elif Income <= 68525:
            Tax = (8350 * 0.10 + (33950 - 8350) * 0.15 +
                   (Income - 33950) * 0.25)
        elif Income <= 104425:
            Tax = (8350 * 0.10 + (33950 - 8350) * 0.15 +
                   (68525 - 33950) * 0.25 + (Income - 68525) * 0.28)
        elif Income <= 186475:
            Tax = (8350 * 0.10 + (33950 - 8350) * 0.15 +
                   (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 +
                   (Income - 104425) * 0.33)
        else:
            Tax = (8350 * 0.10 + (33950 - 8350) * 0.15 +
                   (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 +
                   (186475 - 104425) * 0.33 + (Income - 186475) * 0.35)
    if Status == 3:  # Compute tax for head of household
        if Income <= 11950:
            Tax = Income * 0.10
        elif Income <= 45500:
            Tax = 11950 * 0.10 + (Income - 11950) * 0.15
        elif Income <= 117450:
            Tax = (11950 * 0.10 + (45500 - 11950) * 0.15 +
                   (Income - 45500) * 0.25)
        elif Income <= 190200:
            Tax = (11950 * 0.10 + (45500 - 11950) * 0.15 +
                   (117450 - 45500) * 0.25 + (Income - 117450) * 0.28)
        elif Income <= 372950:
            Tax = (11950 * 0.10 + (45500 - 11950) * 0.15 +
                   (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 +
                   (Income - 190200) * 0.33)
        else:
            Tax = (11950 * 0.10 + (45500 - 11950) * 0.15 +
                   (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 +
                   (372950 - 190200) * 0.33 + (Income - 372950) * 0.35)
    print("Tax is", format(Tax, ".2f"))
