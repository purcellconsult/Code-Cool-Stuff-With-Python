import turtle
import random


def choose_colors():
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
    return random.choice(colors)


def draw(turtle, radius):
    heading = turtle.heading()
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.setheading(heading)
    turtle.color(choose_colors())
    turtle.speed(100)


radius = int(input("Radius of the flower? "))
petals = int(input("How many petals? "))

koopa = turtle.Turtle()

for i in range(petals):
    draw(koopa, radius)
    koopa.left(360 / petals)

koopa.hideturtle()
screen = turtle.Screen()
screen.exitonclick()
