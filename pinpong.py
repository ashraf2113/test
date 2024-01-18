import turtle
import time

wind = turtle.Screen()
wind.title("ping pung")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.penup()
madrab1.goto(350, 0)

madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(-350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

score1 = 0
score2 = 0

score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("player 1: 0 player 2: 0 ", align="center", font=("courier", 24, "normal"))

# functions:
def madrab1_up():
    y = madrab1.ycor()
    y += 20
    if y < 290:
        madrab1.sety(y)

def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    if y > -290:
        madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y += 20
    if y < 290:
        madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    if y > -290:
        madrab2.sety(y)

wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")

while True:
    wind.update()  # Update the graphics window

    # Check for events and move paddles
    wind.update()
    madrab1_up()
    madrab1_down()
    madrab2_up()
    madrab2_down()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score_display.clear()
        score_display.write("player 1: {} player 2: {}".format(score1, score2), align="center", font=("courier", 24, "normal"))

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score_display.clear()
        score_display.write("player 1: {} player 2: {}".format(score1, score2), align="center", font=("courier", 24, "normal"))

    if (340 > ball.xcor() > 330) and (madrab2.ycor() + 40 > ball.ycor() > madrab2.ycor() - 40):
        ball.setx(330)
        ball.dx *= -1

    elif (-340 < ball.xcor() < -330) and (madrab1.ycor() + 40 > ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-330)
        ball.dx *= -1

    time.sleep(0.01) 
