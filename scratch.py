import random

Floors = int(input("How many floors are there?"))

List = []

for i in range(Floors):
    List.append(i)

random.shuffle(List)
print(List)
