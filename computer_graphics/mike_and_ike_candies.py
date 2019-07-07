###################################
# Mike and Ike candies
# --------------------
#
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
###################################

import turtle
from random_colors import get_random_color
from random import randint


def create_candies(number=70, angle=20):
    width = turtle.Screen().window_width()
    height = turtle.Screen().window_height()

    screen = turtle.Screen()
    screen.bgcolor('black')
    screen.screensize(width, height)
    turn = angle
    lights = turtle.Turtle()
    lights.speed(0)
    lights.hideturtle()

    for x in range(number):
        x, y = randint(-height, height), randint(-width, width)
        lights.pensize(50)
        lights.pencolor(get_random_color())
        lights.right(turn)
        lights.forward(200)
        lights.penup()
        lights.goto(x, y)
        lights.pendown()
    turtle.done()


if __name__ == '__main__':
    create_candies()

