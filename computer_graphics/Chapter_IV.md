# **Chapter IV: Crafting Catchy Computer Art with Python Turtle**


## Geometry 101: Learning How to Create Shapes

Let's create the following image:

![Big Green Turtle](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/computer_graphics/images/big_green_turtle.png)

Below is the code for it:

 
    import turtle
    leonardo = turtle.Turtle()
    leonardo.shape(**'turtle'**)
    leonardo.shapesize(7.5, 7.5)
    leonardo.color(**'green'**)
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

Here's a quick explanation. To randomly fill in the inner and outer colors of a turtle object you need to do two things: use the color  function and then pass in the `get_random_color` method twice from the `random_colors` module.  Remember, when you specify two arguments the first one is the outer color while the second one is for the  inner color. To get the color to generate we need to include the `begin_fill` method call before the loop and the `end_fill`  after it.

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
