
# Building Practical Desktop apps in Python Using The Core Tkinter Library #  
  
Tkinter is the de facto standard GUI in python. It's wired into its core meaning that if you already have python installed then you can simply import the library and start coding away. The Tkinter library is actually a binding to the Tk GUI toolkit.  
  
Tk is a free and open source cross platform widget toolkit that provides a library full of an assortment of GUI widgets in various programming languages. There's other GUI tool kits for python but I've decided to focus on just one in this chapter, and figured that focusing on the one that shipped with python makes the most sense.  
  
There's a lot of functionality in Tkinter, so instead of highlighting a bunch of boring jargon the game plan will be to build something simple first, analyze it, and then work through some more interesting projects. So, let's get started by building a simple GUI program!  
  
## A Simple Tkinter GUI ##  
  
Here's a very basic Tkinter app:  
 
    import tkinter as tk  
    root = tk.Tk()  
    root.title('Simple Tkinter App')  
    root.geometry('500x500')  
    tk.mainloop()  
 

Here’s the output:  

![simple tkinter gui](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_05/Simple_Tkinter_GUI.jpg)
    
  
Woohoo, you've created your first Tkinter app! While this app doesn’t do anything useful it does illustrate some key concepts with Tkinter.  

      
    import tkinter as tk  

  
This statement simply imports the tkinter module. We could have done import tkinter but we save ourselves some extra typing by shortening the text to tk. Also, some developers prefer to import everything from tkinter by doing the following:  
  

    from tkinter import *  

  
However, since we're still learning the ins-and-outs of tkinter it's a bit premature.  
  

    root = tk.Tk()  

  
This starts the tcl/tk interpreter under the cover. Then, the tkinter commands are translated into tcl/tk commands. The main window and the interpreter are linked, and both are needed in order for the tkinter app to work. So, in other words, creating an instance of Tk initializes the interpreter and creates the root window. Next…  
  

    root.title('Simple Tkinter App')

 
The title method allows you to set the title of the app. Nothing tricky!  
  

    root.geometry('500x500')  

  
This sets the dimensions of the window AND to position the window within the user's Desktop. The default size is typically too small so to modify it to the way you like use this method.  
  
In order to specify the dimensions it has to be in the 'widthxheight' format. If you want to specify the location of the app then pass in the arguments after the dimensions in the format x, y. You have to put a plus or minus in front of the values as indicated in the code snippet below:  
  

    root.geometry('500x500+10-10')  

  
The plus value for the x coordinate pushes the window to the left while the minus pushes it to the right; for the y value the + value pushes the window up while the minus value pushes the window down.  
  
Last but not least is the call of the mainloop method which keeps your application running. It functions similar to an infinite loop that you may use when you’re creating a game script.  
  
This code is more or less boilerplate that you can commit to memory so you at least know the basics of setting up your app. The problem with the app is it doesn't process user input and therefore can't interact with the user which negates a crucial benefit of GUIs. Therefore, let's create another silly app which has an input form which asks the user for their name and then displays it. In order to do this we need to know just 3 more things:  
  
1. We need some way to provide instructions to a user, in the way an email form for example may have the text email next to the form, or the text first name next to the form in which you enter in your name. We can accomplish this using the `Label` widget. More on this later...  
2. We need a way so that the user can enter in data into the program. What we need is known as an `Entry` widget. More on this later...  
3. We need a way to process the user input. We can do this yet again with the help of another widget, this time the Button widget. More on this later...  
  
Ok, before moving forward we need to understand what widgets are so let's describe it, and then get to coding the `Name App`.  
  
## The Label, Entry, and Button Widgets ##  
  
Tkinter supports 15 widgets. A widget is an object that provides various controls that the coder can use to integrate with the GUI.  
  
A label as the name suggests allows you to display text or an image on the screen. Below is an example on how to create one:  
  

    name = tk.Label(root, text='Your favorite food?').pack() 

 
So, we call the `Label` method using `tk`, and then pass in the root which is the parent of the class.  
  
We can then make use of the various attributes in the label widget and text is one of them. As the name indicates it allows you to add text to the label.  
  
It's important to note that the size of the label will automatically be set so that all of the characters in the text attribute are displayed. However, there’s an attribute that allows you to use the width and height of the label. Below is a listing of some of the attributes for the label widget.  
  
◦ `width`: Change the width of the label widget. If you set this too small then all of the text won’t show.  
◦ `height`: Adjust the height of the label.  
◦ `bg`: The background color.  
◦ `fg`: The foreground color.  
◦ `bd/borderwidth`: The width of the label border.  
◦ `padx`: Extra horizontal padding to add around the text.  
◦ `pady`: Extra vertical padding to add around text.  
◦ `textvariable`: Associates a Tkinter variable, typically a StringVar with the label.  
  
