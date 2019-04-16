import turtle as t
import random
my_turtle = t.Turtle()
my_turtle.screen.bgcolor('gray')
my_turtle.color('green')
my_turtle.speed(100)
my_turtle.pensize(3)
my_turtle.left(90)
my_turtle.screen.title('Turtle Fractal Tree')


def create_fractal(size):
    """main logic to create image."""
    colors = ['white', 'black', 'orange', 'red', 'blue', 'lightblue']
    my_turtle.color(random.choice(colors))
    if size < 15:
        return
    else:
        my_turtle.forward(size)
        my_turtle.left(35)
        create_fractal((3 * size) / 4)
        my_turtle.right(70)
        create_fractal((3 * size) / 4)
        my_turtle.left(35)
        my_turtle.backward(size)


create_fractal(80)
my_turtle = t.done()



