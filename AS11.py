import random

x = " "
Colour = input("What is for your favourite colour? ")
Location = input("What is your favourite location? ")
Animal = input("What is your favourite animal? ")

SpecialCharacters = ["!","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","=","<","=",">","?","@","[","]","^","_"]
RandomSpecial1 = random.choice(SpecialCharacters)
SpecialCharacters.remove(RandomSpecial1)
RandomSpecial2 = random.choice(SpecialCharacters)
SpecialCharacters.remove(RandomSpecial2)

x = x + Colour + Location + Animal + RandomSpecial1 + RandomSpecial2
Length = len(x)

print("Your password is", x)