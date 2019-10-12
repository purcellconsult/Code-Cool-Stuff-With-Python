##################################
# Party lights in turtle
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
###################################

import turtle
from random_colors import get_random_color
from random import randint


def create_lights(number=100, angle=20, forward=100):
    screen = turtle.Screen()
    screen.bgcolor('black')
    screen.screensize(-300, 300)
    turn = angle
    lights = turtle.Turtle()
    lights.speed(0)
    lights.hideturtle()

    for x in range(200):
        x, y = randint(-300, 300), randint(-300, 300)
        lights.pensize(4)
        lights.pencolor(get_random_color())
        lights.right(turn)
        lights.forward(200)
        lights.penup()
        lights.goto(x, y)
        lights.pendown()
    turtle.done()


if __name__ == '__main__':
    create_lights()


