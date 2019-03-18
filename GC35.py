import time

Player1 = input("What is Player 1's name? ")

time.sleep(0.5)

Player2 = input("What is Player 2's name? ")

print("What is your question", Player1)
Player1Question = input()
Player1Answer = input("What is the answer?")

print("What is your question", Player2)
Player2Question = input()
Player2Answer = input("What is the answer?")

Player2Guess = input(Player1Question)
if Player2Guess != Player1Answer:
    print("You have failed")
else:
    print("Nice!")

time.sleep(0.5)

Player1Guess = input(Player2Question)
if Player1Guess != Player2Answer:
    print("You have failed")
else:
    print("Nice!")