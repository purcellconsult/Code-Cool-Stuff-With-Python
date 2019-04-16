import turtle as t
import random
my_turtle = t.Turtle()
my_turtle.screen.bgcolor('gray')
my_turtle.color('green')
my_turtle.speed(10)
my_turtle.pensize(3)
my_turtle.left(50)
my_turtle.screen.title('Nonagon')


def create_nonagon(size):
    """main logic to create image."""
    colors = ['white', 'black', 'orange', 'red', 'blue', 'lightblue']
    my_turtle.color(random.choice(colors))
    if size < 15:
        return
    else:
        my_turtle.forward(size)
        my_turtle.left(40)
        create_nonagon((4 * size) / 4)
        my_turtle.right(80)
        create_nonagon((4 * size) / 4)
        my_turtle.left(40)
        my_turtle.backward(size)


create_nonagon(100)
my_turtle = t.done()




