CurrentTime = 14
TimeNeeded = 51

Hour = CurrentTime + TimeNeeded

while Hour > 24:
    Hour = Hour - 24

if Hour > 12:
    Hour = Hour - 12
    print(Hour, "PM")

else:
    print(Hour, "AM")

