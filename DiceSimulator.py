import random
import turtle
print("\nCreated by \"Reza Rafiee\".02-Mar-22")
RandomNumber = random.randint(1, 6)
Txt = turtle.Turtle()
Tur = turtle.Turtle()
Win = turtle.Screen()
Win.title("Dice Simulation \U0001f600\U0001f3b2")
Win.bgcolor("black")
Tur.shape("classic")
Tur.pencolor("white")
Tur.fillcolor("black")
Tur.shapesize(0.5)
Tur.pensize(7)
Tur.speed(100)
Txt.goto(0, 150)
Txt.pencolor("white")
Txt.pensize(20)
Txt.write(f"The result is : {RandomNumber}", font="Arial", align="center")
Txt.hideturtle()
if RandomNumber == 1:
    Tur.penup()  # Starts drawing a square
    Tur.goto(100, 100)
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("black")
    Tur.rt(180)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.end_fill()
    Tur.penup()  # Finishes drawing the square
    Tur.goto(10, 0)  # Goes to coordinates of the only circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.hideturtle()
elif RandomNumber == 2:
    Tur.penup()  # Starts drawing a square
    Tur.goto(100, 100)
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("black")
    Tur.rt(180)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.end_fill()
    Tur.penup()  # Finishes drawing the square
    Tur.goto(85, 75)  # Goes to coordinates of 1st circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.penup()
    Tur.goto(-65, -75)  # Goes to coordinates of 2nd circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.hideturtle()
elif RandomNumber == 3:
    Tur.penup()  # Starts drawing a square
    Tur.goto(100, 100)
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("black")
    Tur.rt(180)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.end_fill()
    Tur.penup()  # Finishes drawing the square
    Tur.goto(85, 75)  # Goes to coordinates of 1st circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.penup()
    Tur.goto(10, 0)  # Goes to coordinates of 2nd circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.penup()
    Tur.goto(-65, -75)  # Goes to coordinates of 3rd circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.hideturtle()
elif RandomNumber == 4:
    Tur.penup()  # Starts drawing a square
    Tur.goto(100, 100)
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("black")
    Tur.rt(180)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.end_fill()
    Tur.penup()  # Finishes
    Tur.goto(85, 75)  # Goes to coordinates of 1st circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.penup()
    Tur.goto(-65, 75)  # Goes to coordinates of 2nd circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.penup()
    Tur.goto(-65, -75)  # Goes to coordinates of 3rd circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.penup()
    Tur.goto(85, -75)  # Goes to coordinates of 4th circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.hideturtle()
elif RandomNumber == 5:
    Tur.penup()  # Starts drawing a square
    Tur.goto(100, 100)
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("black")
    Tur.rt(180)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.end_fill()
    Tur.penup()  # Finishes
    Tur.goto(85, 75)  # Goes to coordinates of 1st circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.penup()
    Tur.goto(-65, 75)  # Goes to coordinates of 2nd circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.penup()
    Tur.goto(-65, -75)  # Goes to coordinates of 3rd circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.penup()
    Tur.goto(85, -75)  # Goes to coordinates of 4th circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.penup()
    Tur.goto(10, 0)  # Goes to coordinates of the 5th circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.hideturtle()
elif RandomNumber == 6:
    Tur.penup()  # Starts drawing a square
    Tur.goto(100, 100)
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("black")
    Tur.rt(180)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.lt(90)
    Tur.fd(200)
    Tur.end_fill()
    Tur.penup()  # Finishes
    Tur.goto(85, 75)  # Goes to coordinates of 1st circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.penup()
    Tur.goto(-65, 75)  # Goes to coordinates of 2nd circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.penup()
    Tur.goto(85, 0)  # Goes to coordinates of 3rd circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.penup()
    Tur.goto(-65, 0)  # Goes to coordinates of 4th circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.penup()
    Tur.goto(85, -75)  # Goes to coordinates of 5th circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.penup()
    Tur.goto(-65, -75)  # Goes to coordinates of 6th circle
    Tur.pendown()
    Tur.begin_fill()
    Tur.fillcolor("white")
    Tur.pensize(2.5)
    Tur.circle(10)
    Tur.end_fill()
    Tur.hideturtle()
Win.mainloop()