A good resource that you can use for additional help is: [http://effbot.org/tkinterbook/label.htm](http://effbot.org/tkinterbook/label.htm)  
  
The `pack` method is one of several geometry managers. This will yet be explained later on, but the important thing to know is that without it your label widget won't show up on the GUI. Next, let's briefly learn about the `Entry` label.  

This allows you to collect data from the user in the GUI. Similar to the way in which you'll use the input function from the python core, you can also use this widget to collect data from the user. Below is an example on how to use the `Entry widget` in python:  
  

    first_name = tk.Entry(root).pack()  

  
It has all of the attributes that were previously discussed with label except padx/pady.  
  
Now, if we want text to appear in the `Entry` widget itself then there’s no attribute that we can place within the `Entry` widget. Instead, we need to create what's called a `StringVar` variable, and then pass it in as the text variable value of the `Entry` widget.  
  
A `StringVar` is in essence part of the variable classes in tkinter; there's also the `BooleanVar`, `DoubleVar`, and `IntVar` classes. These serve as wrappers for their respective datatype.  
  
Enough discussing, let's look at some code snippets:  
  

    default_value = tk.StringVar()  

  
In order to use `StringVar` you can use tk to call it. From there, you can use some of the various functions inside of it such as set which sets the default value of this variable, or get which retrieves the value stored. Here's an example on how to use the set method in python:  
  

    default_value.set('pizza?')  

  
In order to make the text 'pizza?' show up in the `Entry` widget you must add the variable name associated with `StringVar` to the `Entry` widgets text variable as shown below:  
  

    first_name = tk.Entry(root, textvariable=default_value).pack() 

 
On to the `Button` widget. Below is an example that not only shows how to create a button in Tkinter but also shows how to tie together the pieces of using a `Label`, layout manager, `StringVar`, get/set, and an `Entry` widget. Here's the code for the simple greetings app:  

    import tkinter as tk
    root = tk.Tk()  # starts a tcl/tk interpreter under the cover
    root.title('Greetings App')
    root.geometry('350x250')
    def greeting():
        greetings = tk.Label(root, bg='tan', borderwidth=3.5, relief='groove', text="Hello {} :-)! Welcome to the wonderful\n"
                                        "world of programming. Enjoy your stay!".format(default_value.get()))
        greetings.pack()
    default_value = tk.StringVar()
    default_value.set('????')
    first_name_label = tk.Label(root, text='What\'s your name?').pack()
    first_name = tk.Entry(root, textvariable=default_value).pack()
    button = tk.Button(text='Click Me!', command=greeting).pack()
    tk.mainloop()

  
The following screenshots illustrates how the GUI works:  
  
![greetings app 1](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_05/Greetings_app_1.jpg)
  
  
Here's the sample output:  
  
![greetings app 2](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_05/Greetings_app_2.jpg)

  
As again, not a ground shattering app but it does its job with providing insights into the possibilities of Tkinter. There's a couple of more things that we should understand until we move onto more advanced Tkinter apps.  
  
Next, we'll learn the geometry manager in Tkinter and the various options for controlling the layout of items in your GUI. Afterwards, we'll cover the remaining widgets and build some simple yet practical apps that can provide insights into what we can accomplish with Tkinter.  
  
## The 3 Ways to Order Widgets in Tkinter ##  
  
There are three ways in which you can control the layout of items in your GUI, they are:  
  
• pack  
• grid  
• place  
  
Before we proceed it's important to know that when you pick a geometry manager you should stick to one as mixing different ones will most likely lead to errors.  
  
## Pack ##  
  
This is the easiest one to use as once you use it the method takes care of the ordering itself. It does this by positioning the elements relative to each other. Here's an example of the pack geometry layout manager in action:  
  

    import tkinter as tk
    root = tk.Tk()
    root.title('Tinker Geometry Managers')
    colors = ['black', 'red', 'orange', 'blue', 'green',
              'yellow', 'brown', 'gold']
    # The label geometry layout manager in Tkinter
    label_one = tk.Label(text='The Black Label').pack()
    label_one_black = tk.Label(root, bg=colors[0]).pack(fill=tk.X)
    label_two = tk.Label(text='The Red Label').pack()
    label_two_red = tk.Label(root, bg=colors[1]).pack(fill=tk.X)
    label_three = tk.Label(text='The Orange Label').pack()
    label_three_orange = tk.Label(root, bg=colors[2]).pack(fill=tk.X)
    label_four = tk.Label(text='The Blue Label').pack()
    label_four_blue = tk.Label(root, bg=colors[3]).pack(fill=tk.X)
    label_five = tk.Label(text='The Green Label').pack()
    label_five_blue = tk.Label(root, bg=colors[4]).pack(fill=tk.X)
    label_six = tk.Label(text='The Yellow Label').pack()
    label_six_yellow = tk.Label(root, bg=colors[5]).pack(fill=tk.X)
    label_seven = tk.Label(text='The Brown Label').pack()
    label_six_brown = tk.Label(root, bg=colors[6]).pack(fill=tk.X)
    label_eight = tk.Label(text='The Gold Label').pack()
    label_six_gold = tk.Label(root, bg=colors[7]).pack(fill=tk.X)
    root.mainloop()

Here's the output:  

![pack geometry manager](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_05/pack_geometry_manager.jpg)
  
As you can see from the above code snippet, the position of the labels are automatically determined. Nothing new added from this code snippet that you haven’t seen before except for the background colors in the labels. Next is an example of the place geometry layout manager.  
  
## Place ##  
  
The place layout manager allows you to do absolute and relative positioning with tkinter. So, you can specify exactly where you want a widget to appear in the GUI. Here’s a code example that shows how to use the place geometry layout manager:  

    import tkinter as tk
    root = tk.Tk()
    root.title('Tinker Place Geometry Manager')
    root.geometry('375x350')
    colors = ['black', 'red', 'orange', 'blue', 'green',
              'yellow', 'brown', 'gold']
    width, height = 0, 0
    for x in range(len(colors)):
        tk.Label(text=colors[x], width=10).place(x=0, y=height)
        tk.Label(bg=colors[x], width=15).place(x=100, y=height)
        height += 15
    tk.mainloop() 

  
  ![place geometry manager](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_05/place_geometry_example.jpg)

  
## Grid ##  
  
The last layout manager to explain is the grid. It organizes components of the GUI by placing them in a 2-dimensional table which consists of rows and columns. Widgets with the same row and column number will be placed on the same line. The size of the grid doesn’t have to be determined because the grid manager automatically takes care of this for you. The below code snippet utilizes the grid manager:  
  

    import tkinter as tk
    root = tk.Tk()
    root.title('Tkinter Grid Geometry Manager')
    root.geometry('875x200')
    colors = ['black', 'red', 'orange', 'blue', 'green',
              'yellow', 'brown', 'gold']
    i = 0
    for x in colors:
        tk.Label(text=x, width=15).grid(row=i+1, column=i)
        tk.Label(bg=x, width=15).grid(row=i, column=i)
        i += 1
    tk.mainloop()


Here's how the GUI looks:  
  
  ![grid layout manager](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_05/grid_layout_manager_example.jpg)
  
  
Before we move on there’s something that I want to get off my chest. I think it's time that we outta convert our procedural GUI programs into their OOP counterparts.  
  
## How to Convert Procedural GUI to Their OOP Counterpart ##  
  
The benefit of converting the procedural styled GUI into OOP is that in essence the program will be more modular and therefore makes debugging more precise. Let's take the very first GUI that we created in this chapter and then convert it to OOP style. To do this we need to accomplish 5 things:  
  
1. We need to create a class.  
1. We need to create a constructor using the __init__ method.  
1. We need to prepend the self convention in front of the variables.  
1. We need to create an instance of the class.  
1. We need to call the mainloop method.  
  
Below is the Simple Tkinter GUI we created earlier in this chapter converted into OOP:  

    import tkinter as tk
    class HelloWorld:
        def __init__(self):
            self.root = tk.Tk()
            self.root.title('Simple Tkinter Class Example')
            self.root.geometry('500x500')
    if __name__ == '__main__':
        app = HelloWorld()
        tk.mainloop()

From now on this is the style we will use to create our GUIs.  
  
Now that we’ve got the basics of Tkinter under control the next step is to put all of our newfound knowledge to use by building some simple yet practical Tkinter apps. We'll convert a command line program that we created in Chapter II into a GUI program and also work through two more interesting projects.  
  
## Project: Temperature Converter GUI  
  
Here's a screenshot of how the app looks:  

![temperature converter gui](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_05/temperature_converter_gui.jpg)
  
  
## Script Hint  
  
__init__: The constructor will initialize the instance variables and do the initial setup for the program. In here a TK instance will be created and the title, size, and the background color set. The instance variables that will be used throughout the program are created here.  
  
**fahrenheit_to_celsius**: This is the method that will calculate the conversion of Fahrenheit to Celsius.  
  
**celsius_to_fahrenheit**: This is the method that will convert from Celsius to Fahrenheit.  
  
**create_widget**s: In this method we’ll create and configure the various widgets that will be used throughout such as the `Label`, `Button`, and `Entry` widgets.  
  
**if __name__ == '__main__**': This is the entry point of the program. An instance of the class will be created and then the various methods will be invoked all followed by a call to mainloop.  
  
Now that we have the script broken down into methods, we can go ahead and start writing the program.  
  
## Solution ##  
  
Here's the initial portion of the script.  

    import tkinter as tk
    from tkinter import Tk, Label, Button, Entry, StringVar
    class Temperature:
        def __init__(self):
            self.root = Tk()
            self.root.title('Temperature Converter App')
            self.root.geometry('500x150')
            self.root.configure(bg='tan')
            # Gets the user input
            self.get_fahren = StringVar()
            self.get_celsius = StringVar()
            # Sets the user input. By default
            # its default values are ° F and ° C
            self.get_fahren.set('° F')
            self.get_celsius.set('° C')

 
As you can see tkinter as well as the various modules that will be used are individually imported. That way, we don't have to invoke tk each time we want to use them. The `get_fahren` and `get_celsius` variables will be used to get the input that the user entered into the program. The following methods will take the input that the user entered and then convert it to its appropriate temperature scale:  
  
       def fahrenheit_to_celsius(self):
            """
            Fahrenheit to Celsius formula is:
            (x - 32) * 5/ 9
            """
            try:
                celsius = float(self.get_fahren.get())
                result = (celsius - 32) * 5 / 9
                result = str(round(result, 3)) + '° C'  # rounds float to 3 places, then converts to string
                self.get_fahren.set(result)
            except ValueError as e:
                self.get_fahren.set('ERROR!!!')

  
We must first get the value that the user entered into the program which is done in this line of code:  
  

    celsius = float(self.get_fahren.get()) 

 
The `get` method allows us to get the value that the user entered, convert it to a float, and then execute the rest of the equation. Once the equation is executed the value is set. The `try/except` statement catches any non-numerical value that's trying to be added to the equation. Below is the `celsius_to_fahrenheit` equation which is more or less the same logic except with a different equation:  
  

     def celsius_to_fahrenheit(self):
            """
            Celsius to Fahrenheit formula is:
            F = (x x 9/5) + 32
            """
            try:
                fahrenheit = float(self.get_celsius.get())
                result = (fahrenheit * 9 / 5) + 32
                result = str(round(result, 3)) + '° F'   
                self.get_celsius.set(result)
            except ValueError as e:
                self.get_celsius.set('ERROR!!!') 

  
The following method creates the widgets that will be used and then positions them using the place layout manager.  
  

     def create_widgets(self):
            """
            arranges the labels,
            Entry, and buttons.
            """
            fahrenheit_to_celsius_label = Label(text='Temperature in Fahrenheit').place(x=0, y=0)
            fahrenheit_to_celsius_widget = Entry(text='enter temperature', textvariable=self.get_fahren, bg='white smoke').place(x=200, y=0, width=225)
            fahrenheit_to_celsius_button = Button(text='convert', width=15, border=2, command=self.fahrenheit_to_celsius)
            fahrenheit_to_celsius_button.place(x=200, y=25, width=150)
            # celsius to fahrenheit label, widget, and button
            celsius_to_fahrenheit_label = Label(text='Temperature in Celsius').place(x=0, y=85)
            read_celsius_widget = Entry(text='enter temperature', textvariable=self.get_celsius, bg='white smoke').place(x=200, y=85, width=225)
            celsius_to_fahren_button = Button(text='convert', width=15, border=2, command=self.celsius_to_fahrenheit)
            celsius_to_fahren_button.place(x=200, y=115, width=150)


Note, that with the place layout manager you can set the absolute positioning of the widgets. Remember, the `Label` widget just allows us to display text or images on the screen, and the `Entry` widget allows us to collect or display a single line of text. The `Entry` widgets have a keyword argument of textvariable which is set to `self.get_fahren` and `self.get_celsius` for the appropriate `Entry` widgets. 

This allows us to get the user input, and then the temperature conversion is done when the appropriate button is clicked. The button executes the appropriate method that does the conversion of Fahrenheit to Celsius and vice-versa. Remember, the buttons can execute the appropriate method when clicked on by using the `command=self.some_method` as a keyword argument. The last step is to set everything up and to then run the program. This is done in the following code snippet:  
  

    if __name__ == '__main__':
        app = Temperature()
        app.create_widgets()
        tk.mainloop()) 

 
