# This program displays the month points awarded for a customer when he or she buys a book
# Input the number of books purchased by a customer
Books = int(input("Enter the number of books you have purchased :"))
# Positive Number required
if Books < 0:
    print("Error: The number of books have to be a positive number. "
          "Please proceed and try again")
# If a customer purchases 0 books, he or she earns 0 points.
elif (Books >= 0) and (Books < 2):
    print("You earn 0 points")
# If a customer purchases 2 books, he or she earns 5 points
elif (Books >= 2) and (Books < 4):
    print("You earn 5 points")
# If a customer purchases 4 books, he or she earns 15 points
elif (Books >= 4) and (Books < 6):
    print("You earn 15 points")
# If a customer purchases 6 books, he or she earns 30 points.
elif (Books >= 6) and (Books < 8):
    print("You earn 30 points")
# If a customer purchases more than 8 or more books, he or she earns 60 points
elif Books >= 8:
    print("You earn 60 points")
