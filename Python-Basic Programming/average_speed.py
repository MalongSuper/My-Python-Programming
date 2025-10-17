# Average Speed a runner runs in mph
print("Average Speed")
distance = float(input("Enter distance (km): "))
time = float(input("Enter time (in minutes): "))
# Convert minute to hour
# 1 hour = 60 min, 1 mile is 1.6 kilometer
time = time / 60
distance = distance / 1.6
speed = distance / time
print(round(speed, 3), "mph")
