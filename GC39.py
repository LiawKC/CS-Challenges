import random
Name = input("What is his/her name? ")

List = []
x = ""

Comment1 = "ugly"
Comment2 = "fat"
Comment3 = "stupid"
Comment4 = "dumb"
Comment5 = "nasty"

Comments = Comment1, Comment2, Comment3, Comment4, Comment5

print("")
print(Name, random.choice(Comments))