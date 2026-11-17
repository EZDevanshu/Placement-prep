h = int(input("Enter hours (1-12): "))
m = int(input("Enter minutes (0-59): "))

hour_angle = (h * 30) + (m * 0.5)
minute_angle = m * 6

angle = abs(hour_angle - minute_angle)

if angle > 180:
    angle = 360 - angle

print("Angle between hour and minute hand =", angle, "degrees")
