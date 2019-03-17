#Challenge 1

import time
import random

Choose_Name = ["James","John","Mark","Rick"]

print("The list of names are", *Choose_Name, sep=", ")
time.sleep(1)

for i in range (1,5):
    chosen = random.choice(Choose_Name)
    print("The gods have chosen", chosen)
    Continue = input("Do you wish to delete this name? ")

    if Continue in ("yes", "Yes"):
        Choose_Name.remove(chosen)
        print(*Choose_Name, sep=", ")

    else:
        print("Your list of names are", *Choose_Name)
        break

#Challenge 2

List = []

while True:
    Add = input("Do you want to add any characters? ")
    if Add == "y":
        Choice = input("What character do you want to add ")
        List.append(Choice)
        print(List)
    else:
        print("Bye")
        break
