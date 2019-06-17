#####################################
# Random circles in turtle
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#####################################

import turtle
from random_colors import get_random_color
from random import randint


def create_circles(amount=100):
    """
    Learn how to create random circles
    in python.
    """

    cir = turtle.Turtle()
    cir.speed(0)
    size = amount
    for cycles in range(size):
        x, y = randint(-300, 300), randint(-400, 400)
        rad = randint(5, 50)
        cir.begin_fill()
        cir.color(get_random_color())
        cir.penup()
        cir.goto(x, y)
        cir.circle(rad)
        cir.pendown()
        cir.end_fill()
    turtle.done()


if __name__ == '__main__':
    create_circles()

