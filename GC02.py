import time

Hour = int(input("What is the hour? "))
if Hour > 60:
    print("What are you trying to do? Read the question! ")
time.sleep(1)
Hour = int(input("What is the real hour? "))


Minute = int(input("What is the minute? "))
if Minute > 60:
    print("What are you trying to do? Read the question! ")
time.sleep(1)
Minute = int(input("What is the real minute? "))


TimeStatus = input("Is it in AM or PM? ")

if Hour == 12 and TimeStatus == "AM":
    print ("00",((Hour - 12)*100 + Minute))

else:
    if TimeStatus == "AM":
        print(AMConvertedTime)

if Hour == 12 and TimeStatus == "PM":
     print((Hour*100) + Minute)

else:
    if TimeStatus == "PM":
        print(PMConvertedTime)
