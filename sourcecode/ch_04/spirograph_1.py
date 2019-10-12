#######################################
# Spirograph creator
# ------------------
# Creates spirograph using the
# turtle module in python.
#
# Learn more about spirographs here:
# http://www.mathematische-basteleien.de/spirographs.htm
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#
########################################

import turtle
from random_colors import get_random_color


def create_circles(cycles=100):
    """
    Function for creating a spriograph
    Cycles is the number of iterations.
    """
    turtle.bgcolor('black')
    turtle.pensize(3)       # sets thickness of pencil stroke
    turtle.speed(0)         # sets drawing to the fastest speed possible

    for i in range(cycles):
        turtle.color(get_random_color())
        turtle.circle(125)  # sets circle radius
        turtle.right(25)    # turn right 25 degrees
    turtle.done()


if __name__ == '__main__':
    create_circles()

