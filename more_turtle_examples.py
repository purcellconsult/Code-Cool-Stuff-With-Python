#############################################
#
# A program that shows how to draw a flower
# and star using turtle.
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#
# Check out the turtle documentation in python:
#
#
#
##############################################

import turtle as t


def draw_flower(it=50):
    """creates a flower image by moving and
    then turning a certain degree after a certain
    time. The 'it' argument means the number of
    iterations. """
    flower = t.Turtle()
    flower.speed(10)
    flower.color('#953881')
    for x in range(it):
        flower.forward(200)
        flower.right(155.52453)
    flower.hideturtle()
    t.done()


def draw_stars(i=5):
    stars = t.Turtle()
    stars.color('light green')
    stars.begin_fill()
    for x in range(i):
        stars.forward(200)
        stars.left(216)
    stars.end_fill()
    t.done()


if __name__ == '__main__':
    draw_flower()

