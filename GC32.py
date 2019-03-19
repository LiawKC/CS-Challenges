import random

OptionA = "Stay Silent"
OptionB = "Confess"
Options = (OptionA, OptionB)

Player = input("What is your name? ")
PlayerOption = input("Do you wish to do OptionA (StaySilent) or OptionB (Confess)? ")

ComputerChoice = random.choice(Options)

if PlayerOption == "OptionA":
    if ComputerChoice == OptionA:
        print("The computer chose", OptionA)
        print("You both go to jail for 1 year (nice!)")
    if ComputerChoice == OptionB:
        print("The computer chose", OptionB)
        print("You go to jail for 20 years (RIP)")

if PlayerOption == "OptionB":
    if ComputerChoice == OptionA:
        print("The computer chose", OptionA)
        print("You're a free man! Congratulations!")
    if ComputerChoice == OptionB:
        print("The computer chose", OptionB)
        print("You both go to jail for 5 years")
