planets = {
    "EARTH": 9.8,
    "MOON": 1.6,
    "JUPITER": 24.7,
    "MARS": 3.7,
    "VENUS": 8.8,
    "ERIS": 0.82
}

height = float(input())
destination = input().upper()
reaction_time = float(input())

actual_time = (2 * height / planets[destination])  ** 0.5
print (actual_time )

if reaction_time > actual_time:
    print("IT'S TOO SOON :(")
elif reaction_time == actual_time:
    print("MISSION COMPLETED.")
else:
    print("BOOOOOM!")