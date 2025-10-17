# This program displays the number of calories burned after 10, 15, 20, 25, 30 minutes
# Assume running on a particular treadmill burns you 4.2 calories per minute
Minute = 0
for Min in range(10, 35, 5):
    Min += Minute
    print("The number of calories burned after", Min, "minutes :", Min * 4.2)