The `if __name__ == '__main__'` conditional is started which serves as the entry point to the program, and then an instance of the class is created along with a call to the `create_app` method. Lastly, the mainloop method is called which emulates an infinite loop and keeps the GUI active until closed.  
  
  
## Project: BMI Calculator App ##  
  
Body mass index or BMI for short is the acronym for body mass index. It's a standard for estimating a healthy weight for individuals. The formula works by taking the body mass of an individual and dividing it by the square of the body height. We'll design a GUI that accepts the height and weight of an individual in the following units:  
  
• Height in feet  
• Weight in pounds  
• Height in meters  
• Weight in kilograms  
  
Below is a screenshot of the finished BMI Calculator that we'll be building:  

![bmi calculator app](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_05/body_mass_index_calculator.jpg)


## Program Hint

We can use a similar template to create this GUI for the one we used to create the Temperature Desktop app. Here’s an outline of methods that you can use to create the app:

__init__: Here you can initialize the variables that will be used throughout the program. 

**create_widgets**: This method creates and places the Label, Entry, and Button widgets on your GUI. 

**weight_in_pounds**:  Accepts the weight in pounds and height in feet and then calculates the BMI. 

**weight_in_kilograms**: Accepts the weight in kilograms and height in meters and then calculates the BMI. 

**run**: This is the method that will contain all of the setup steps for the GUI. 

