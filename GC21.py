#Exercise 1

for i in range(1000):
    print("We like Python's turtles!")

#Exercise 2
print("Colour, background colour, pen size")

#Exercise 3

for c in ("January","February","March","April","May","June","July","August","September","October","November","December"):
    print("One of the months of the year is", c)

#Exercise 4

print("She will be facing 45 degrees towards the top right from the horizontal")

#Exercise 5

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
Length = len(xs)

for i in range (Length):
    print(xs[i])
    print(xs[i] * xs[i])

print("")

Total = 0

for i in range(Length):
    Total = Total + xs[i]

print(Total)

print("")

for i in range (Length-1):
    print(xs[i] * xs[i+1])

#Exercise 6

import turtle

wn = turtle.Screen()
wn.bgcolor("Red")
wn.title("Hello, Tess!")

tess = turtle.Turtle()
tess.color("Blue")
tess.pensize(2)

for i in range(3):
    tess.forward(60)
    tess.left(120)

tess.penup()
tess.forward(100)
tess.pendown()

for i in range(4):
    tess.forward(45)
    tess.left(90)

tess.penup()
tess.forward(100)
tess.pendown()

for i in range(6):
    tess.forward(25)
    tess.left(60)

tess.penup()
tess.forward(100)
tess.pendown()

for i in range(8):
    tess.forward(20)
    tess.left(45)

wn.mainloop()