print("This is a speed, distance, time calculator!")

print("")

x = input("Which variable are you trying to find?")

if x in ("speed", "Speed"):
    Distance = int(input("What is the distance?"))
    Time = int(input("What is the time?"))
    print(Distance/Time)

if x in ("distance", "distance"):
    Speed = int(input("What is the speed?"))
    Time = int(input("What is the time?"))
    print(Speed*Time)

if x in ("time", "Time"):
    Distance = int(input("What is the distance?"))
    Time = int(input("What is the speed?"))
    print(Distance/Speed)