## Solution

Let’s get the basic stuff out of the way such as the class and __init__ method:

    class BMICalculator:
        def __init__(self, master):
            self.height_in_feet = tk.StringVar()
            self.weight_in_pounds = tk.StringVar()
            self.pounds_bmi = tk.StringVar()
            self.height_in_meters = tk.StringVar()
            self.weight_in_kilos = tk.StringVar()
            self.kilos_bmi = tk.StringVar()

The above are just the variables that will be manipulated throughout the program. Let’s next create all of the widgets that will be used throughout the program and wrap them inside a method: 

     def create_widgets(self):
        bmi_feet_inches_label = Label(text='Enter height in feet')
        bmi_feet_inches_label.place(x=0, y=0, height=25, width=250)
    
        bmi_feet_inches_entry = Entry(textvariable=self.height_in_feet)
        bmi_feet_inches_entry.place(x=275, y=0, height=25, width=250)
        bmi_feet_inches_entry.config(highlightbackground='white smoke')
    
        height_inches_label = Label(text='Enter weight in pounds')
        height_inches_label.place(x=0, y=40, height=25, width=250)
    
        weight_pounds_entry = Entry(textvariable=self.weight_in_pounds)
        weight_pounds_entry.place(x=275, y=40, height=25, width=250)
        weight_pounds_entry.config(highlightbackground='white smoke')
    
        bmi_button = Button(text='Find BMI', command=self.weight_in_pounds)
        bmi_button.place(x=50, y=80, width=100)
    
        display_bmi_inches = Entry(textvariable=self.pounds_bmi)
        display_bmi_inches.place(x=200, y=80, height=25, width=100)
        display_bmi_inches.config(highlightbackground='black', bg='lavender')  
    
        Label(bg='black', fg='white', text='BMI Weight Status').place(x=325, y=80)
        Label(bg='floral white', text='Below 18.5     Under weight').place(x=325, y=95)
        Label(bg='azure', text='Below 18.5-24.9     Normal weight').place(x=325, y=110)
        Label(bg='yellow', fg='black', text='Below 25.0-29.9     Over weight').place(x=325, y=125)
        Label(bg='red', fg='white', text='30.0 and above     Obese').place(x=325, y=140)
    
        meters_and_kilo_label = Label(text='Enter height in meters')
        meters_and_kilo_label.place(x=100, y=200, width=400)
        height_meters_label = Label(text='Enter height in meters')
        height_meters_label.place(x=0, y=250, height=25, width=250)
        height_meters_entry = Entry(textvariable=self.height_in_meters)
        height_meters_entry.place(x=275, y=250, height=25, width=250)
        height_meters_entry.config(highlightbackground='white smoke')
    
        bmi_meters_kilo_label = Label(text='Enter weight in kilograms')
        bmi_meters_kilo_label.place(x=0, y=300, height=25, width=260)
        bmi_meters_kilo_entry = Entry(textvariable=self.weight_in_kilos)
        bmi_meters_kilo_entry.place(x=275, y=300, height=25, width=260)
        bmi_meters_kilo_entry.config(highlightbackground='white smoke')
    
        bmi_button_meters = Button(text='Find BMI', command=self.weight_in_kilograms)
        bmi_button_meters.place(x=50, y=350, width=100)
    
        display_bmi_meters = Entry(textvariable=self.kilos_bmi)
        display_bmi_meters.place(x=200, y=350, height=25, width=100)
        display_bmi_meters.config(highlightbackground='black', bg='lavender')


