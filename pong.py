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
batA.penup()
batA.goto(-350, 0)

# Bat B

# Ball

# Main game
while True:
    win.update()