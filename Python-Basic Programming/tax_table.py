# This program displays a tax table
def compute_tax(status, taxable_income):  # Define function
    # Compute tax
    if status == 0:  # Compute tax for single filers
        if taxable_income <= 8350:
            tax = taxable_income * 0.10
            return round(tax)
        elif taxable_income <= 33950:
            tax = 8350 * 0.10 + (taxable_income - 8350) * 0.15
            return round(tax)
        elif taxable_income <= 82250:
            tax = (8350 * 0.10 + (33950 - 8350) * 0.15 +
                   (taxable_income - 33950) * 0.25)
            return round(tax)
        elif taxable_income <= 171550:
            tax = (8350 * 0.10 + (33950 - 8350) * 0.15 +
                   (82250 - 33950) * 0.25 + (taxable_income - 82250) * 0.28)
            return round(tax)
        elif taxable_income <= 372950:
            tax = (8350 * 0.10 + (33950 - 8350) * 0.15 +
                   (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 +
                   (taxable_income - 171550) * 0.33)
            return round(tax)
        else:
            tax = (8350 * 0.10 + (33950 - 8350) * 0.15 +
                   (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 +
                   (372950 - 171550) * 0.33 + (taxable_income - 372950) * 0.35)
            return round(tax)
    if status == 1:  # Compute tax for married jointly
        if taxable_income <= 16700:
            tax = taxable_income * 0.10
            return round(tax)
        elif taxable_income <= 67900:
            tax = 16700 * 0.10 + (taxable_income - 16700) * 0.15
            return round(tax)
        elif taxable_income <= 137050:
            tax = (16700 * 0.10 + (67900 - 16700) * 0.15 +
                   (taxable_income - 67900) * 0.25)
            return round(tax)
        elif taxable_income <= 208850:
            tax = (16700 * 0.10 + (67900 - 16700) * 0.15 +
                   (137050 - 67900) * 0.25 + (taxable_income - 137050) * 0.28)
            return round(tax)
        elif taxable_income <= 372950:
            tax = (16700 * 0.10 + (67900 - 16700) * 0.15 +
                   (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 +
                   (taxable_income - 208850) * 0.33)
            return round(tax)
        else:
            tax = (16700 * 0.10 + (67900 - 16700) * 0.15 +
                   (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 +
                   (372950 - 208850) * 0.33 + (taxable_income - 372950) * 0.35)
            return round(tax)
    if status == 2:  # Compute tax for married separately
        if taxable_income <= 8350:
            tax = taxable_income * 0.10
            return round(tax)
        elif taxable_income <= 33950:
            tax = 8350 * 0.10 + (taxable_income - 8350) * 0.15
            return round(tax)
        elif taxable_income <= 68525:
            tax = (8350 * 0.10 + (33950 - 8350) * 0.15 +
                   (taxable_income - 33950) * 0.25)
            return round(tax)
        elif taxable_income <= 104425:
            tax = (8350 * 0.10 + (33950 - 8350) * 0.15 +
                   (68525 - 33950) * 0.25 + (taxable_income - 68525) * 0.28)
            return round(tax)
        elif taxable_income <= 186475:
            tax = (8350 * 0.10 + (33950 - 8350) * 0.15 +
                   (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 +
                   (taxable_income - 104425) * 0.33)
            return round(tax)
        else:
            tax = (8350 * 0.10 + (33950 - 8350) * 0.15 +
                   (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 +
                   (186475 - 104425) * 0.33 + (taxable_income - 186475) * 0.35)
            return round(tax)
    if status == 3:  # Compute tax for head of household
        if taxable_income <= 11950:
            tax = taxable_income * 0.10
            return round(tax)
        elif taxable_income <= 45500:
            tax = 11950 * 0.10 + (taxable_income - 11950) * 0.15
            return round(tax)
        elif taxable_income <= 117450:
            tax = (11950 * 0.10 + (45500 - 11950) * 0.15 +
                   (taxable_income - 45500) * 0.25)
            return round(tax)
        elif taxable_income <= 190200:
            tax = (11950 * 0.10 + (45500 - 11950) * 0.15 +
                   (117450 - 45500) * 0.25 + (taxable_income - 117450) * 0.28)
            return round(tax)
        elif taxable_income <= 372950:
            tax = (11950 * 0.10 + (45500 - 11950) * 0.15 +
                   (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 +
                   (taxable_income - 190200) * 0.33)
            return round(tax)
        else:
            tax = (11950 * 0.10 + (45500 - 11950) * 0.15 +
                   (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 +
                   (372950 - 190200) * 0.33 + (taxable_income - 372950) * 0.35)
            return round(tax)


def main():  # Define main function
    print("Tax Table")
    print("Taxable Income\t\tSingle\t\tMarried Joint\t\tMarried\t\tHead of Separate a House")
    # Assume the value for the table
    tax_income = 49950
    # Display the table
    for table in range(1, 202):
        tax_income = tax_income + 50
        status = 0
        print("{:<20}{:<15}".format(tax_income, compute_tax(status, tax_income)), end="")
        status = 1
        print("{:<18}".format(compute_tax(status, tax_income)), end="")
        status = 2
        print("{:<16}".format(compute_tax(status, tax_income)), end="")
        status = 3
        print("{:<15}".format(compute_tax(status, tax_income)))


# Display the result
main()
