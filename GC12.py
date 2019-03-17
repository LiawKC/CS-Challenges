import time

TotalTime = int(input("How many hours do you have in total? "))
TotalPeople = int(input("How many people are there? "))

TimePerPerson = TotalTime/TotalPeople
RoundedHoursPerPerson = int(round(TimePerPerson))
RoundedMinutesPerPerson = RoundedHoursPerPerson*60

for i in range(TotalPeople):
    for i in range (RoundedMinutesPerPerson, 0, -1):
        print("You have", i)
        time.sleep(0.1)
