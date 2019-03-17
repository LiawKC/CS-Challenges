import random
Students = int(input("How many students are there? "))

List = []
x = ""

Comment1 = "is a very stupid kid he never concentrates"
Comment2 = "is a very smart kid he gets A*s in everything"
Comment3 = "is a very lazy kid absolutely unteachable"
Comment4 = "is amazing, let me have him as my son"
Comment5 = "is absolutely horrendous, I will personally have him expelled"

GenericComments = Comment1, Comment2, Comment3, Comment4, Comment5

for i in range(Students):
    StudentName = input("What are their names? ")
    List.append(StudentName)

for i in range(Students):
    x = List[i]
    print("")
    print(x, random.choice(GenericComments))




