from random_colors import get_random_color
import turtle


def random_color_square():
    square = turtle.Turtle()
    square.hideturtle()
    square.pensize(3)   # set the border to 3 pixels
    square.pencolor(get_random_color()) # set border color
    square.color(get_random_color(), get_random_color())  # set fill and outer color
    square.begin_fill()
    for x in range(4):
        square.forward(100)
        square.right(90)
    square.end_fill()
    turtle.done()


random_color_square()