The `Labels`, `Entry`, and `Button` widgets are created here. Let’s focus on the config method; it’s called on the `Entry` widgets and allows you to set the background color of that widget. Let’s inspect this portion of the GUI:

![bmi weight status labels](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_05/bmi_weight_status_labels.jpg)


These are simply labels that corresponds to this portion of the code:

	    Label(bg='black', fg='white', text='BMI Weight Status').place(x=325, y=80)
        Label(bg='floral white', text='Below 18.5     Under weight').place(x=325, y=95)
        Label(bg='azure', text='Below 18.5-24.9     Normal weight').place(x=325, y=110)
        Label(bg='yellow', fg='black', text='Below 25.0-29.9     Over weight').place(x=325, y=125)
        Label(bg='red', fg='white', text='30.0 and above     Obese').place(x=325, y=140)

The next step is to create the methods that does the BMI computation contingent on the values:

     def bmi_in_pounds(self):
           
            inches = float(self.height_in_feet.get()) * 12
            pounds = float(self.weight_in_pounds.get())
            bmi = round(float(pounds / (inches ** 2)) * 703, 2)
            self.pounds_bmi.set(bmi)

The appropriate values entered into the GUI are retrieved by calling the get method on `self.height_in_feet` and `self.weight_in_pounds`. The formula is then executed and the result is stored in `pounds_bmi`. The `weight_in_kilograms` method is the same logic with the exception of a different formula being used:


     def weight_in_kilograms(self):
    
            meters = float(self.height_in_meters.get())
            kilograms = float(self.bmi_meters_kilo_entry.get())
            bmi = round(float(kilograms / (meters ** 2)), 2)
            self.kilos_bmi.set(bmi)

It’s time to test that everything finally works. In this app we’re going to take a different approach to running the file compared to the Temperature app. What we’re going to do is create a function that does all of the setup for the GUI and then within the if conditional calls the run function. Below is how the run function looks: 

    def run():
        root = tk.Tk()
        root.title('Body Mass Index Calculator')
        root.geometry('600x600')
        root.configure(bg='AntiqueWhite2')
        app = BMICalculator(root)
        app.create_widgets()
        tk.mainloop()

The `run` function calls the Tk constructor which allows us to use the various functionality built into the package such as setting the title, size, and configuring the bg color for the GUI. 

From there we create an instance of the class and pass in the root and then call the create_widgets method belonging to the `BMICalculator` class, and the mainloop method to get the GUI to constantly run. From there we can use the `if __name__ == ‘__main__` functionality to create the entry point to our script and then within it call the run function as shown below:

    if __name__ == '__main__':
        run()

Note, `run` is a function because it’s declared outside of the `BMICalculator` class. 

Access the full program here: [insert link]

## Project: The Secret Number Game

We want to create a classic number guessing game in which the player in essence plays against the computer. Given a range of possible numbers from 1-100 we can create a game.  Here’s some screenshots from that game: 

![guessing game 1](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_05/guessing_game_1.jpg)

![guessing game 2](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_05/guessing_game_2.jpg)

![guessing game 3](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_05/guessing_game_3.jpg)

The above screenshots in a nutshell shows how this game works. But, here are the rules just in case:

1. The program will randomly generate a secret number from 1...100.
2. The program will randomly generate the number of tries that the user can take form 1… 15.
3. The program will list how many tries the user has left.
4. If the user ran out of number of tries then the program will notify them of that and then display a message that the game is over. The user should not be able to make additional guesses.
5. If the user guesses the right secret number then the correct number will be displayed.

## Script Hint

Like the previous GUIs we created we can break this program down into methods.

 __init__: This is where we’ll initialize the variables that will be used throughout the program.

 **create_widgets**: This is where the `Label`, `Entry`, and `Button` widgets are created.

**guess**: This is where the logic is done that determines if the user input is equal to that of the secret number. A loop is actually not needed because an implicit infinite loop is done when the mainloop method is called.

**run**: This does all of the setup for the GUI.

`if __name__ == ‘__main__’`: This serves as the entry point to the program.

## Solution

Now, let’ s analyze the code…

    from random import randint
    from tkinter import Tk, Label, Entry, Button, StringVar	
    class SecretNumberGame:
        def __init__(self):
            self.root = Tk()
            self.secret_number = randint(1, 100)
            self.tries = (randint(1, 15))
            # a list of StringVars
            self.secret_num_str_var = StringVar()
            self.secret_num_str_var.set('Secret Number is ?????')
            self.your_guess = StringVar()
            self.hint = StringVar()

