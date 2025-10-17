# This program computes the tuition in ten years and the future four years
Tuition_Amount = 0
Four_Year = 0
Total = 10000
print("Year\t\tTuition Amount")
print("---------------------------")
# Suppose that the tuition for the first year is $10,000
for Year in range(1, 2):
    Tuition_Amount = 10000
    print(f'{Year}\t\t\t\t{Tuition_Amount}')
for Year in range(2, 11):
    Tuition_Amount = Tuition_Amount + (Tuition_Amount * 0.05)
    print(f'{Year}\t\t\t\t{round(Tuition_Amount, 2)}')
    # Compute the tuition for 10 years
    Total += Tuition_Amount
    # Compute the four years tuition worth using geometric series
    Four_Year = 10000 * ((1 + 0.05) ** 4 - 1) / ((1 + 0.05) - 1)
# Display the results
print("Compute Future Tuition")
print("The total tuition in ten years: ", round(Total, 3))
print("The total cost of four years’ worth of tuition: ", round(Four_Year, 5))
