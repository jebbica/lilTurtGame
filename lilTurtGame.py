import turtle
import random
import time

one = turtle.Turtle()
two = turtle.Turtle()
ref = turtle.Turtle()

one.shape("turtle")
two.shape("turtle")
ref.shape("turtle")

one.speed(5)
two.speed(0)
ref.speed(0)

one.color("red")
two.color("blue")



one.penup()
one.goto(-275,200)

two.penup()
two.goto(-275, -200)

ref.penup()
ref.goto(-275, 400)
ref.pendown()
ref.right(90)
ref.forward(800)

ref.penup()
ref.goto(250, 400)
ref.pendown()
ref.forward(800)

total_length = 525 
distance = 0
distance1 = 0
while distance and distance1 < 525:
    move = random.randint(0,100)
    move1 = random.randint(0,100)
    one.forward(move)
    two.forward(move1)
    time.sleep(0.5)
    distance1 += move1
    distance += move



turtle.mainloop()