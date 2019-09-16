# **Chapter IV: Crafting Catchy Computer Art with Python Turtle**


## Geometry 101: Learning How to Create Shapes

Let's create the following image:

![Big Green Turtle](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/big_green_turtle.png)

Below is the code for it:

 
    import turtle
    leonardo = turtle.Turtle()
    leonardo.shape('turtle')
    leonardo.shapesize(7.5, 7.5)
    leonardo.color('green')
    turtle.done()

  

The first thing we need to do is import the turtle module so that we can use all of the builtin functionality. 
  
After the turtle module is imported we can go ahead and call the `Turtle()` constructor. From there we can change the default shape of the turtle object to something more appealing like you guessed it, a turtle. From there we can call various functions on it to manipulate its appearance such as `shapesize()` and `color()`. We must then use the `done()` method to start the event loop which in essence calls the Tkinter’s main loop function. We’ll learn about Tkinter in Chapter V but just remember that into the meantime you need it at the end of your program.

## Coding a Simple Square in Turtle

Lets reminiscence about the time our geometry teacher taught us about important things in life such as the x-y coordinate plane, how to plot, and the foundations of shapes. Remember any of that? If so then great because it will serve you well when learning about the basics of turtle. Lets go back down memory lane, do you recall the essential features of a square? Facts like that they have four equal sides and four right angles. 

We can easily create a square in turtle but we need to know a couple of things. For one, we need to know how to move forward, and we also need to know how to create angles as the interior of a square should be 90 degrees. In order to do this we need to use the builtin methods of forward and turn. Below is a demo of how to create a square in python:

    import turtle
    square = turtle.Turtle()
    square.hideturtle()
    square.forward(100)
    square.right(90)
    square.forward(100)
    square.right(90)
    square.forward(100)
    square.right(90)
    square.forward(100)
    turtle.done()

Below is the image that it will render:

![Image: Simple Square](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/simple_turtle.png)

The `hideturtle` method removes the turtle so that it won’t appear in the final output, the forward method pushes the turtle forward an arbitrary number of pixels, and the right method pivots the turtle an arbitrary number of degrees.

There’s one slight problem which is we have some duplicate code! The code pretty much has four forward method calls and three right method calls. We can therefore add these two statements in a for loop as shown in the following code snippet:

    import turtle
    square = turtle.Turtle()
    square.hideturtle()
    for x in range(4):
        square.forward(100)
        square.right(90)
    turtle.done()

It literally produces the same image as above but with fewer lines of code.

But wait, we can further enhance our code by giving the user the ability to modify the square size, color, border, etc. We can wrap the logic inside of a function so that we can reuse it when needed. The below function still creates a square, albeit with the enhanced functionality:

    import turtle
    def create_square(size=100, outer_color='black', inner_color='blue', border=2):
        square = turtle.Turtle()
        square.pensize(border)
        square.color(outer_color, inner_color)
        square.hideturtle()
        square.begin_fill()
        for x in range(4):
            square.forward(size)
            square.right(90)
        square.end_fill()
        turtle.done()
        
    create_square()
![Image: Enhanced Square](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/enhanced_square.jpg)

The **Enhanced Square** has the same logic as the **Simple Square** with the exception that it specifies some default features of the square such as the size, outer color, inner color, and border.

If the above wasn’t clear It’s best to tinker with the function parameters to learn how they manipulate the square. There’s so many world of possibilities! This is just a sample of what’s possible when you’re coding with python turtle.

## The PyRandomColor Open source Module

Just like how entertainment would be mundane with just black and white television, the same concept applies to your turtle computer graphics. Therefore, we can spice things up by adding color to our images. Turtle enables pythonistas the ability to add color via the color function.

You can read about the function specifications in the turtle module here: [https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.color](https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.color)

You can call it with no arguments, one argument, or two arguments. When you pass in one argument it returns the `pencolor` and current `fillcolor` as a pair; it doesn't actually manipulate the color, just returns what color is in the turtle object to the user. When you specify one argument it fills in the turtle object with that color, and when you specify two arguments the first argument is the outer color and the second one is the fill _aka_ inner color.

