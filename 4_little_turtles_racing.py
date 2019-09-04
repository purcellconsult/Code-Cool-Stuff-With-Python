###########################################
# 4 Little Turtles Racing Game
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

        '''
         Create starting x positions of turtles.
         Set it equal to the width + 100 so that
         it'll appear on the screen.
        '''
        self.red_x = self.width + (-self.width / 10)
        self.blue_x = self.width + (-self.width / 10)
        self.green_x = self.width + (-self.width / 10)
        self.black_x = self.width + (-self.width / 10)

        self.red_y = self.height - (self.height / 1.20)
        self.blue_y = self.height - (self.height / 1.1)
        self.green_y = self.height - (self.height / 1)
        self.black_y = self.height - (self.height / .9)

        # create speeds of turtles

        self.red_speed = 0
        self.blue_speed = 0
        self.green_speed = 0
        self.black_speed = 0

        self.finish = turtle.Turtle()

    def start_turtles(self):
        """
        Draws the turtles on the
        screen.
        """
        self.red.penup()
        self.red.color('red')
        self.red.goto(self.red_x, self.red_y)
        self.red.pendown()

        self.blue.penup()
        self.blue.color('blue')
        self.blue.goto(self.blue_x, self.blue_y)
        self.blue.pendown()

        self.green.penup()
        self.green.color('green')
        self.green.goto(self.green_x, self.green_y)
        self.green.pendown()

        self.black.penup()
        self.black.color('black')
        self.black.goto(self.black_x, self.black_y)
        self.black.pendown()

    def finish_line(self):
        """
        Draws the finish line
        and positions it on the right
        hand portion of the screen.
        """

        self.finish.hideturtle()
        self.finish.speed(0)  # draws graphics fastest possible
        self.finish.pensize(7)
        self.finish.hideturtle()
        self.finish.penup()
        self.finish.goto(-self.width / 2, self.height / 3)
        self.finish.pendown()
        self.finish.right(90)   # makes it vertical instead of horizontal


        for cycles in range(30):
            self.finish.forward(cycles)

        """
        write the text of 'Finish Line!' above
        the actual finish line. 
        """
        self.finish.penup()
        self.width = int(self.width / 2.4)
        self.finish.goto(-self.width, self.height / 2)
        self.finish.pendown()
        self.finish.write('Finish Line!', font=('Verdana', 13))
        print(self.width)

    def countdown_timer(self):
        """
        creates the countdown timer
        in the script.
        """
        secs = 5
        while secs > 0:
            message.write(secs, font=('Verdana', 50))
            secs -= 1
            sleep(1)
            message.clear()

    def set_turtle_speeds(self):
        """
        Randomly sets the speeds of
        the turtles.
        """
        speeds = [gait for gait in range(20, 25)]
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
            if self.red.pos()[0] >= self.finish.pos()[0]:
                if self.blue.pos()[0] >= self.finish.pos()[0] and self.blue.pos()[0] > self.red.pos()[0]:
                    self.finish.penup()
                    self.finish.goto(-self.width, self.height / 2.9)
                    self.finish.pendown()
                    self.finish.write('Blue Wins!', font=('Verdana', 13))
                    race_on = False
                    return self.blue
                elif self.green.pos()[0] >= self.finish.pos()[0] and self.green.pos()[0] > self.red.pos()[0] :
                    self.finish.penup()
                    self.finish.goto(-self.width, self.height / 2.9)
                    self.finish.pendown()
                    self.finish.write('Green Wins!', font=('Verdana', 13))
                    race_on = False
                    return self.green
                elif self.black.pos()[0] >= self.finish.pos()[0] and self.black.pos()[0] > self.red.pos()[0]:
                    self.finish.penup()
                    self.finish.goto(-self.width, self.height / 2.9)
                    self.finish.pendown()
                    self.finish.write('Black Wins!', font=('Verdana', 13))
                    race_on = False
                    return self.black
                self.red.forward(25)
                self.finish.penup()
                self.finish.goto(-self.width, self.height / 2.9)
                self.finish.pendown()
                self.finish.write('Red Wins!', font=('Verdana', 13))
                race_on = False
                return self.red
            elif self.blue.pos()[0] >= self.finish.pos()[0]:
                if self.green.pos()[0] > self.finish.pos()[1] and self.green.pos()[0] > self.blue.pos()[0]:
                    self.finish.penup()
                    self.finish.goto(-self.width, self.height / 2.9)
                    self.finish.pendown()
                    self.finish.write('Green Wins!', font=('Verdana', 13))
                    race_on = False
                    return self.green
                elif self.black.pos()[0] > self.finish.pos()[0] and self.black.pos()[0] > self.blue.pos()[0]:
                    self.finish.penup()
                    self.finish.goto(-self.width, self.height / 2.9)
                    self.finish.pendown()
                    self.finish.write('Black Wins!', font=('Verdana', 13))
                    race_on = False
                    return self.black
                self.blue.forward(25)
                self.finish.penup()
                self.finish.goto(-self.width, self.height / 2.9)
                self.finish.pendown()
                self.finish.write('Blue Wins!', font=('Verdana', 13))
                race_on = False
                return self.blue
            elif self.green.pos()[0] >= self.finish.pos()[0]:
                if self.black.pos()[0] > self.finish.pos()[1] and self.black.pos()[0] > self.green.pos()[0]:
                    self.finish.penup()
                    self.finish.goto(-self.width, self.height / 2.9)
                    self.finish.pendown()
                    self.finish.write('Black Wins!', font=('Verdana', 13))
                    race_on = False
                    return self.black
                self.green.forward(25)
                self.finish.penup()
                self.finish.goto(-self.width, self.height / 2.9)
                self.finish.pendown()
                self.finish.write('Green Wins!', font=('Verdana', 13))
                race_on = False
                return self.green
            elif self.black.pos()[0] >= self.finish.pos()[0]:
                self.black.forward(25)
                self.finish.penup()
                self.finish.goto(-self.width, self.height / 2.9)
                self.finish.pendown()
                self.finish.write('Black Wins!', font=('Verdana', 13))
                race_on = False
                return self.black

            self.red.forward(self.red_speed)
            self.blue.forward(self.blue_speed)
            self.green.forward(self.green_speed)
            self.black.forward(self.black_speed)

    def victor_dance(self):
        """
        silly little dance the winner
        turtle does after winning.
        """
        if self.turtle_race() == self.red:
            for x in range(50):
                self.red.right(90)
            self.red.shapesize(10, 10)
            return
        elif self.turtle_race() == self.blue:
            for x in range(50):
                self.blue.right(29)
            self.blue.shapesize(10, 10)
            return
        elif self.turtle_race() == self.green:
            for x in range(50):
                self.green.right(30)
            self.green.shapesize(10, 10)
            return
        elif self.turtle_race() == self.black:
            for x in range(15):
                self.black.right(90)
            self.black.shapesize(10, 10)
            return


if __name__ == '__main__':
    message = turtle.Turtle()
    message.hideturtle()

    race = TurtleRace()
    race.start_turtles()
    race.finish_line()

    race.countdown_timer()

    race.set_turtle_speeds()
    race.turtle_race()
    race.victor_dance()
    turtle.done()