import turtle
import random
import time

races = int(input("How many races u wanna see bruv? "))

win1 = 0
win2 = 0

def data(num, wins, total):
    print(f"Turtle {num} has {wins} win(s)")
    print(f"Turtle {num}'s win rate is {wins/total}")


x = 0
for x in range(races):
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
    ref.color("green")


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
    ref.hideturtle()

    total_length = 525 
    distance = 0
    distance1 = 0


    #turtle.reset()
    while distance < 525 and distance1 < 525:
        move = random.randint(0,100)
        move1 = random.randint(0,100)
        one.forward(move)
        two.forward(move1)
        time.sleep(0.1)
        distance1 += move1
        distance += move


    one.write("Distance traveled: " + str(distance), font=('Arial', 20 , 'italic'))
    two.write("Distance traveled: " + str(distance1),font=('Arial', 20 , 'italic'))

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

    turtle.resetscreen()

data(1, win1, races)
data(2, win2, races)


# print("Turtle one: \n" + str(win) + " wins \n  Turtle one win rate: " + str((win/races)*100))
# print("Turtle two: \n" + str(win2) + " wins \n Turtle two win rate: " + str((win2/races)*100))
turtle.mainloop()