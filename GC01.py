import random

ComputerChoice = random.randint(0,100)

Choice = int(input("Guess a number! "))

while True:
    if Choice > ComputerChoice:
        print("Your number is too high!")
        Choice = int(input("Guess a new number! "))
    if Choice < ComputerChoice:
        print("Your number is too low!")
        Choice = int(input("Guess a new number! "))
    if Choice == ComputerChoice:
        print("You got it!")
        break

