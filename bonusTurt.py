import turtle
import random
import time

print('--------------------------------------------')
races = int(input("How many races u wanna see bruv? "))
print('--------------------------------------------')


win1 = 0
win2 = 0

colors = ['blue','green','pink','purple','brown','yellow','gold','turquoise']


def data(num, wins, total):
    print(f"Turtle {num} has {wins} win(s)")
    print(f"Turtle {num}'s win rate is {wins/total}")


for x in range(races):
    turtle.bgcolor("grey")
    one = turtle.Turtle()
    two = turtle.Turtle()
    ref = turtle.Turtle()

    one.shape("turtle")
    two.shape("turtle")
    ref.shape("turtle")

    one.speed(0)
    two.speed(0)
    ref.speed(0)

    one.color("red")
    two.color("blue")
    ref.color("black")

    x_val = -330
    y_val = 340
    ref.penup()
    ref.goto(-330,340)
    ref.pendown()

    for a in range(22):
        if a % 2 == 0:
            for x in range(3):
                if x % 2 == 0:
                    ref.penup()
                    ref.goto(x_val,y_val)
                    ref.pendown()
                    ref.begin_fill()

                    for y in range(4):
                        ref.right(90)
                        ref.forward(30)

                    ref.color("black")
                    ref.end_fill()
                    x_val += 30
                else:
                    ref.penup()
                    ref.goto(x_val,y_val)
                    ref.pendown()
                    ref.begin_fill()

                    for y in range(4):
                        ref.right(90)
                        ref.forward(30)

                    ref.color("white")
                    ref.end_fill()
                    x_val += 30
        else:
            for x in range(3):
                if x % 2 == 0:
                    ref.penup()
                    ref.goto(x_val,y_val)
                    ref.pendown()
                    ref.begin_fill()

                    for y in range(4):
                        ref.right(90)
                        ref.forward(30)

                    ref.color("white")
                    ref.end_fill()
                    x_val += 30
                else:
                    ref.penup()
                    ref.goto(x_val,y_val)
                    ref.pendown()
                    ref.begin_fill()

                    for y in range(4):
                        ref.right(90)
                        ref.forward(30)

                    ref.color("black")
                    ref.end_fill()
                    x_val += 30 
        y_val -= 30
        x_val = -330

    x_val = 290
    y_val = 340
    ref.penup()
    ref.goto(260,340)
    ref.pendown()

    for a in range(22):
        if a % 2 == 0:
            for x in range(3):
                if x % 2 == 0:
                    ref.penup()
                    ref.goto(x_val,y_val)
                    ref.pendown()
                    ref.begin_fill()

                    for y in range(4):
                        ref.right(90)
                        ref.forward(30)

                    ref.color("black")
                    ref.end_fill()
                    x_val += 30
                else:
                    ref.penup()
                    ref.goto(x_val,y_val)
                    ref.pendown()
                    ref.begin_fill()

                    for y in range(4):
                        ref.right(90)
                        ref.forward(30)

                    ref.color("white")
                    ref.end_fill()
                    x_val += 30
        else:
            for x in range(3):
                if x % 2 == 0:
                    ref.penup()
                    ref.goto(x_val,y_val)
                    ref.pendown()
                    ref.begin_fill()

                    for y in range(4):
                        ref.right(90)
                        ref.forward(30)

                    ref.color("white")
                    ref.end_fill()
                    x_val += 30
                else:
                    ref.penup()
                    ref.goto(x_val,y_val)
                    ref.pendown()
                    ref.begin_fill()

                    for y in range(4):
                        ref.right(90)
                        ref.forward(30)

                    ref.color("black")
                    ref.end_fill()
                    x_val += 30 
        y_val -= 30
        x_val = 290
    one.penup()
    one.goto(-275,200)

    two.penup()
    two.goto(-275, -200)
    total_length = 525 
    distance = 0
    distance1 = 0


    #turtle.reset()
    while distance < 525 and distance1 < 525:
        move = random.randint(0,100)
        move1 = random.randint(0,100)
        one.forward(move)
        one.color(random.choice(colors))
        two.forward(move1)
        two.color(random.choice(colors))
        time.sleep(0.1)
        distance1 += move1
        distance += move

    one.penup()
    two.penup()
    one.goto(-100,100)
    two.goto(-100,50)

    one.write("Distance traveled: " + str(distance), font=('Arial', 20 , 'italic'))
    two.write("Distance traveled: " + str(distance1),font=('Arial', 20 , 'italic'))
    time.sleep(2)

    if distance>distance1:
        one.right(90)
        one.forward(20)
        one.left(90)
        one.write("winner winner chicken dinner", font=('Arial', 20 , 'italic'))
        win1 += 1
    else:
        two.right(90)
        two.forward(20)
        two.left(90)
        two.write("winner yeehaw",font=('Arial', 20 , 'italic'))
        win2 += 1

    turtle.clearscreen()

#turtle.bgpic("/lilTurt/winner.gif")
print('---------------------------')
data(1, win1, races)
print('---------------------------')
data(2, win2, races)
print('---------------------------')



# print("Turtle one: \n" + str(win) + " wins \n  Turtle one win rate: " + str((win/races)*100))
# print("Turtle two: \n" + str(win2) + " wins \n Turtle two win rate: " + str((win2/races)*100))
turtle.mainloop()