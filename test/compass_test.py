import math

compass = {0: "N", 1: "NE", 2: "E", 3: "SE", 4: "S", 5: "SW", 6: "W", 7: "NW"}
px = int(input("Player X : "))
py = int(input("Player Y : "))
x = int(input("Point X : "))
y = int(input("Point Y : "))

direction = int(input("Direction : "))


if direction in range(8):
    print(compass[direction])

    # Center of the circle is the (px,py) point, atan2(py-y,px-x) gives the radian angle
    # to the chosen point within that circle
    angle = math.degrees(math.atan2(py - y, px - x))
    print("\nAngle :", angle,"°")

    # Reduce angle to [0,7] interval, called region
    region = math.floor((angle / 45) + 4)

    # If the point is in the chosen direction, region and direction are now equal
    if direction == region:
        print(
            "Point is", compass[direction], "compared to the selected player (center)"
        )
    else:
        print(
            "Point is not",
            compass[direction],
            "compared to the selected player (center) but rather",
            compass[region],
        )
