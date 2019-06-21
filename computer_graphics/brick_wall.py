#######################################
# A simple turtle module that creates
# a 5 x 5 brick wall image by default.
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#######################################

import turtle

rect = turtle.Turtle()
screen = turtle.Screen()
screen.screensize()
rect.color('tomato')
rect.pencolor('black')  # creates a black border
rect.pensize(2)         # creates size of border in pixels

rect.shape('turtle')


def create_rectangle(l=100, w=50, r=5, c=5):
    """
    :param l: the length of the brick
    :param w: the width of the brick
    :param r: rows
    :param c: columns
    """

    x = -screen.screensize()[0]     # gets farthest left point
    y = screen.screensize()[1]      # gets height of the screen
    length, width, rows, cols = l, w, r, c

    for outer in range(rows):
        """
        skips the first iteration as we
        want to modify our position after 
        the first iteration. 
        """
        if outer == 0:
            pass
        else:
            y -= width                   # decrements y by rect's width
            x = -screen.screensize()[0]  # resets x to left-most corner

        for inner in range(cols):
            rect.penup()
            rect.setposition(x, y)
            rect.pendown()
            rect.begin_fill()
            for shape in range(2):
                rect.forward(length)
                rect.right(90)
                rect.forward(width)
                rect.right(90)
            rect.end_fill()
            x += length


if __name__ == '__main__':
    create_rectangle()
    turtle.done()