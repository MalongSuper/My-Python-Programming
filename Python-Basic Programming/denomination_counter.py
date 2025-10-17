# This program counts denominations
# Suppose you have a paper of 1$, 2$, 5$, 10$, 25$, 50$ and 100$
print("Denominations Counter")
cost = int(input("Enter the cost of the item: "))
if cost < 1:
    print("No suitable amount")
else:
    print(f"${cost} requires: ")
    # Calculate count for each denomination
    # Initialize the denominations as 0
    deno_100 = deno_50 = deno_25 = deno_10 \
        = deno_5 = deno_2 = deno_1 = 0
    # Calculate count for each denomination and update the remaining cost
    if cost >= 100:
        deno_100 = cost // 100
        cost = cost % 100
    if cost >= 50:
        deno_50 = cost // 50
        cost = cost % 50
    if cost >= 25:
        deno_25 = cost // 25
        cost = cost % 25
    if cost >= 10:
        deno_10 = cost // 10
        cost = cost % 10
    if cost >= 5:
        deno_5 = cost // 5
        cost = cost % 5
    if cost >= 2:
        deno_2 = cost // 2
        cost = cost % 2
    if cost >= 1:
        deno_1 = cost // 1
        cost = cost % 1
    # Display the nonzero denominations
    if deno_100 >= 1:
        print(f"* {deno_100} bills of 100$")
    if deno_50 >= 1:
        print(f"* {deno_50} bills of 50$")
    if deno_25 >= 1:
        print(f"* {deno_25} bills of 25$")
    if deno_10 >= 1:
        print(f"* {deno_10} bills of 10$")
    if deno_5 >= 1:
        print(f"* {deno_5} bills of 5$")
    if deno_2 >= 1:
        print(f"* {deno_2} bills of 2$")
    if deno_1 >= 1:
        print(f"* {deno_1} bills of 1$")
