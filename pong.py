import turtle 

win = turtle.Screen()
win.title("Ping Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

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

# Main game
while True:
    win.update()