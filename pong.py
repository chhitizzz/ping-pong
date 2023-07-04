import turtle 

win = turtle.Screen()
win.title("Ping Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score
scoreA = 0
scoreB = 0

# Bat A
batA = turtle.Turtle()
batA.speed(0)
batA.shape("square")
batA.color("white")
batA.shapesize(stretch_wid=5, stretch_len=1)
batA.penup()
batA.goto(-350, 0)

# Bat B
batB = turtle.Turtle()
batB.speed(0)
batB.shape("square")
batB.color("white")
batB.shapesize(stretch_wid=5, stretch_len=1)
batB.penup()
batB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.07
ball.dy = -0.07

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0              Player B: 0", align="center", font = ("Courier", 22, "normal"))

# Bat Movement
def batA_up():
    y = batA.ycor()
    y += 20
    batA.sety(y)

def batA_down():
    y = batA.ycor()
    y -= 20
    batA.sety(y)

def batB_up():
    y = batB.ycor()
    y += 20
    batB.sety(y)

def batB_down():
    y = batB.ycor()
    y -= 20
    batB.sety(y)

win.listen()
win.onkeypress(batA_up, "w")
win.onkeypress(batA_down, "s")
win.onkeypress(batB_up, "Up")
win.onkeypress(batB_down, "Down")

# Main game
while True:
    win.update()

# Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.write("Player A: {}              Player B: {}".format(scoreA, scoreB), align="center", font = ("Courier", 22, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.write("Player A: {}              Player B: {}".format(scoreA, scoreB), align="center", font = ("Courier", 22, "normal"))

    # Ball bounce 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < batB.ycor() + 40 and ball.ycor() > batB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < batA.ycor() + 40 and ball.ycor() > batA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1