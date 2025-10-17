# Calculate % of a value
# Reference: https://www.calculateme.com/math/percent-change/60-percent-less-than-0


def percentage_more(value, percentage):
    return value + (value * (percentage / 100))


def percentage_less(value, percentage):
    return value - (value * (percentage / 100))


def main():
    print("Percentage Calculation")
    count = 0
    while count < 100:
        value = float(input("Enter value: "))
        percentage = float(input("Enter percentage (%): "))
        if value < 0 or percentage < 0:
            print("Can't be Negative")
            continue
        result_more = percentage_more(value, percentage)
        result_less = percentage_less(value, percentage)
        print(f"+ {percentage}% more than {value} is: {result_more}")
        print(f"+ {percentage}% less than {value} is: {result_less}")
        count += 1


if __name__ == '__main__':
    main()