This is great, but sometimes when you’re creating images you’re not exactly sure what colors to use… at least I don’t! Or better yet, maybe you just want to experiment with the many different types of until you find the combinations you like the most.

Ta-da, this is where the *PyRandomColor* module  comes to the rescue! I’ve told you in **Chapter III** that I’m obsessed with randomization :-).

This simple module allows you to randomly pick colors which can come in handy when you want to quickly create computer art. You can access it here: [https://github.com/purcellconsult/PyRandomColor](https://github.com/purcellconsult/PyRandomColor)

There’s a couple of ways that you can quickly access the script so that you’ll be up and running.

Since the module is available via the PyPI package manager you can simply install it using pip as shown in the following code snippet:

    $ pip install pyrandomcolor
    
Alternatively, you can clone the file to your computer using the following git command:

    git https://github.com/purcellconsult/PyRandomColor.git

It's a really simple script but it will save you the grunt work of having to think of a way to do this yourself. Here’s a quick overview of the functions that’s available:

`get_random_color()`: Picks any random color.

`whites_and_pastels()`: Returns a random color that’s within the white and pastel hues.

`grays()`: returns a random color that’s within the gray color scheme.

 `blues()`: Returns a random color within the blue color scheme.

`greens()`: Returns a random color within the green color scheme.

`yellows()`: Returns a random color within the yellow color scheme.

`browns()`: Returns a random color within the brown color scheme.

`oranges()`:  Returns a random color within the orange color scheme.

`pinks_violets()`: Returns a random color within the pinkish and _violetish_ color scheme.

Here's an example on how to use the module to randomly color a square:

    from random_colors import get_random_color
    import turtle
    def random_color_square1():
        square = turtle.Turtle()
        square.hideturtle()
        square.pensize(3)   
        square.pencolor(get_random_color()) 
        square.color(get_random_color(), get_random_color()) 
        square.begin_fill()
        for x in range(4):
            square.forward(100)
            square.right(90)
        square.end_fill()
        turtle.done()
        
    random_color_square1()
    
Below is the output image:

![ Random Color Square One](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/random_color_square_1.png)

Note, since this uses randomized colors there’s a high probability that there will be some variance compared to the image you generate. This is why I think this so cool, every execution of the script will most likely generate something slightly different.

Here's a quick explanation. To randomly fill in the inner and outer colors of a turtle object you need to do two things: use the color  function and then pass in the `get_random_color` method twice from the `random_colors` module.  

Remember, when you specify two arguments the first one is the outer color while the second one is for the  inner color. To get the color to generate we need to include the `begin_fill` method call before the loop and the `end_fill`  after it.

Here’s some more examples of the things you can do with `PyRandomColor` so that you’ll have inspiration:

    def random_color_square2(cycles=10):
        square = turtle.Turtle()
        go, turn = 100, 90
        square.hideturtle()
        square.pensize(3)  
        square.pencolor(get_random_color()) 
        square.color(get_random_color(), get_random_color()) 
        for x in range(cycles):
            for y in range(4):
                square.forward(go)
                square.right(turn)
            go -= 10
        turtle.done()
    random_color_square2()

Here’s the output:

![Random Color Square](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/random_color_square_2.png)

## How to Craft Beautiful Designs From Ugly Shapes with Turtle and PyRandomColor

Putting together simple shapes is an easy way to draw complex and surprisingly stunning patterns. Let’s start with what we already know which is the square. We can use that simple shape to create a multi-colored cube as shown in the following code snippet:

    import turtle
    from random_colors import get_random_color
    square = turtle.Turtle()
    square.hideturtle()
    for x in range(4):
        square.color(get_random_color(), get_random_color())
        square.begin_fill()
        square.right(90)
        for y in range(4):
            square.forward(100)
            square.right(90)
        square.end_fill()
    turtle.done()

Below is one way in which the image could look:

![Square Cube](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/square_cube.png)

A nested loop is used to create four squares of varying colors. After each iteration the new square is rotated 90 degrees and then the new square is created. Can you guess what happens is that if the inner loop iterated two cycles instead of 4? Here’s how it would manipulate the image:

![Triangle Cube](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/triangle_cube.png)

It will be a cube of multicolored triangles instead of squares. We can continue to create a more complex images by building on top of the simple code for creating a square. Let’s make some tweaks to the **square cube** code as shown below:

    import turtle
    from random_colors import get_random_color
    square = turtle.Turtle()
    square.hideturtle()
    square.speed(0)
    for x in range(50):
        square.color(get_random_color(), get_random_color())
        square.begin_fill()
        square.right(35)
        for y in range(4):
            square.forward(100)
            square.right(90)
        square.end_fill()
    turtle.done()
    
If we do that then we can get an interesting image as shown below:

![Square Artwork](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/square_artwork.png)

This image looks complex but the code is straightforward. It’s an image that contains 50 squares which are rotated by 35 degrees after each complete inner loop cycle. Go ahead and play with the code to see how a couple of tweaks to these simple _turtle algorithms_ can create  derivative artwork.

## A Randomly Generated Night Sky with Shining Stars

The sky dotted with stars is a beautiful sight to see. The good news is that you don’t have to be in the Grand Canyon to stargaze as you can bring the sky to your computer screen as shown in the image below:

![Night](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/night.png)

To emulate the effect of the star-dotted-sky we need two things: a black background and a whole bunch of circles of various sizes spread throughout. To re-create this image we need to first learn how to make circles which fortunately is simple with turtle. Here’s the method signature for circles:

    turtle.circle(radius, extent=None, steps=None)

The radius is the distance from the center of a circle to any point on its circumference. The _extent_ if not given draws the entire circle, and if given draws an arc. The arc is drawn in a counterclockwise direction if the radius is positive, otherwise it’s drawn in a clockwise direction. Let's learn how to create a simple circle and then a simple arc. The following code snippet shows a full circle:

    import turtle
    x = turtle.Turtle()
    x.hideturtle()
    x.pensize(2)
    x.circle(100)
    turtle.done()

Below is an example of how the circle looks in python:

![Circle](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/circle.png)

As you have probably figured out the bigger you make the radius the bigger the circle, and vice-versa. To simulate an arc pass in a keyword argument in the circle method as shown below:

    import turtle
    x = turtle.Turtle()
    x.hideturtle()
    x.pensize(2)
    x.circle(100, extent=150)
    turtle.done()

Below is the generated image:

![Arc](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/arc.png)

Now, with our newfound knowledge of circles we have one more thing that we need to know. We need to know how to move turtle objects on the screen. The reason for this is that we don’t want to plot all of the circles at the same exact position because doing so will lead to a blob of circles around the same area which is kind of awkward. Instead, we want to randomly draw the circles at various locations on the screen in order to get a better distribution of circles. We can accomplish this by using three more methods from the turtle class:

-   `penup`: Picks the pen up, no drawing happens.
-   `pendown`:Puts the pen down.
-   `goto(x, y=None)`: Move the turtle to the x and y coordinates.

The `penup` and `pendown` methods operates the exact way you’ll think when you’re drawing on a piece of paper. If you're sitting at your desk sketching a masterpiece what happens when you decide to pick your pen up and move it to a different position on the paper you’re sketching on? The pen appears at a different part on your paper, and of course when the pen is in the air no drawing happens.

When you put your pen back down this is when the drawing happens. This is important to use in turtle because if you don’t use these methods and instead just use the `goto` method then lines will be drawn along the path which is not what you want. In other words, it’s like if you’re sketching a stick man on a piece of paper and instead of picking the pen up to draw the individual components, you keep the pen down the entire time which will lead to ugly squiggly lines along the way.

Lastly, we need to set the background color of the screen which can be done by using the `bgcolor` method from the Screen class. From there we can call the `bgcolor` method in order to modify the color. Let’s code the night sky in turtle by first including all of the imports:

    import turtle
    from random import randint
    from random_colors import whites_and_pastels

We’ll import the turtle module in order to use its functionality, the `randint` function from random to generate random numbers which will be used for positioning, and then the `white_and_pastels` function from the `PyRandomColor` module in order to give the stars various shades to mimic the sky. Below is the beginning of the function definition:

    def create_night_sky(stars=1000):
        sky = turtle.Turtle()
        sky.speed(0)
        turtle.Screen().bgcolor('black')

Here we’re just creating a function with a default argument of 1000. This simply represents how many stars will be in the final image. Next, the turtle constructor is called and the speed is set to 0 so that the images will be drawn at the fastest rate possible. The `bgcolor` method from the `Screen` instance is called to set the background of the screen to black which will give us the _night sky_ effect. Now, here’s the rest of the function:

    num = stars
    for x in range(num):
        sky.color(whites_and_pastels())
        sky.begin_fill()
        sky.penup()
        sky.goto(randint(-300, 300), randint(-300, 300))
        sky.circle(randint(1, 5))
        sky.pendown()
        sky.end_fill()
    turtle.done()


Here's where the stars are created and then moved each iteration. We create a for loop which iterates by default 1000 cycles. From there, we set the colors of the starts. To do this we again need to utilize the color, `begin_fill`, and `end_fill` methods. Since we want to arbitrarily determine the position of the stars that we want to draw, we can use the `penup`, `goto`, and `pendown` methods. Remember, the `penup` method is used to pick the pen up so that no lines follow when the position is being allocated. We then pass the `randint` function into the x and y arguments of `goto` to randomly determine the x/y coordinates of where the circle will be displayed.


Once the position is located we can use the circle method to create the actual circle. Since we want to simulate stars in the sky, we need to ensure that some stars are bigger than others. How can we accomplish this? We need to arbitrarily set the radius of the circle by again using the `randint` function. The last statement in the program must be `turtle.done()` so that the final image will stay; without this then the outputted image goes _bye-bye_. We can then run the program to see the sky populated with varying sized stars in various locations. Every time the program is ran the output will be different but it could be difficult to tell without screenshotting and comparing the pictures due to the small size of the circles.

## Creating Circle Art With Python Turtle

While we’re on the topic of using circles to create cool graphics we can again use these shapes for more creative computer art. Just like we did in the previous example, let's again create random circles of varying sizes. However, this time we’re going to give them any of the various random colors from the get_random_color  function in the `PyRandomColor`  module. The code for crafting this is listed below:

    import turtle
    from random_colors import get_random_color
    from random import randint
    
    def create_color_circles(amount=500):
        
        cir = turtle.Turtle()
        cir.speed(0)
        quantity_circles = amount
        length = cir.getscreen().window_width()
        height = cir.getscreen().window_height()
        for cycles in range(quantity_circles):
            cir.penup()
            x, y = randint(-length, length), randint(-height, height)
            cir.goto(x, y)
            cir.pendown()
            rad = randint(5, 50)
            cir.begin_fill()
            cir.color(get_random_color())
            cir.pendown()
            cir.circle(rad)
            cir.end_fill()
        turtle.done()

Here's the output:

![Random Colored Circles](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/random_color_circles.png)

Now, let’s dig through the code. This function is similar to the code used to create the **Night** image. 

However, there’s two simple tweaks. One, the circles are populated across the whole dimension of the user’s screen. This is accomplished by using the `getscreen` method which returns the `TurtleScreen` object that the turtle is drawing on. The width of the screen is stored in the length variable and the height is stored in the height variable. A loop is created that by default iterates over 500 and then repeatedly runs the steps of:

-   Picking the pen up
    
-   Randomly sets the location of the circle by selecting a variable x within the range of -length to length, and a y variable in the range of negative height to height
    
-   Puts the circle at the location of the x and y variables
    
-   Places the pen down. No more squiggly lines!
    
-   Randomly sets the size of the radius of the circle within the range of 5 through 50 pixels
    
-   Calls the `begin_fill` method
    
-   Calls the `get_random_color` method from the `PyRandomColor`  module
    
-   Puts the pen down
    
-   Draws the circle with the rad radius
    
-   Calls the `end_fill` method
    
-   Calls `turtle.done()`

Pretty cool stuff. Let’s continue riding the circle art bandwagon. Let’s ago ahead and create a simple _spirograph_ with a circle. Below is the code snippet for this:

import turtle
from random_colors import get_random_color

    def create_circles(cycles=100):
    
        turtle.bgcolor('black')
        turtle.pensize(3)       
        turtle.speed(0)        
        for i in range(cycles):
            turtle.color(get_random_color())
            turtle.circle(125)  
            turtle.right(25)   
        turtle.done()

![Spirograph 1](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/spirograph1.png)

So we in essence create a screen with a black background and then use a for loop to iterate a predetermined amount of cycles. From there, we create the random colored circle, and then rotate the pen right 25 degrees. We can play with the angle rotation to see how much it effects the output. Also, if we wanted the circles to appear in a linear fashion instead of having them rotate then we can make a couple of adjustments. 

One, we don't need to rotate the circle after each cycle, but instead we need to move it forward by a predetermined amount. If we want to start the drawing at the area located furthest to the left then we can get the width of the screen. Inside of the Screen module is a function called window_width that allows you to get the width of the screen. It’s important that we take the negative of that value and then store it in a variable. We want it to be negative because just like with the x-y Cartesian coordinate system the negative value denotes to the left on the coordinate system. To get the  _left most_  portion of the screen we can do something like the following:

    x = -(turtle.Screen().window_width())



Then, after each iteration we can update the x value and then move the turtle pen to the new location using the penup, pendown, and goto methods. Below is the updated code snippet:

    import turtle
    from random_colors import get_random_color
    def create_circles(cycles=30):
       
        turtle.bgcolor('black')
        turtle.pensize(3)      
        turtle.speed(0)        
        x = -(turtle.Screen().window_width())
        for i in range(cycles):
            turtle.penup()
            turtle.goto(x, 0)
            turtle.pendown()
            turtle.color(get_random_color())
            turtle.circle(100)  
            x += 50
        turtle.done()

![Circle Art](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/circle_art.png)

## Creating Party Lights and Delicious Fruit Candy Pieces With Simple Lines

To create a line in python all you have to do is just move forward with the turtle object. You could also optionally add width to the pen so that the line will have more _thickness_. For example, the following code consists of several lines that rotates 45 degrees each iteration around the origin and kind of mimics a snow flake as shown below:

![Snow flake image](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/snow_flake.png)

#Here's the code snippet for doing this:

    import turtle
    line = turtle.Turtle()
    line.hideturtle()
    line.pensize(3)
    for x in range(8):
        line.forward(200)
        line.goto(0, 0)
        line.left(45)
    turtle.done()

Since we now know how to create lines the next thing to do is to create some computer artwork with them using turtle baby! Let’s do something cool by following this simple algorithm:

-   Generate many lines
-   Use the PyRandomColor  module to randomly color each line
-   Add some thickness to the lines
-   Randomly allocate the x/y coordinates of each line
    
So, pretty much more of the same stuff that we saw previously. Below is how the image looks:

![party lights](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/party_lights.png)

Below is the code for this which is similar to the code used to create the **Nigh**t and **Random Colored Circles**

    import turtle
    from random_colors import get_random_color
    from random import randint
    def create_lights(number=70, angle=20):
        width = turtle.Screen().window_width()
        height = turtle.Screen().window_height()
        screen = turtle.Screen()
        screen.bgcolor('black')
        screen.screensize(width, height)
        turn = angle
        lights = turtle.Turtle()
        lights.speed(0)
        lights.hideturtle()
        for x in range(number):
            x, y = randint(-height, height), randint(-width, width)
            lights.pensize(12)
            lights.pencolor(get_random_color())
            lights.right(turn)
            lights.forward(250)
            lights.penup()
            lights.goto(x, y)
            lights.pendown()
        turtle.done()

There’s no new logic in the code, the only thing you haven’t seen yet is how to control the thickness of the lines. This can be done by calling the pensize method. 
We can in essence take the above logic and manipulate the image slightly by modifying the pensize, aka thickness and the forward function, aka length of the line. Here’s how the modified loop portion of **Party Lights**  look:





## Project: 4 Little Turtles Racing Game

Let’s put our newfound knowledge of the turtle module to the test and build ourselves a simple little game. This game is called _4 Little Turtles_ and it’s actually more of a simulator than a game, but yet we can still get a ton of entertainment from this. Below are the rules to the 4 Little Turtles:

 - [ ] Create a game that consists of 4 little turtles of unique colors.
 - [ ] Include a countdown that starts the game.
 - [ ] Create a graphical finish line with the text “Finish Line” directly above it.
 - [ ] Randomly generate the speed of the turtles.
 - [ ] Write an algorithm to accurately determine which turtle crossed the finish line first.
 - [ ] Write a message to let the user know which turtle won.
 - [ ] Write a simple algorithm to make the winning turtle spin and then grow in size afterwards.
 - [ ] Have fun playing and showing the game off to your friends and family!
 
 Below are some screenshots of how the game looks:

![4 Little Turtles Screenshot 1](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/4_little_turtles_racing_1.png)

![4 Little Turtles 2](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/4_little_turtles_racing_2.png)

![4 Little Turtles 3](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/4_little_turtles_racing_3.png)


![4 Little Turtles 4](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/4_little_turtles_racing_4.png)

## Script Hint

  
Compared to the other programs we created so far I felt that this program would fair better by using the _object oriented_ approach in python. I felt like it would make the program cleaner, more modular, and easier to extend when needed. Below is the list of methods that’s used in the script:

`__init__`: The constructor which creates the four turtle objects along with getting the height and width of the screen.

`start_turtles`: Sets the default positions of the turtles.

`finish_line`: Draws the finish line in the racing game and aligns it on the right hand portion of the screen.

`countdown_timer`: Creates the countdown timer for the script starting at 5. Use the sleep function from the time module to pause the program.

 `set_turtle_speeds`: Randomly sets the speed of the turtles within the range of 1-25.

`turtle_race`: Contains the logic that gets the turtles to start moving towards the finish line.

`victor_dance`: Contains the logic that gets the winning turtle to do a celebratory dance after they win and then grow in size.

`if __name__ == '__main__':` We need to figure out a way to start the game. I’ve decided to use this approach.  It can be used for larger projects to define a starting point of execution of the project. Python doesn’t have an official main method like in C or Java. This is one way in which you can control the flow of execution of a script.

## Solution

  
We can break down the solution of the script down by analyzing the methods. We’ll start at the top and work our way to the bottom. Let’s start with the class declaration and then the constructor or `__init__` method:

    import turtle
    from random import choice
    from time import sleep
    class TurtleRace:
    
        def __init__(self):
            
            self.red = turtle.Turtle(shape='turtle')
            self.blue = turtle.Turtle(shape='turtle')
            self.green = turtle.Turtle(shape='turtle')
            self.black = turtle.Turtle(shape='turtle')
            self.height = turtle.Screen().window_height()
            self.width = -turtle.Screen().window_width() 
            
            self.red_x = self.width + (-self.width/10)
            self.blue_x = self.width + (-self.width/10)
            self.green_x = self.width + (-self.width/10)
            self.black_x = self.width + (-self.width/10)
    
            self.red_y = self.height - (self.height / 1.20)
            self.blue_y = self.height - (self.height / 1.1)
            self.green_y = self.height - (self.height / 1)
            self.black_y = self.height - (self.height / .9)
            
            self.red_speed = 0
            self.blue_speed = 0
            self.green_speed = 0
            self.black_speed = 0
            self.finish = turtle.Turtle()

