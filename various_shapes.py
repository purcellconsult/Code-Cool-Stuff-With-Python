############################################
#
# Turtle shapes in python.
# Learn how to create a square,
# triangle, and rectangle using
# the builtin turtle module.
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#
#
############################################

import turtle as t


def main():

    # the following creates a square
    square = t.Turtle()
    t.title('Shapes in Turtle')
    square.begin_fill()
    # changes color mode to rgb
    t.colormode(255)
    square.color(150, 175, 215)
    # moves turtle forward 50 pixels
    square.forward(50)
    # change turtle angle 90 degrees
    square.right(90)
    # move turtle forward 50 pixels
    square.forward(50)
    # change turtle 90 degrees
    square.right(90)
    # moves turtle forward 50 pixels
    square.forward(50)
    # change turtle angel 90 degrees
    square.right(90)
    # moves turtle forward 50 pixels
    square.forward(50)
    square.end_fill()
    # prevents turtle from showing in square
    square.hideturtle()

    # creates a triangle

    triangle = t.Turtle()
    # needs this so lines are not drawn
    triangle.begin_fill()
    # points pen up so lines won't show when moving
    triangle.penup()
    # changes location of the triangle
    triangle.goto(0, -100)
    # point pendown so we can start drawing
    triangle.pendown()
    # changes color of the triangle
    triangle.color(50, 150, 255)
    triangle.begin_fill()
    # changes degree of turtle to 45 degrees
    triangle.right(45)
    # moves turtle forward 100 pixels
    triangle.forward(100)
    # changes turtle degree to 135
    triangle.right(135)
    # move turtle forward 71 pixels
    triangle.forward(71)
    # change turtle right 90 degrees
    triangle.right(90)
    # moves turtle forward 70 pixels
    triangle.forward(70)
    triangle.end_fill()
    # prevents turtle from showing in square
    triangle.hideturtle()

    # creates a rectangle

    rect = t.Turtle()
    rect.begin_fill()
    # points pen up so lines won't show when moving
    rect.penup()
    # moves the turtle to this x, y point
    rect.goto(0, 200)
    rect.begin_fill()
    # change color of this rectangle to the rgb value
    rect.color(150, 75, 100)
    # puts pen down so we can start drawing
    rect.pendown()
    # moves turtle forward 150 pixels
    rect.forward(150)
    # changes turtle angle by 90 degrees
    rect.right(90)
    # moves turtle forward 100 pixels
    rect.forward(100)
    # changes turtle angle 90 degrees
    rect.right(90)
    # moves turtle forward 150 pixels
    rect.forward(150)
    # changes turtle angle 90 degrees
    rect.right(90)
    # moves turtle forward 100 degrees
    rect.forward(100)
    rect.end_fill()
    rect.pendown()
    # prevents turtle from showing in square
    rect.hideturtle()
    # keeps the shapes on the screen
    t.done()


if __name__ == '__main__':
    main()