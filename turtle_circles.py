#############################################
# Turtle circle
# A simple program to teach you the basics
# of python programming by creating shapes
# using the builtin turtle module
#
# Circle
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#
#############################################

import turtle as t
import random as r


def create_circle(radius, width, x, y):
    """creates a circle in python. x and y represents
    the position of the circle."""
    circle = t.Turtle()
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'black']

    # set colors for circle
    a, b = r.choice(colors), r.choice(colors)
    circle.color(a, b)

    # ensures bg color is different from circle color
    background = r.choice(colors)
    begin = True
    while True:
        if background == a or background == b:
            continue
        break

    t.Screen().bgcolor(background)
    # sets pen width
    circle.width(width)
    # fill in shape with color
    circle.begin_fill()
    circle.circle(radius)
    circle.end_fill()
    circle.hideturtle()
    circle.setposition(x, y)
    t.done()


if __name__ == '__main__':
    create_circle(100, 5, 0, 0)
