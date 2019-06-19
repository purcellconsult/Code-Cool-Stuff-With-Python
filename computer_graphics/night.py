#######################################
# Creates a night sky using the turtle
# module in python.
#
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#######################################

import turtle
from random import randint
from random_colors import whites_and_pastels


def create_night_sky(stars=1000):
    sky = turtle.Turtle()

    back_ground = turtle.Screen()
    back_ground.bgcolor('black')
    num = stars
    sky.speed(0)
    for x in range(num):
        sky.color(whites_and_pastels())
        sky.begin_fill()
        sky.penup()
        sky.goto(randint(-300, 300), randint(-300, 300))
        sky.circle(randint(1, 5))
        sky.pendown()
        sky.end_fill()
    turtle.done()


if __name__ == '__main__':
    create_night_sky()