#####################################
# Random circles in turtle
# ------------------------
# Creates randomed colored circles
# in python.
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#####################################

import turtle
from random_colors import get_random_color
from random import randint


def create_circles(amount=500):
    """
    Learn how to create random circles
    in python.
    """
    cir = turtle.Turtle()
    cir.speed(0)
    quantity_circles = amount
    length = cir.getscreen().window_width()
    height = cir.getscreen().window_height()
    for cycles in range(quantity_circles):
        cir.color(get_random_color())
        cir.penup()
        x, y = randint(-length, length), randint(-height, height)
        cir.goto(x, y)
        cir.pendown()
        rad = randint(5, 50)
        cir.begin_fill()
        cir.color(get_random_color())
        cir.pendown()
        cir.circle(rad)
        cir.end_fill()
    turtle.done()


if __name__ == '__main__':
    create_circles()

