import random
import time

Cards = ["2","3","4","5","6","7","8","9","10"]
Special = ["Jack","Queen","King"]
Ace = ["Ace"]

z = []
z = z + Cards + Special + Ace

Player1Cards = []
Player2Cards = []

Player1 = input("What is Player 1s name? ")
Player2 = input("What is Player 2s name? ")


print(Player1,"...")
time.sleep(0.5)

x = random.choice(z)
print("Your first random card is", x)

if x in (Ace):
    AceValue = int(input("Do you want your ace to be a 1 or a 10?"))
    Player1Cards.append(AceValue)
else:
    Player1Cards.append(x)

y = random.choice(z)
print("Your second random card is", y)
Player1Cards.append(y)

if x in (Ace):
    AceValue = int(input("Do you want your ace to be a 1 or a 10?"))
    Player1Cards.append(AceValue)
else:
    Player1Cards.append(x)

print("")

print(Player2,"...")
time.sleep(0.5)

a = random.choice(z)
if a in (Ace):
    AceValue = int(input("Do you want your ace to be a 1 or a 10? "))
    Player2Cards.append(AceValue)
else:
    Player2Cards.append(x)
print("Your first random card is", a)

b = random.choice(z)
if b in (Ace):
    AceValue = int(input("Do you want your ace to be a 1 or a 10? "))
    Player2Cards.append(AceValue)
else:
    Player2Cards.append(x)
print("Your second random card is", b)

if sum(Player1Cards) > sum(Player2Cards):
    print(Player1, "wins")
else:
    print(Player2, "wins")