All of the variables that’s used throughout the program will be added here. The next step is to create a method that setup all of the widgets that will be used in the program:

    def create_widgets(self):
        # Labels
        game_banner = Label(text='Guess Any Number From 1-100').place(x=0, y=0, width=500, height=50)
        guess_number_label = Label(text='Guess Number').place(x=50, y=85, width=100)
        your_tries = Label(text=f'You have {self.tries} tries').place(x=225, y=160, width=200)
        # Entry Widgets
        guess_number_widget = Entry(textvariable=self.your_guess).place(x=225, y=75, height=40, width=150)
        the_secret_number = Entry(textvariable=self.secret_num_str_var).place(x=225, y=250, width=175,
                                                                                      height=25)
        # Button
        guess_budget = Button(text='Guess', command=self.guess).place(x=225, y=125, width=125)

Three labels, two entries, and one button widget are created here. The place method is again used to layout the widgets in the GUI. A header is created that serves as a way to add a little style to the GUI. Next, let’s dig into the guess method which serves as the logic to the game play. Below is the `guess` method:

    def guess(self):
        """
        method updates the GUI
        after each user guess.
        """
        your_guess = self.your_guess.get()
        your_guess = int(your_guess)
        if self.tries == 1:
            your_tries = Label(text=f'Game Over!!!').place(x=225, y=160, width=200)
            self.secret_num_str_var.set(self.secret_number)
            Label(text=f'{  self.secret_number} is the secret number!').place(x=225, y=230, width=250)
            your_tries = Label(text=f'You have {0} tries').place(x=225, y=180, width=200)
        elif your_guess > self.secret_number:
            self.tries -= 1
            Label(text=f'{your_guess} is too big').place(x=225, y=160, width=200)
            your_tries = Label(text=f'You have {self.tries} tries').place(x=225, y=180, width=200)
        elif your_guess < self.secret_number:
            self.tries -= 1
            Label(text=f'{your_guess} is too small').place(x=225, y=160, width=200)
            your_tries = Label(text=f'You have {self.tries} tries').place(x=225, y=180, width=200)
        else:
            self.tries = 1
            your_tries = Label(text=f'You Win!!!').place(x=225, y=160, width=200)
            self.secret_num_str_var.set(self.secret_number)
            Label(text=f'{self.secret_number} is the secret number!').place(x=225, y=230, width=250)


The first thing we need to do is get the user input which is done in this line of code:

    your_guess = self.your_guess.get()

However, since the input is received a StringVar will be converted into an int which is done in this line snippet:

    your_guess = int(your_guess)

Easy enough, ok, so as mentioned in the hint we don’t have to include a loop because an infinite loop is running in the background once the script starts. However, what we need to do is start with a counter and decrement the counter each time until we’ve found a match or until the counter is equal to 1. In our case the counter is `self.tries` which is the random number of tries that’s generated within the range of 1… 15. Here’s the code snippet for this:


    if self.tries == 1:
            your_tries = Label(text=f'Game Over!!!').place(x=225, y=160, width=200)
            self.secret_num_str_var.set(self.secret_number)
            Label(text=f'{  self.secret_number} is the secret number!').place(x=225, y=230, width=250)
            your_tries = Label(text=f'You have {0} tries').place(x=225, y=180, width=200)

 
If `self.tries` is equal to 1 then the `Label` is updated to let the player know that the game is over. 

The remaining parts of the chained conditional just checks to see if the player’s guess was larger or smaller than that of the secret number. If those conditional checks evaluate to `False` then we can assume that the user guessed the correct number. If that’s the case then the `Label` is updated letting them know that they guessed the correct number. The `self.tries` instance variable is set equal to 1 so that the user can’t continue guessing after they won because that’s not acceptable game play. The `run` method simply sets up the GUI, calls create_widgets, and then calls mainloop:

    def run(self):
        """
        Setups the basics of the app.
        """
        self.root.title('Secret Number Game')
        self.root.config(bg='tan')
        self.root.geometry('500x500')
        self.create_widgets()
        self.root.mainloop()

And that’s all there is to the Secret Number Game GUI.
  
  
  
Image: Body Mass Index Calculator Screenshot.  
  
  
## Program Hint ##  
  
We can use a similar template to create this GUI for the one we used to create the Temperature Desktop app. Here’s an outline of methods that you can use to create the app:  
  
__init__: Here you can initialize the variables that will be used throughout the program.  
  
**create_widgets**: This method creates and places the Label, Entry, and Button widgets on your GUI.  
  
**weight_in_pounds**: Accepts the weight in pounds and height in feet and then calculates the BMI.  
  
  
**weight_in_kilograms**: Accepts the weight in kilograms and height in meters and then calculates the BMI.  
  
**run**: This is the method that will contain all of the setup steps for the GUI.  
  
## Solution ##  
  
Let’s get the basic stuff out of the way such as the class and __init__ method:  
  
  

    class BMICalculator:
        def __init__(self, master):
            self.height_in_feet = tk.StringVar()
            self.weight_in_pounds = tk.StringVar()
            self.pounds_bmi = tk.StringVar()
            self.height_in_meters = tk.StringVar()
            self.weight_in_kilos = tk.StringVar()
            self.kilos_bmi = tk.StringVar()

