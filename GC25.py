import time

Milo = ("Milo", "milo")
MiloValue = 5
Wine = ("Wine", "wine")
WineValue = 4
Coke = ("Coke", "coke")
CokeValue = 3

y = 0
MoreCoins= 0

print("Welcome!")
time.sleep(1)
print("TO THE VENDING MACHINE!")
time.sleep(0.5)

print("|############################################|")
print("|#|                           |##############|")
print("|#|  ======  ======  ======   |##|````````|##|")
print("|#|  |Milo|  |Wine|  |Coke|   |##| Exact  |##|")
print("|#|  |_$5_|  |_$4_|  |_$3_|   |##| Change |##|")
print("|#|  /=__\   /.__\   /,__\    |##| Only   |##|")
print("|#|  \__//   \__//    \__//   |##|________|##|")
print("|#|===========================|##############|")
print("|#|```````````````````````````|##############|")
print("|#| =.._      +++     //////  |##############|")
print("|#| \/  \     | |     \    \  |#|`````````|##|")
print("|#|  \___\    |_|     /___ /  |#| _______ |##|")
print("|#|  / __\   /|_|\   // __\   |#| |1|2|3| |##|")
print("|#|  \__//-  \|_//   -\__//   |#| |4|5|6| |##|")
print("|#|===========================|#| |7|8|9| |##|")
print("|#|```````````````````````````|#| ``````` |##|")
print("|#| ..--    ______   .--._.   |#|[=======]|##|")
print("|#| \   \   |    |   |    |   |#|  _   _  |##|")
print("|#|  \___\  : ___:   | ___|   |#| ||| ( ) |##|")
print("|#|  / __\  |/ __\   // __\   |#| |||  `  |##|")
print("|#|  \__//   \__//  /_\__//   |#|  ~      |##|")
print("|#|===========================|#|_________|##|")
print("|#|```````````````````````````|##############|")
print("|############################################|")
print("|#|||||||||||||||||||||||||||||####```````###|")
print("|#||||||||||||PUSH|||||||||||||####\|||||/###|")
print("|############################################|")
print(" \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////")
Coins = int(input("Enter some coins! "))

while Coins > 2:
    Purchase = input("What would you like to buy? ")
    if Purchase in Milo:
        print("You have purchased milo!")
        Coins = Coins - MiloValue
        print("You still have", Coins, "coins to spend")
        Purchase = input("Would you like to purchase anything else? ")

    if Purchase in Wine:
        print("You have purchased wine! ")
        Coins = Coins - WineValue
        print("You still have", Coins, "coins to spend")
        Purchase = input("Would you like to purchase anything else? ")

    if Purchase in Coke:
        print("You have purchased coke! ")
        Coins = Coins - CokeValue
        print("You still have", Coins, "coins to spend")
        Purchase = input("Would you like to purchase anything else? ")

    if Coins < 2:
        MoneyStatus = input("You are out of money! Would you like to enter more? y/n ")
        if MoneyStatus == "y":
            MoreCoins = int(input("Enter more coins! "))
        Coins = Coins + MoreCoins
        Purchase = input("Would you like to purchase anything else? ")
        if MoneyStatus == "n":
            print("Goodbye!")
            break

