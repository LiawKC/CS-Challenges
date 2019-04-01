import time
import random

PokemonList = ["Charmander's","Squirtle's","Bulbasaur's"]

Player1Move1 = random.randint(0,50)
Player1Move2 = random.randint(0,50)
Player1Move3 = random.randint(0,50)
Player1Move4 = random.randint(0,50)

Player2Move1 = random.randint(0,50)
Player2Move2 = random.randint(0,50)
Player2Move3 = random.randint(0,50)
Player2Move4 = random.randint(0,50)


Player1 = input("What is Player 1's name? ")
Player2 = input("What is Player 2's name? ")

Player1Pokemon = random.choice(PokemonList)
Player1Health = random.randint(100,200)
PokemonList.remove(Player1Pokemon)
Player2Pokemon = random.choice(PokemonList)
Player2Health = random.randint(100,200)

print("")

print(Player1, "got", Player1Pokemon, "!")
time.sleep(0.25)
print(Player1Pokemon, "first move has a damage of", Player1Move1)
time.sleep(0.25)
print(Player1Pokemon, "second move has a damage of", Player1Move2)
time.sleep(0.25)
print(Player1Pokemon, "third move has a damage of", Player1Move3)
time.sleep(0.25)
print(Player1Pokemon, "fourth move has a damage of", Player1Move4)

time.sleep(1)
print("")

print(Player2, "got", Player2Pokemon, "!")
time.sleep(0.25)
print(Player2Pokemon, "first move has a damage of", Player2Move1)
time.sleep(0.25)
print(Player2Pokemon, "second move has a damage of", Player2Move2)
time.sleep(0.25)
print(Player2Pokemon, "third move has a damage of", Player2Move3)
time.sleep(0.25)
print(Player2Pokemon, "fourth move has a damage of", Player2Move4)

time.sleep(1)
print("")

while True:
    print(Player1Pokemon,"has",Player1Health,"HP points!")
    print(Player2Pokemon,"has",Player2Health,"HP points!")

    print("")

    Choice1 = input("Player1, which move do you choose? ")
    if Choice1 == "1":
        Player2Health = Player2Health - Player1Move1
    if Choice1 == "2":
        Player2Health = Player2Health - Player1Move2
    if Choice1 == "3":
        Player2Health = Player2Health - Player1Move3
    if Choice1 == "4":
        Player2Health = Player2Health - Player1Move4

    print("")

    Choice2 = input("Player2, which move do you choose? ")
    if Choice2 == "1":
        Player1Health = Player1Health - Player2Move1
    if Choice2 == "2":
        Player1Health = Player1Health - Player2Move2
    if Choice2 == "3":
        Player1Health = Player1Health - Player2Move3
    if Choice2 == "4":
        Player1Health = Player1Health - Player2Move4

    if Player2Health < 0:
        print("")
        print("Player 1 Wins!")
        break

    if Player1Health < 0:
        print("")
        print("Player 2 Wins!")
        break

