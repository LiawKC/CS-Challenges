import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Hi")

Nan = turtle.Turtle()
Nan.shape("turtle")
Nan.color("Blue")
Nan.pensize(2)

for i in range (100):
    Nan.forward(100)
    Nan.left(random.randint(0,360))

wn.mainloop()