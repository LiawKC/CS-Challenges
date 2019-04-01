import time
import random

NameList = ["Marcus","Nan","Rei","Max","Jung"]

for i in range(5):
    Strength1 = random.randint(0,100)
    Speed1 = random.randint(0,100)
    Intellect1 = random.randint(0,100)
    Endurance1 = random.randint(0,100)
    Equipment1 = random.randint(0,100)

for i in range(5):
    Strength2 = random.randint(0, 100)
    Speed2 = random.randint(0, 100)
    Intellect2 = random.randint(0, 100)
    Endurance2 = random.randint(0, 100)
    Equipment2 = random.randint(0, 100)

Player1 = input("What is Player 1's name? ")
Player2 = input("What is Player 2's name? ")

Player1Name = random.choice(NameList)
NameList.remove(Player1Name)
Player2Name = random.choice(NameList)

print("Player 1 Cards:")
time.sleep(0.5)
print("")
print(Player1, "got", Player1Name, "!")
time.sleep(0.25)
print(Player1Name, "has a strength of", Strength1, "!")
time.sleep(0.25)
print(Player1Name, "has a speed of", Speed1, "!")
time.sleep(0.25)
print(Player1Name, "has an intellect of", Intellect1, "!")
time.sleep(0.25)
print(Player1Name, "has an endurance of", Endurance1, "!")
time.sleep(0.25)
print(Player1Name, "has an equipment of", Equipment1, "!")

time.sleep(1)
print("")

print("Player 2 Cards:")
time.sleep(0.5)
print("")
print(Player2, "got", Player2Name, "!")
time.sleep(0.25)
print(Player2Name, "has a strength of", Strength2, "!")
time.sleep(0.25)
print(Player2Name, "has a speed of", Speed2, "!")
time.sleep(0.25)
print(Player2Name, "has an intellect of", Intellect2, "!")
time.sleep(0.25)
print(Player2Name, "has an endurance of", Endurance2, "!")
time.sleep(0.25)
print(Player2Name, "has an equipment of", Equipment2, "!")

time.sleep(1)
print("")

Choice = input("Do you choose strength, speed, intellect, endurance, or equipment?")

if Choice == "Strength":
    if Strength1 > Strength2:
        print(Player1, "wins!")
    else:
        print(Player2, "wins!")

if Choice == "Speed":
    if Speed1 > Speed2:
        print(Player1, "wins!")
    else:
        print(Player2, "wins!")

if Choice == "Intellect":
    if Intellect1 > Intellect2:
        print(Player1, "wins!")
    else:
        print(Player2, "wins!")

if Choice == "Endurance":
    if Endurance1 > Endurance2:
        print(Player1, "wins!")
    else:
        print(Player2, "wins!")

if Choice == "Equipment":
    if Equipment1 > Equipment2:
        print(Player1, "wins!")
    else:
        print(Player2, "wins!")