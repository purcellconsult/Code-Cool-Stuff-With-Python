###########################################
# PyTurtle Race Game
# ----------------------------
# Creates a simple yet fun little
# turtle racing simulator in python using
# the turtle module. Includes countdown timer
# and randomly determines the speed of the turtles.
#
# By Doug Purcell
# http://www.purcellconsult.com
#
############################################

import turtle
from random import choice
from time import sleep


class TurtleRace:

    def __init__(self):
        """
        creates the various turtles as instance
        variables.
        """
        self.red = turtle.Turtle(shape='turtle')
        self.blue = turtle.Turtle(shape='turtle')
        self.green = turtle.Turtle(shape='turtle')
        self.black = turtle.Turtle(shape='turtle')
        self.height = turtle.Screen().window_height()
        self.width = -turtle.Screen().window_width()  # make it negative to start turtle farthest left possible
        self.finish = turtle.Turtle()
        self.finish.hideturtle()

        self.finish.speed(0)  # draws graphics fastest possible
        self.games = 1

        # create starting x positions of turtles

        self.red_x = self.width + 100
        self.blue_x = self.width + 100
        self.green_x = self.width + 100
        self.black_x = self.width + 100

        # create speeds of turtles

        self.red_speed = None
        self.blue_speed = None
        self.green_speed = None
        self.black_speed = None

    def start_turtles(self):
        """
        Draws the turtles on the
        screen.
        """
        self.red.penup()
        self.red.color('red')
        self.red.goto(self.width + 100, 100)
        self.red.pendown()

        self.blue.penup()
        self.blue.color('blue')
        self.blue.goto(self.width + 100, 50)
        self.blue.pendown()

        self.green.penup()
        self.green.color('green')
        self.green.goto(self.width + 100, 0)
        self.green.pendown()

        self.black.penup()
        self.black.color('black')
        self.black.goto(self.width + 100, -50)
        self.black.pendown()

    def set_turtle_speeds(self):
        """
        Randomly sets the speeds of
        the turtles.
        """
        speeds = [x for x in range(1, 25) if x % 2 == 0]
        self.red_speed = choice(speeds)
        self.blue_speed = choice(speeds)
        self.green_speed = choice(speeds)
        self.black_speed = choice(speeds)

    def turtle_race(self):
        """
        Makes the turtles actually move,
        and determines the winner.
        """
        race_on = True
        while race_on:
            self.red.forward(self.red_speed)
            self.blue.forward(self.blue_speed)
            self.green.forward(self.green_speed)
            self.black.forward(self.black_speed)
            red_x, red_y = self.red.pos()

            if self.red.pos()[0] >= self.finish.pos()[0]:
                self.red.forward(self.red_speed * 2.75)
                self.finish.penup()
                self.finish.goto(-self.width, self.height / 2.9)
                self.finish.pendown()
                self.finish.write('Red Wins!', font=('Verdana', 13))
                race_on = False
                return self.red
            elif self.blue.pos()[0] >= self.finish.pos()[0]:
                self.blue.forward(self.blue_speed * 2.75)
                self.finish.penup()
                self.finish.goto(-self.width, self.height / 2.9)
                self.finish.pendown()
                self.finish.write('Blue Wins!', font=('Verdana', 13))
                race_on = False
                return self.blue
            elif self.green.pos()[0] >= self.finish.pos()[0]:
                self.green.forward(self.green_speed * 2.75)
                self.finish.penup()
                self.finish.goto(-self.width, self.height / 2.9)
                self.finish.pendown()
                self.finish.write('Green Wins!', font=('Verdana', 13))
                race_on = False
                return self.green
            elif self.black.pos()[0] >= self.finish.pos()[0]:
                self.black.forward(self.black_speed * 2.75)
                self.finish.penup()
                self.finish.goto(-self.width, self.height / 2.9)
                self.finish.pendown()
                self.finish.write('Black Wins!', font=('Verdana', 13))
                race_on = False
                return self.black

    def victor_dance(self):
        """
        silly little dance the winner
        turtle does after winning.
        """
        if self.turtle_race() == self.red:
            for x in range(50):
                self.red.right(90)
            self.red.shapesize(10, 10)
        elif self.turtle_race() == self.blue:
            for x in range(50):
                self.blue.right(29)
            self.blue.shapesize(10, 10)
        elif self.turtle_race() == self.green:
            for x in range(50):
                self.green.right(30)
            self.green.shapesize(10, 10)
        elif self.turtle_race() == self.black:
            for x in range(15):
                self.black.right(90)
            self.black.shapesize(10, 10)

    def finish_line(self):
        """
        Draws the finish line
        and positions it on right
        hand portion of the screen.
        """

        self.finish.pensize(7)
        self.finish.hideturtle()
        self.finish.penup()
        self.finish.goto(-self.width / 2, self.height / 3)
        self.finish.pendown()
        self.finish.right(90)

        for cycles in range(30):
            self.finish.forward(cycles)
        self.finish.penup()
        self.width = int(self.width / 2.4)
        self.finish.goto(-self.width, self.height / 2)
        self.finish.pendown()
        self.finish.write('Finish Line!', font=('Verdana', 13))


if __name__ == '__main__':
    message = turtle.Turtle()
    message.hideturtle()

    race = TurtleRace()
    race.start_turtles()
    race.finish_line()

    message.penup()
    message.goto(race.width, race.height / 2)
    message.pendown()

    """
    adds countdown timer to game.
    """
    secs = 5
    while secs > 0:
        message.write(secs, font=('Verdana', 50))
        secs -= 1
        sleep(1)
        message.clear()
    race.set_turtle_speeds()
    race.turtle_race()
    race.victor_dance()
    turtle.done()
