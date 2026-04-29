import turtle
import random

screen = turtle.Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("#0a0a0a")
screen.title("Live growing Dense Fractal Tree")
screen.tracer(1)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -300)
t.pendown()

def grow_tree_by_step(branch_len, thickness):
    if branch_len < 5:
        t.color(random.choice(["#27ae60", "#2ecc71", "#a2d149","#155e37"]))
        t.pensize(2)
        t.forward(branch_len)
        t.dot(random.randint(3,6))
        t.backward(branch_len)
        return

    if branch_len >= 45:
        t.color("#5d4037")
    else:
        t.color("#5d4037")
    t.pensize(thickness)
    t.forward(branch_len)
