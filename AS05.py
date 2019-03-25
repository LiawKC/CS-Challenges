import time
import random


print("Welcome!")
time.sleep(1)

for i in range(20):
    print ("\n")

print("Welcome To")
time.sleep(1)

for i in range(20):
    print ("\n")

print("Welcome To Hangman!")


print("")

print("Scanning User IQ.")
time.sleep(0.5)
print("Scanning User IQ..")
time.sleep(0.5)
print("Scanning User IQ...")
time.sleep(0.5)

print("")

print("Finding Suitable Word.")
time.sleep(0.5)
print("Finding Suitable Word..")
time.sleep(0.5)
print("Finding Suitable Word..")
time.sleep(0.5)

print("")

WordList = ["funny","jazz","lucky","bomb","mock","bottle","mouse","bag","chair"]
GuessList = []
Guesses = 0

RandomWord = random.choice(WordList)
LengthOfWord = len(RandomWord)

RandomWordOrganized = []
for i in range (LengthOfWord):
    RandomWordOrganized.append(RandomWord[i])

for i in range (LengthOfWord):
    GuessList.append("_")

print("If the list shows the word, just press any key again!")

print("")

print(*GuessList, sep = " ")

print("")

Guess = input("Guess a letter: ")

while Guesses < 9:
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

    if GuessList == RandomWordOrganized:
        print("Wowzers! You guessed it in", Guesses, "guesses!")
        break

print("")

if Guesses > 8:
     print("Sorry, you lose!")












