import random

Name = input("What is your name? ")

Number = random.randint(0,3)

if Number == 1:
    print("Hi!", Name, "how is your day today?")

if Number == 2:
    print("Good afternoon,", Name)

if Number == 3:
    print("It's a fine day today, isn't it?,", Name)

