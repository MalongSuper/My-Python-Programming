# This program computes the estimated area enclosed by these four cities
# The GPS location for the given cites
from math import sqrt, sin, cos, acos, radians
Atl_Lat, Atl_Lon = 33.748783, -84.388168
Orl_Lat, Orl_Lon = 28.538336, -81.379234
Sav_Lat, Sav_Lon = 32.083541, -81.099834
Char_Lat, Char_Lon = 35.2270869, -80.8431267
# Convert to Radians
Atl_Lat, Atl_Lon = radians(Atl_Lat), radians(Atl_Lon)
Orl_Lat, Orl_Lon = radians(Orl_Lat), radians(Orl_Lon)
Sav_Lat, Sav_Lon = radians(Sav_Lat), radians(Sav_Lon)
Char_Lat, Char_Lon = radians(Char_Lat), radians(Char_Lon)
# Compute the distance between two cities using the formula
Radius = 6371.01
Distance1 = Radius * acos(sin(Atl_Lat) * sin(Orl_Lat) + cos(Atl_Lat) * cos(Orl_Lat) * cos(Atl_Lon - Orl_Lon))
Distance2 = Radius * acos(sin(Orl_Lat) * sin(Sav_Lat) + cos(Orl_Lat) * cos(Sav_Lat) * cos(Orl_Lon - Sav_Lon))
Distance3 = Radius * acos(sin(Sav_Lat) * sin(Char_Lat) + cos(Sav_Lat) * cos(Char_Lat) * cos(Sav_Lon - Char_Lon))
Distance4 = Radius * acos(sin(Char_Lat) * sin(Atl_Lat) + cos(Char_Lat) * cos(Atl_Lat) * cos(Char_Lon - Atl_Lon))
Distance5 = Radius * acos(sin(Atl_Lat) * sin(Sav_Lat) + cos(Atl_Lat) * cos(Sav_Lat) * cos(Atl_Lon - Sav_Lon))
# All four cities created a polygon the same as a polygon
# Divide the polygon into two triangles
# Compute the area of Triangle 1
Side1 = Distance1
Side2 = Distance2
Side3 = Distance5
S1 = (Side1 + Side2 + Side3) / 2
Area1 = sqrt(S1 * (S1 - Side1) * (S1 - Side2) * (S1 - Side3))
# Compute the area of Triangle 2
Side4 = Distance5
Side5 = Distance3
Side6 = Distance4
S2 = (Side4 + Side5 + Side6) / 2
Area2 = sqrt(S2 * (S2 - Side4) * (S2 - Side5) * (S2 - Side6))
# Compute the total area
Total_Area = Area1 + Area2
# Display the result
print("The four cites: Atlanta, Georgia; Orlando, Florida; "
      "Savannah,Georgia; and Charlotte, North Carolina ")
print("The estimated area enclosed by these four cities is", Total_Area)
