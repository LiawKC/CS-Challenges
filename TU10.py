import random

Addlist = "y"
anotherone = "y"
Chosen_names = []
Names = ["James","John","Mark","Rick"]
while anotherone == "y":
    randompick = random.choice(Names)
    print(randompick)
    Addlist = input("Add name to list? ")
    if Addlist == "y":
        Chosen_names.append(randompick)
        anotherone = input("Add more names? ")
    if Addlist != "y":
        print("Your chosen names are", Chosen_names)
        break
