# Find min(x) so that F(x) >= 0
# Input F(x)


def find_min_value(f):
    dictionaries = {}
    res_list = []
    for x in range(-100, 100):  # Try x from -100 to 100
        res = f(x)
        if res >= 0:
            dictionaries.update({x: res})  # Save the number as dictionary
            res_list.append(res)
    for key, item in dictionaries.items():
        if item == min(res_list):
            print(f"At x = {key}, y = {item} is the minimum value")


def main():
    print("Min of x so that F(x) ≥ 0")
    fx = input("Enter exact equation f(x): ")
    fx_lambda = eval(f"lambda x: {fx}")
    find_min_value(fx_lambda)


main()
