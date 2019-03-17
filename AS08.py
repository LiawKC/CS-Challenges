import time
import random

print("Rock, 💎")
time.sleep(1)
print("Paper, 📄")
time.sleep(1)
print("Scissors, ✂")
time.sleep(1)

Choice = input("Shoot! 🔫 ")

if Choice in ("Rock", "rock"):
    print("Rock 💎.")
    time.sleep(0.5)
    print("Rock 💎..")
    time.sleep(0.5)
    print("Rock 💎...")
    time.sleep(0.5)

if Choice in ("Paper", "paper"):
    print("Paper, 📄.")
    time.sleep(0.5)
    print("Paper, 📄..")
    time.sleep(0.5)
    print("Paper, 📄...")
    time.sleep(0.5)

if Choice in ("Scissors", "scissors"):
    print("Scissors, ✂.")
    time.sleep(0.5)
    print("Scissors, ✂..")
    time.sleep(0.5)
    print("Scissors, ✂...")
    time.sleep(0.5)

ComputerChoice = ["Rock","Paper","Scissors"]
Chosen = random.choice(ComputerChoice)

if Choice in ("Rock", "rock") and Chosen == "Paper":
    print("I choose Paper 📄, you lose!")

if Choice in ("Rock", "rock") and Chosen == "Scissors":
    print("I choose Scissors ✂, you win!")

if Choice in ("Rock", "rock") and Chosen == "Rock":
    print("I choose Rock 💎, we draw!")

if Choice in ("Paper", "paper") and Chosen == "Scissors":
    print("I choose Scissors ✂, you lose!")

if Choice in ("Paper", "paper") and Chosen == "Rock":
    print("I choose Rock 💎, you win!")

if Choice in ("Paper", "paper") and Chosen == "Paper":
    print("I choose Paper 📄, we draw!")

if Choice in ("Scissors", "scissors") and Chosen == "Rock":
    print("I choose Rock 💎, you lose!")

if Choice in ("Scissors", "scissors") and Chosen == "Paper":
    print("I choose Paper 📄, you win!")

if Choice in ("Scissors", "scissors") and Chosen == "Scissors":
    print("I choose Scissors ✂, we draw!")