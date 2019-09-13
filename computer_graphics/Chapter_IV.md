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

  

The first thing we need to do is import the turtle module so that we can use all of the builtin functionality. Check out all of the features of the turtle module here: [https://docs.python.org/3.3/library/turtle.html?highlight=turtle](https://docs.python.org/3.3/library/turtle.html?highlight=turtle)

  

After the turtle module is imported we can go ahead and call the `Turtle()` constructor. From there we can change the default shape of the turtle object to something more appealing like you guessed it, a turtle. From there we can call various functions on it to manipulate its appearance such as `shapesize()` and `color()`. We must then use the `done()` method to start the event loop which in essence calls the Tkinter’s main loop function. We'll learn about Tkinter in Chapter V but just remember that into the meantime you need it at the end of your program.
