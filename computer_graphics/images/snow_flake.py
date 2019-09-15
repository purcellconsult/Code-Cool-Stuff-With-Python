#################################
# Snow flake
# ----------------------------
# Draw a simple snow flake using
# lines in python.
#
#
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
###################################


import turtle

line = turtle.Turtle()
line.hideturtle()
line.pensize(3)

for x in range(8):
    line.forward(200)
    line.goto(0, 0)
    line.left(45)
turtle.done()