######################################
# Simple turtle animation in python
# that shows a turtle rotating.
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#######################################

import turtle


def turtle_dance(rotate=90, cycles=500):
    """
    a simple program to model animation with
    the python turtle module. To change the
    animation try playing with the rotation.
    Try changing it to .5, 1, 5, and 10 to see
    how it effects the program.
    """
    tur = turtle.Turtle()
    tur.write('This shows a turtle spinning!', align='center', font=("Cambria", 11, "normal"))
    tur.shape('turtle')
    tur.color('green')
    x, y = rotate, cycles
    for spin in range(cycles):
        tur.left(x)
    turtle.done()


if __name__ == '__main__':
    turtle_dance()
