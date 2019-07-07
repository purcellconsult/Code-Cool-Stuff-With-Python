import turtle
from random_colors import get_random_color


def create_circles(cycles=30):
    """
    Function for creating a spriograph
    Cycles is the number of iterations.
    """
    turtle.bgcolor('black')
    turtle.pensize(3)       # sets thickness of pencil stroke
    turtle.speed(0)         # sets drawing to the fastest speed possible
    x = -(turtle.Screen().window_width())

    for i in range(cycles):
        turtle.penup()
        turtle.goto(x,0)
        turtle.pendown()
        turtle.color(get_random_color())
        turtle.circle(100)  # sets circle radius
        x += 50
    turtle.done()


if __name__ == '__main__':
    create_circles()
