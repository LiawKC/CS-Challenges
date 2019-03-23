import time
import random

WordList = ["funny","jazz","lucky","bomb","mock"]
GuessList = []
Guesses = 0

RandomWord = random.choice(WordList)
LengthOfWord = len(RandomWord)

RandomWordOrganized = []
for i in range (LengthOfWord):
    RandomWordOrganized.append(RandomWord[i])

for i in range (LengthOfWord):
    GuessList.append("_")

print(*GuessList, sep = " ")

print("")

Guess = input("Guess a letter: ")

while Guesses < 10:
    if Guess not in (RandomWord):
        Guesses = Guesses + 1
        print(GuessList)
        Guess = input("Guess a letter: ")

    if Guess in (RandomWord):
        Guesses = Guesses + 1
        for i in range(LengthOfWord):
            if Guess in (RandomWord[i]):
                GuessList[i] = Guess
                print(GuessList)
                Guess = input("Guess a letter: ")

    if Guesses > 10:
        print("Sorry, you lose!")

    if GuessList == RandomWordOrganized:
        print("Wowzers! You guessed it in", Guesses, "guesses!")
        break








