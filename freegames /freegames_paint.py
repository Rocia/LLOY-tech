import random
from random import choice
import turtle
from freegames import vector

def value():
    "Randomly generate value between (-5, -3) or (3, 5)."
    return (3 + random() * 2) * choice([1, -1])

ball = vector(0, 0)
aim = vector(value(), value())

def draw():
    "Move ball and draw game."
    ball.move(aim)

    x = ball.x
    y = ball.y

    if x < -200 or x > 200:
        aim.x = -aim.x

    if y < -200 or y > 200:
        aim.y = -aim.y

    vector.clear()
    vector.goto(x, y)
    vector.dot(10)

    vector.ontimer(draw, 50)

vector.setup(420, 420, 370, 0)
turtle.hideturtle()
vector.tracer(False)
vector.up()
vector.draw()
vector.done()