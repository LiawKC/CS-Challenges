import time

TotalTime = int(input("How many hours do you have in total? "))
TotalPeople = int(input("How many people are there? "))

TimePerPerson = TotalTime/TotalPeople
RoundedHoursPerPerson = int(round(TimePerPerson))
RoundedMinutesPerPerson = RoundedHoursPerPerson*60

if TotalPeople == 1:
    for i in range (RoundedMinutesPerPerson, 0, -1):
        print("You have", i)
        time.sleep(0.1)

if TotalPeople == 2:
    for i in range (RoundedMinutesPerPerson, 0, -1):
        print("The first person has", i)
        time.sleep(0.1)
    for i in range (RoundedMinutesPerPerson, 0, -1):
        print("The second person has", i)
        time.sleep(0.1)

if TotalPeople == 3:
    for i in range (RoundedMinutesPerPerson, 0, -1):
        print("The first person has", i)
        time.sleep(0.1)
    for i in range (RoundedMinutesPerPerson, 0, -1):
        print("The second person has", i)
        time.sleep(0.1)
    for i in range (RoundedMinutesPerPerson, 0, -1):
        print("The third person has", i )
        time.sleep(0.1)

if TotalPeople == 4:
    for i in range(RoundedMinutesPerPerson, 0, -1):
        print("The first person has", i)
        time.sleep(0.1)
    for i in range(RoundedMinutesPerPerson, 0, -1):
        print("The second person has", i)
        time.sleep(0.1)
    for i in range(RoundedMinutesPerPerson, 0, -1):
        print("The third person has", i)
        time.sleep(0.1)
    for i in range(RoundedMinutesPerPerson, 0, -1):
        print("The fourth person has", i)
        time.sleep(0.1)

if TotalPeople == 5:
    for i in range(RoundedMinutesPerPerson, 0, -1):
        print("The first person has", i)
        time.sleep(0.1)
    for i in range(RoundedMinutesPerPerson, 0, -1):
        print("The second person has", i)
        time.sleep(0.1)
    for i in range(RoundedMinutesPerPerson, 0, -1):
        print("The third person has", i)
        time.sleep(0.1)
    for i in range(RoundedMinutesPerPerson, 0, -1):
        print("The fourth person has")
        time.sleep(0.1)
    for i in range(RoundedMinutesPerPerson, 0, -1):
        print("The fifth person has", i)
        time.sleep(0.1)