The above are just the variables that will be manipulated throughout the program. Let's next create all of the widgets that will be used throughout the program and wrap them inside a method:  

    def create_widgets(self):
        bmi_feet_inches_label = Label(text='Enter height in feet')
        bmi_feet_inches_label.place(x=0, y=0, height=25, width=250)
    
        bmi_feet_inches_entry = Entry(textvariable=self.height_in_feet)
        bmi_feet_inches_entry.place(x=275, y=0, height=25, width=250)
        bmi_feet_inches_entry.config(highlightbackground='white smoke')
    
        height_inches_label = Label(text='Enter weight in pounds')
        height_inches_label.place(x=0, y=40, height=25, width=250)
    
        weight_pounds_entry = Entry(textvariable=self.weight_in_pounds)
        weight_pounds_entry.place(x=275, y=40, height=25, width=250)
        weight_pounds_entry.config(highlightbackground='white smoke')
    
        bmi_button = Button(text='Find BMI', command=self.weight_in_pounds)
        bmi_button.place(x=50, y=80, width=100)
    
        display_bmi_inches = Entry(textvariable=self.pounds_bmi)
        display_bmi_inches.place(x=200, y=80, height=25, width=100)
        display_bmi_inches.config(highlightbackground='black', bg='lavender')  
    
        Label(bg='black', fg='white', text='BMI Weight Status').place(x=325, y=80)
        Label(bg='floral white', text='Below 18.5     Under weight').place(x=325, y=95)
        Label(bg='azure', text='Below 18.5-24.9     Normal weight').place(x=325, y=110)
        Label(bg='yellow', fg='black', text='Below 25.0-29.9     Over weight').place(x=325, y=125)
        Label(bg='red', fg='white', text='30.0 and above     Obese').place(x=325, y=140)
    
        meters_and_kilo_label = Label(text='Enter height in meters')
        meters_and_kilo_label.place(x=100, y=200, width=400)
        height_meters_label = Label(text='Enter height in meters')
        height_meters_label.place(x=0, y=250, height=25, width=250)
        height_meters_entry = Entry(textvariable=self.height_in_meters)
        height_meters_entry.place(x=275, y=250, height=25, width=250)
        height_meters_entry.config(highlightbackground='white smoke')
    
        bmi_meters_kilo_label = Label(text='Enter weight in kilograms')
        bmi_meters_kilo_label.place(x=0, y=300, height=25, width=260)
        bmi_meters_kilo_entry = Entry(textvariable=self.weight_in_kilos)
        bmi_meters_kilo_entry.place(x=275, y=300, height=25, width=260)
        bmi_meters_kilo_entry.config(highlightbackground='white smoke')
    
        bmi_button_meters = Button(text='Find BMI', command=self.weight_in_kilograms)
        bmi_button_meters.place(x=50, y=350, width=100)
    
        display_bmi_meters = Entry(textvariable=self.kilos_bmi)
        display_bmi_meters.place(x=200, y=350, height=25, width=100)
        display_bmi_meters.config(highlightbackground='black', bg='lavender')

  
The `Labels`, `Entry`, and `Button` widgets are created here. Let's focus on the config method; it's called on the `Entry` widgets and allows you to set the background color of that widget. Let's inspect this portion of the GUI:  
  
  
These are simply labels that corresponds to this portion of the code:  

    Label(bg='black', fg='white', text='BMI Weight Status').place(x=325, y=80)
        Label(bg='floral white', text='Below 18.5     Under weight').place(x=325, y=95)
        Label(bg='azure', text='Below 18.5-24.9     Normal weight').place(x=325, y=110)
        Label(bg='yellow', fg='black', text='Below 25.0-29.9     Over weight').place(x=325, y=125)
        Label(bg='red', fg='white', text='30.0 and above     Obese').place(x=325, y=140) 

  
The next step is to create the methods that does the BMI computation contingent on the values:  

     def bmi_in_pounds(self):
           
            inches = float(self.height_in_feet.get()) * 12
            pounds = float(self.weight_in_pounds.get())
            bmi = round(float(pounds / (inches ** 2)) * 703, 2)
            self.pounds_bmi.set(bmi) 

  
The appropriate values entered into the GUI are retrieved by calling the get method on `self.height_in_feet` and `self.weight_in_pounds`. The formula is then executed and the result is stored in `pounds_bmi`. The `weight_in_kilograms` method is the same logic with the exception of a different formula being used:  

      def weight_in_kilograms(self):
    
            meters = float(self.height_in_meters.get())
            kilograms = float(self.bmi_meters_kilo_entry.get())
            bmi = round(float(kilograms / (meters ** 2)), 2)
            self.kilos_bmi.set(bmi)
      
It's time to test that everything finally works. In this app we're going to take a different approach to running the file compared to the Temperature app. What we're going to do is create a function that does all of the setup for the GUI and then within the if conditional calls the run function. Below is how the run function looks:  
  

    def run():
        root = tk.Tk()
        root.title('Body Mass Index Calculator')
        root.geometry('600x600')
        root.configure(bg='AntiqueWhite2')
        app = BMICalculator(root)
        app.create_widgets()
        tk.mainloop()


The `run` function calls the Tk constructor which allows us to use the various functionality built into the package such as setting the title, size, and configuring the bg color for the GUI. From there we create an instance of the class and pass in the root and then call the `create_widget`s method belonging to the `BMICalculator` class, and the mainloop method to get the GUI to constantly run. From there we can use the `if __name__ == '__main__'` functionality to create the entry point to our script and then within it call the run function as shown below:  
  

    if __name__ == '__main__':
        run()

Note, run is a function because it's declared outside of the `BMICalculator` class.  
  
Access the full program here: [insert link]  
  
## Project: The Secret Number Game ##  
  
We want to create a classic number guessing game in which the player in essence plays against the computer. Given a range of possible numbers from 1-100 we can create a game. Here's some screenshots from that game:  
 
The above screenshots in a nutshell shows how this game works. But, here are the rules just in case:  
  
1. The program will randomly generate a secret number from 1...100.  
2. The program will randomly generate the number of tries that the user can take form 1 ... 15.  
3. The program will list how many tries the user has left.  
4. If the user ran out of number of tries then the program will notify them of that and then display a message that the game is over. The user should not be able to make additional guesses.  
5. If the user guesses the right secret number then the correct number will be displayed.  
  
  
## Script Hint ##  
  
