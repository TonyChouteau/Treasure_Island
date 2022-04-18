import math

compass = {0: "W", 1: "SW", 2: "S", 3: "SE", 4: "E", 5: "NE", 6: "N", 7: "NW"}
px = 0
py = 0
x = float(input("Point X : "))
y = float(input("Point Y : "))

# direction = int(input("Direction : "))



# Center of the circle is the (px,py) point, atan2(py-y,px-x) gives the radian angle
# to the chosen point within that circle
angle = math.degrees(math.atan2(y - py, x - px))
print("\nAngle :", angle,"°")

# Offset to get 8 directions with diagonal frontiers
offset = (angle + 202.5) / 45
if int(offset) == offset:
    print("EDGE CASE") # Right on the frontiers
else:
    # Reduce angle to [0,7] interval, called region
    region = math.floor(offset) % 8
    # print(region)

    # If the point is in the chosen direction, region and direction are now equal
    print(compass[region])
    # if direction == region:
    #     print(
    #         "Point is", compass[direction], "compared to the selected player (center)"
    #     )
    # else:
    #     print(
    #         "Point is not",
    #         compass[direction],
    #         "compared to the selected player (center) but rather",
    #         compass[region],
    #     )