Like the previous GUIs we created we can break this program down into methods.  
  
`__init__`: This is where we'll initialize the variables that will be used throughout the program.  

`create_widgets`: This is where the Label, Entry, and Button widgets are created.  

`guess`: This is where the logic is done that determines if the user input is equal to that of the secret number. A loop is actually not needed because an implicit infinite loop is done when the mainloop method is called.  
  
`run`: This does all of the setup for the GUI.  
  
`if __name__ == '__main__'`: This serves as the entry point to the program.  
  
## Solution ##  
  
Now, let's analyze the code...  
  

    from random import randint
    from tkinter import Tk, Label, Entry, Button, StringVar	
    class SecretNumberGame:
        def __init__(self):
            self.root = Tk()
            self.secret_number = randint(1, 100)
            self.tries = (randint(1, 15))
            # a list of StringVars
            self.secret_num_str_var = StringVar()
            self.secret_num_str_var.set('Secret Number is ?????')
            self.your_guess = StringVar()
            self.hint = StringVar()

  
All of the variables that's used throughout the program will be added here. The next step is to create a method that setup all of the widgets that will be used in the program:  

    def create_widgets(self):
        # Labels
        game_banner = Label(text='Guess Any Number From 1-100').place(x=0, y=0, width=500, height=50)
        guess_number_label = Label(text='Guess Number').place(x=50, y=85, width=100)
        your_tries = Label(text=f'You have {self.tries} tries').place(x=225, y=160, width=200)
        # Entry Widgets
        guess_number_widget = Entry(textvariable=self.your_guess).place(x=225, y=75, height=40, width=150)
        the_secret_number = Entry(textvariable=self.secret_num_str_var).place(x=225, y=250, width=175,
                                                                                      height=25)
        # Button
        guess_budget = Button(text='Guess', command=self.guess).place(x=225, y=125, width=125)



 
  
Three labels, two entries, and one button widget are created here. The place method is again used to layout the widgets in the GUI. A header is created that serves as a way to add a little style to the GUI. Next, let's dig into the guess method which serves as the logic to the game play. Below is the guess method:  
  

    def guess(self):
        """
        method updates the GUI
        after each user guess.
        """
        your_guess = self.your_guess.get()
        your_guess = int(your_guess)
        if self.tries == 1:
            your_tries = Label(text=f'Game Over!!!').place(x=225, y=160, width=200)
            self.secret_num_str_var.set(self.secret_number)
            Label(text=f'{  self.secret_number} is the secret number!').place(x=225, y=230, width=250)
            your_tries = Label(text=f'You have {0} tries').place(x=225, y=180, width=200)
        elif your_guess > self.secret_number:
            self.tries -= 1
            Label(text=f'{your_guess} is too big').place(x=225, y=160, width=200)
            your_tries = Label(text=f'You have {self.tries} tries').place(x=225, y=180, width=200)
        elif your_guess < self.secret_number:
            self.tries -= 1
            Label(text=f'{your_guess} is too small').place(x=225, y=160, width=200)
            your_tries = Label(text=f'You have {self.tries} tries').place(x=225, y=180, width=200)
        else:
            self.tries = 1
            your_tries = Label(text=f'You Win!!!').place(x=225, y=160, width=200)
            self.secret_num_str_var.set(self.secret_number)
            Label(text=f'{self.secret_number} is the secret number!').place(x=225, y=230, width=250)

The first thing we need to do is get the user input which is done in this line of code:  
  

    your_guess = self.your_guess.get() 

However, since the input is received a `StringVar` will be converted into an int which is done in this line snippet:  
  

    your_guess = int(your_guess) 

 
Easy enough, ok, so as mentioned in the hint we don't have to include a loop because an infinite loop is running in the background once the script starts. However, what we need to do is start with a counter and decrement the counter each time until we've found a match or until the counter is equal to 1. In our case the counter is self.tries which is the random number of tries that's generated within the range of 1 ... 15. Here's the code snippet for this:  
  

    if self.tries == 1:
            your_tries = Label(text=f'Game Over!!!').place(x=225, y=160, width=200)
            self.secret_num_str_var.set(self.secret_number)
            Label(text=f'{  self.secret_number} is the secret number!').place(x=225, y=230, width=250)
            your_tries = Label(text=f'You have {0} tries').place(x=225, y=180, width=200)

  
If `self.tries` is equal to 1 then the `Label` is updated to let the player know that the game is over.  
  
The remaining parts of the chained conditional just checks to see if the player's guess was larger or smaller than that of the secret number. If those conditional checks evaluate to `False` then we can assume that the user guessed the correct number. 

If that's the case then the `Label` is updated letting them know that they guessed the correct number. The `self.tries` instance variable is set equal to 1 so that the user can't continue guessing after they won because that's not acceptable game play. The run method simply sets up the GUI, calls `create_widgets`, and then calls mainloop:  
  

    def run(self):
        """
        Setups the basics of the app.
        """
        self.root.title('Secret Number Game')
        self.root.config(bg='tan')
        self.root.geometry('500x500')
        self.create_widgets()
        self.root.mainloop()

  
To start the GUI use the if __name__ == ‘__main__’ condition:  
  

    if __name__ == '__main__':
        SecretNumberGame().run()

  
And that’s all there is to the Secret Number Game GUI.


## The best way to support this project is to [purchase a digital copy](https://www.amazon.com/Code-Cool-Stuff-Python-Purcell-ebook/dp/B081XJMNRB) on Amazon and leave a review. 
