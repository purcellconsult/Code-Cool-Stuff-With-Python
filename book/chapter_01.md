
# A Merry Overview of The Python Programming Language

Learning the basics of any language isn’t necessary the funnest parts, but it’s definitely a necessary evil. I’ve condensed the basics of python into a single chapter so that we can start building more interesting programs in the subsequent chapters. Learn how to install python on your machine, get acquainted with the free PyCharm editor, learn primary data types, master core data structures, build reusable code with functions, study object oriented programming, and learn how to construct try/except statements.

# Getting python installed on your machine

Just like python is renowned for it’s simplicity, the same can be said about it’s installation procedure. Below are the steps on how to quickly install python on all of the major operating systems. If you already have python installed then you can fast-forward to the _Setting up PyCharm_ section.

## Install Python on Windows

There’s a high probability that if you’re using a Windows powered machine that Python won't be there by default. To discover if Python is indeed installed you can open up command prompt by typing _cmd_ in the search bar  followed by the word  _python_. If there  the python interpreter will run;  otherwise you’ll get an  annoying message like the following:

*'python' is not recognized as an internal or external command, operable program or batch file*

This tells you the sad news that Python is not installed and that you have to set it up. Follow the steps below to make that happen:

****Step one****: Download the latest version of python on your machine: [https://www.python.org/downloads](https://www.python.org/downloads)

****Step two****: Start the Windows installer that matches your system. If you click “Install Now” then Python is installed in the “user” directory, but if you change its location then just remember where it’s installed.

****Step three****: You’ll have an option to add Python to PATH which is where the computer searches for Python when you type it via command prompt. If you check this box then Python will be available via this option, if not then an error will occur. Therefore, it’s a good idea to go ahead and check this option so that you can type in python commands via command prompt. If you installed Python without selecting this option then no biggie as you can manually add the path to your system. Below are the steps:

-   In the Windows menu search for _advanced system settings._
    
-   In the window that displays click __Environment Variables__.
    
-   In the next window, find and select the user variable called path and click __Edit__.
    
-   Scroll to the end of the value and add a semicolon (;) followed by the location of __python.exe__. If you didn’t change the default installation location it should be located in your user directory.
    
-   Click OK to save the settings.

If you don’t know the location of python.exe then don’t panic, just search for *python.exe* in the Windows menu. Once located, right click the file, select properties, and view the Location. Right click to copy the full path and then paste it at the end of the Path user variable. If you don’t have one then click the new button, add a variable named Path, and then add the value which is the location or “path” of the python.exe file. Once done type “python” into the terminal to ensure that everything was set up properly and that it runs.

 ## Install Python on macOS

Like Linux, Python is already installed on a variety of OS X systems. You can confirm that Python is installed by going to: __Applications → Utilities → Terminal__. Next, type the following into the terminal:

    $ python --version

The command will output the version of Python which is:

Python 3.7.3

One way to install the latest-and-greatest version of python on macOS is to use the [appropriate](https://www.python.org/downloads) [m](https://www.python.org/downloads)[acOS installer](https://www.python.org/downloads)  that matches your system: [https://www.python.org/downloads](https://www.python.org/downloads/)

## Installing Python on Linux (Ubuntu 18.04)

To see if Python is installed on your machine open up the terminal and type in the following:

    $ python

You can fire-up the terminal by using the keyboard shortcut: __ctr + alt + t__.

  

The output should look something like the following:

    Python 3.7.3 |Anaconda, Inc.| (default, Apr 29 2018, 16:14:56)
    
    [GCC 7.2.0] on linux
    
    Type "help", "copyright", "credits" or "license" for more information.

  
If you got something like this then __woot-woot__, Python 3.7.3 is installed on your machine. If Python 2.7 or later is installed then it’s OK, you don’t need to uninstall it, you just need to get Python 3.0+ running. Luckily this process is super easy with Ubuntu:

-   Step one: Open up the terminal by typing: ctr + alt + t
    
-   Step two: sudo apt-get update
    
-   Step three: sudo apt-get install python 3.7.3
    

The word sudo is abbreviation for “super user do” and it allows programs to be executed as a super user, aka the root user. The apt command means Advanced Package Tool, which is a package manager for Debian based operating systems like Ubuntu. The apt-get command is the APT package handling utility.

  
A short term alternative is to use an online python interpreter. Here’s some of the following:

-   Online GDB: [https://www.onlinegdb.com/online_python_interpreter](https://www.onlinegdb.com/online_python_interpreter)
    
-   Repl.it: [https://repl.it/languages/python3](https://repl.it/languages/python3)
    
-   Another online python interpreter: [http://mathcs.holycross.edu/~kwalsh/python](http://mathcs.holycross.edu/~kwalsh/python)

 ## A Quick Tutorial to Learning PyCharm
   
There are many choices of integrated development environments (IDEs) in python that you can choose from such as sublime, IDLE, Vim, Wing, Atom, Spyder, and PyCharm. There’s like way too many for me to keep track of so you can always check out Wikipedia: [https://wiki.python.org/moin/IntegratedDevelopmentEnvironments](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments)

If you have python installed, an editor you’re comfortable with, and ran the standard _Hello World_ program then you can jump to  _The_ _One Day_ _Python Bootcamp_  section in this chapter. If you don’t already have an editor or IDE then I’ll recommend PyCharm which has the largest mindshare in the python community.

Before you download and run PyCharm you need to have the python interpreter installed. There’s three flavors to PyCharm which are the community, education, and professional editions. The community edition is open source and compared to the commercial version (professional), it comes equipped with less features. However, when you’re starting out programming the community edition will suffice. Below are the instructions on the various operating systems:

-   **Windows:**
    
    -   Download the PyCharm installer, run the executable file, and follow the installer steps. Here’s the instructions on the PyCharm website: [https://www.jetbrains.com/help/pycharm/installation-guide.html?section=Windows](https://www.jetbrains.com/help/pycharm/installation-guide.html?section=Windows)
        
-   **MacOs:** Download the PyCharm disk image and mount and drag the image to the Applications folder: [https://www.jetbrains.com/help/pycharm/installation-guide.html?section=macOS](https://www.jetbrains.com/help/pycharm/installation-guide.html?section=macOS)
    
-   **Linux**: If you have Ubuntu 16.04 you can install PyCharm through the command line using the snappy package manager. $ sudo snap apt-get install pycharm-community
    

## Hello World With PyCharm

Once you’ve installed PyCharm the next step is to run the proverbial _Hello World_ program. Here’s the step-by-step procedure on how to do this.

### Create a Brand Spanking New Project

Create a new project by doing the following: _File → New Project_

A project is an organizational unit in PyCharm. Name the project _SampleProjects;_ here’s a screenshot of what the setup should look like thus far:

![create a sample project](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_01/Create_SampleProjects.jpg)


Next, select the python interpreter that you want to use. Click the arrow that’s next to _Project Interpreter:Existing Interpreter,_ and then _s_elect a python 3.6  or  up. Below is an example of how my setup looks:

![adding interpreter](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/images/ch_1/adding_interpreter.jpg)

Once the python interpreter is selected click the create button to create your project. Here’s a screenshot of the setup:

![adding interpreter](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_01/adding_interpreter.jpg)

### Create a fresh python file

At the main menu on PyCharm, or the portion where you see the various menus such as File, Edit, and View, do the following: **File → New File → python file.**

![create a fresh python file](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_01/create_a_fresh_python_file.jpg)

A text box should appear which looks like the following:

![a new python file](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_01/new_python_file.jpg)

Enter in the name _HelloWorld_ and select the OK button. Once done here’s how your project setup should look:

![hello world in pycharm](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_01/helloworld.jpg)

The blank white space is known as the editor. That’s where you’ll spend most of your time hacking away. The left hand side is known as the project manager, that’s where you can see the organization of files in a project.

### Add code and run the file

Copy the following code into the editor:

    print('Hello World!!!')

To run the file click the following on the main menu: run → run

A dialog box should appear which looks like the following:

![run helloworld](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/media/images/ch_01/run_helloworld.jpg)

Select the _HelloWorld_ program. Once the program has executed you should see the text:  _Hello World!!!_

If all went well then congrats, you’ve ran your first python program. Now, there’s already a plethora of free curated information about PyCharm online. Here’s a couple of places to whet your appetite:

-   Quick Start Guide: [https://www.jetbrains.com/help/pycharm/quick-start-guide.html](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)
    
-   PyCharm blog: [https://blog.jetbrains.com/pycharm](https://blog.jetbrains.com/pycharm)
    
-   Learn keyboard shortcuts for editing, navigating, refactoring, and debugging: [https://www.jetbrains.com/help/pycharm/mastering-keyboard-shortcuts.html](https://www.jetbrains.com/help/pycharm/mastering-keyboard-shortcuts.html)
# The One Day Python Boot camp

You can learn the gist of python in a day, I have no doubt about that. It will be a somewhat superficial level, but it’s a start nonetheless that you can build on top of overtime. If you want to gain a deeper understanding of the basics of python then I’ll wholeheartedly recommend the best book for learning python basics which is [Become a Python Developer](https://www.amazon.com/Become-Python-Developer-Wrestle-Defeat-ebook/dp/B07KX8RT4V).

It’s written by the amazing author Doug Purcell... oh shoot, my cover is blown.

## Variables

A variable in python is similar to a variable in mathematics. It’s something that has a changeable state. Examples of variables in python are shown below:

    a = 10
    
    b = 1.598
    
    c = .1987
    
    d = 100.579


### Printing output

The above code snippet simply stores the variables in the computer’s memory. This means that the data is there but you as the user can’t see it. In order to view the data you need to use the print function to display the output as shown below:

print(a)

print(b)

print(c)

print(d)

### Swapping variables

A useful tip to know in python is that to swap variables you can do that in a single statement.

    x = 5
    
    y = 10
    
    z = 30
    
    x, y, z = z, x, y
    
    print(x)
    
    print(y)
    
    print(z)

  
The output will be:

30	

5

10

### Variable Naming Tips

For details on how to properly name variables in python refer to the python enhancement proposals also known as _PEP 8_.

Here are some of the highlights of PEP 8:

-   Variable names can have letters, numbers, and underscores.
    
-   Can't use a reserved word like print.
    
-   Be as descriptive as possible with your variable names. This reduces ambiguity and helps make your code more maintainable when other developers follow in after you.
    
-   Python IS case sensitive so apple is not the same as Apple.
    
-   Put constants, or variables that value is fixed in all CAPS. I.e, DAYS_OF_WEEK = 7
    

For a more comprehensive overview refer to PEP 8: [https://www.python.org/dev/peps/pep-0008](https://www.python.org/dev/peps/pep-0008)

## Python Math Operators
    

The word computation has computer in it, which gives a hint to one of the uses of computers. Python like many sophisticated programming languages can be used as a _souped up calculator_. All of the standard features that’s available on scientific computers can easily be emulated with the help of built in operations and modules in python. Let’s look at some of the math operators available in python: +, -, *, **, /, //, %

Most of these symbols you’re probably already familiar with. Let’s dig into some code to better understand this:

    print(10 + 10)
    
    print(50 - 10)
    
    print(10 * 10)
    
    print(20 ** 2)
    
    print(9 / 5)
    
    print(8 // 3)
    
    print(11 % 5)
    
    print(1e10)

Here’s the output:

20

40

100

400

1.8

2

1

10000000000.0

The +, -, *, and / symbols behave as we expect. The asterisk means multiplication and forward slash means division. The double star, (**) means raise to the power. So, in this case 20 ** 2 means 20^2 or 400. The double forward slash (//) indicates the floor operator in mathematics. This means to divide the dividend by the divisor, and ignore the remainder. 

In this case this means 8 divided by 3, which is 2.66666666667, but the floor operator ignores all of the stuff following the decimal point (mantissa), so the answer is 2. The % sign indicates modulus, so you divide the dividend by the divisor like you would with regular division except you take the remainder. Therefore you do 11 divided by 5 which is 2, and then take the remainder which is 1.

### Adding additional functionality into your programs

If we use just the builtin math operators then we’re severely limited in what we can do for our mathematical calculations. Luckily there’s the math module which you can checkout here: [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

It includes mathematical properties like logarithms and trigonometry. To use these functions in your program you need to use the import statement. Below is a quick example:

    import math
    
    print(math.log(1000000, 2))
    
    print(math.sqrt(9))
    
    print(math.cos(100) + math.sin(90) + math.tan(90))
    
    print(math.pi**2 * math.e)

<pre>
19.931568569324174

3.0

-0.23888487632000044

26.828366297560617
</pre>

## Strings
    
If you have ever sent a SMS text, used Facebook chat, or sent an email then you have used strings. A **string** is a sequence of characters wrapped in quotes; in python it could be single, double, or triple quotes. The single or double quotes can be used interchangeably. 

The triple quotes are typically used as doctrings, or comments inside methods, functions, or classes. They’re typically used when you need to include text that expands multiple lines as they can handle line breaks nicely. The best way to understand the difference between the various string types is to create a simple python program and experiment with them. Below is a quick overview of strings in python:


    city = 'Los Angeles' # indexing: python is a zero based indexed language
    print(city[0])  # L
    print(city[3])  # empty space is a string!
    print(city[4])  # capital A
    print(city[-1]) # negative indices are permitted # len() function: gets the length of the string
    print(len(city))    # 11
    print(city[len(city)-1]) # s 
    print('john ' + 'doe ' + 'public') # john doe public # slicing: retrieves ranges of a string
    print(city[0:3])   # Los
    print(city[4:11])  # Angeles
    print(city[::])    # Los Angeles
    print(city[::2])   # LsAgls
    print(city[::-1])  # selegnA soL


## Boolean Algebra
    

This is a branch of mathematics that was invented by English mathematician George Boole back in 1847. Even though it’s over a century old its impact still permeates. It has been fundamental in the development of digital electronics, and is available in all modern day programming languages. Therefore, learning Boolean algebra for python means that you can apply that set of logic to a wide array of languages like Java, C++, Haskell, Erlang, or R.

In python what we need to worry about are the values of `True` or `False`, which can also be denoted by 1 or 0 respectively. The main operations that we’ll discuss are “and” (conjunction), “or”  (disjunction), as well as “negation.” There’s also the lesser used “xor”  operator:


<pre>
Below is a sample of how the truth table looks:

x	y	x and y  	x or y		x     not x
0	0	0	   		0			0     	1
1	0	0	   		1			1     	0
0	1	0	   		1
1	1	1	   		1
</pre>

  

Remember, 0 maps to False, and 1 maps to True. Here’s a shortcut to remembering this: _and_ is always False or less you have two True operands, while _o__r_ is always True or less you have two False  operands. If you’re confused about this then no worries, just commit the above table to memory. You’ll need to remember it in order to to understand conditional logic.


    is_the_sky_blue = True
    
    do_cats_bark = False
    
    print(is_the_sky_blue) # True
    
    print(do_cats_bark) # False

  
Remember, 0 and 1 could be used for False or True. Therefore you could use them interchangeably if you desire, even though True or False are more common.

### The 'and' truth table

  
The 'and' operator evaluates to False in all situations EXCEPT when both operands are `False`.


    print(True and True) # True
    
    print(True and False) # False
    
    print(False and False) # False
    
    print(False and True) # False

  

### The ‘or’ truth table

Or evaluates to True with at least one True  operand.

    print(True or True) # True
    
    print(True or False) # True
    
    print(False or False) # False
    
    print(False or True) # True

 

### The ‘xor’ truth table

Xor is a little tricky. It evaluates to True when the two operands are different.

    print(True ^ True) # False
    
    print(True ^ False) # True
    
    print(False ^ True) # True
    
    print(False ^ False) # False

 

## Control Flow in Python

  
Once you understand Boolean algebra you can apply that newfound knowledge to control flow, or the order in which statements are executed. Python uses the if, else, and elif statements for this.

### if/else statement

Here’s an example of an if/else statement:

  

    x, y, z = 5, 10, 15
    
    if x < y and z > y:
    
        print(x)
    
    else:
    
        print(y)

The if keyword is a reserved keyword in python, and the expression most be terminated by a colon. If the first expression is True then the statements inside the body are executed, if it’s False then the branch under the else statement is executed.

### elif statement

Below is an example of the elif statement in python:

    from random import randint
    # picks a random number in range 1...100
    grade = randint(1, 100)
    if grade >= 90 <= 100:
        print('A')
    elif grade >= 80 <= 89:
        print('B')
    elif grade >= 70 <= 79:
        print('C')
    elif grade >= 60 <= 69:
        print('D')
    else:
        print('F!')

### Ternary Statement

This is a special type of operator that evaluates something based on a condition being True or False. The best way to understand it is to take a look at a simple code snippet:
  

    mood = True
    
    state = 'nice' if mood else 'not so nice'
    
    print('state = {}'.format(state))

  
The following prints nice because if mood evaluates to True.

## Comments

At this point you may have saw the hash symbol (#) followed by text. This is known as a _comment_ in python and this portion of the code is ignored by the interpreter. However, it’s still very useful to include in your programs as it helps other programmers that may be messing around in your code to understand the logic.

    # This is a comment
    # This is a comment and will be ignored by the interpreter
    # I think you get the memo!

## Data structures in python 3.7.3

  
There are four builtin data structures in python which are lists, tuples, dictionaries, and sets. Here’s a quick rundown of each one:

### lists are mutable collections of objects


Below is a demo of some of the features of a list in python:

    evens = [0, 2, 4, 6, 8, 10]

  
### reverses the list

    >>> evens.reverse()

[10, 8, 6, 4, 2, 0]


### adds an object to the list

    >>> evens.append(100)

[10, 8, 6, 4, 2, 0, 100]


### merges another list with the list

    >>> evens.extend([1, 3, 5, 7, 9])

[10, 8, 6, 4, 2, 0, 100, 1, 3, 5, 7, 9]

 
### pops an item from the list

    >>> evens.pop()

_9_


## iterating over a list

    for x in evens:
    
        print(x)

...

10

8

6

4

2

0

100

1

3

5

7

### Tuples

These are an immutable sequence. Unlike lists once you create a tuple they cannot be modified, and trying to do so will cause an error.

    nums = (1, 3, 5, 7)
    
    >>> print(nums)

...

(1, 3, 5, 7)

### Dictionaries

These are key/value pairs or associative arrays in some languages.

    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for key, value in vowels.items():
    
        print(key, value)

  
_..._

_a 0_

_e 0_

_i 0_

_o 0_

_u 0_

### Sets

Stores unique items.

    letters = {'a', 'a', 'a', 'b', 'b', 'b'}
    
    >>> print(sorted(letters))

...

['a', 'b']

  
  
## Iteration in Python

  
_Iteration_ is the process in which computers do repetitive tasks. Humans despise repetition while computers are amazing at it. Humans can do repetitive tasks like summing all of the numbers from 1-100 manually (assuming no mathematical formulas are used), but these tasks are tedious and error prone. Computers can do number crunching like this in very quick times, like in a couple of freaking nanoseconds. The two main ways to do iteration in python is by using either the while or for loops.

### WHILE LOOP

A while loop states that while a condition is True to execute the statements in the body.

    # sets while loop starting at
    i = 0
    # condition
    while i < 10:
        print('i =  {}'.format(i, end=' ')) # print value of i, end='' means print on same line
        i += 1  # increment i

When ran the above code prints 0 … 9.

     # Sum numbers from 1...1000 in nanoseconds
    i, sum = 0, 0
    while i < 1000:
        i += 1
        sum += i
    print('The summation of 1...1000 = {}'.format(sum)) 
<pre>

>>> The summation of 1...1000 = 500500
</pre>

### for loop

This is another way to iterate in python. It can be used with the range function to iterate over a sequence of numbers or it can be used standalone to iterate over data structures like lists or sets. Below is a simple example of a for loop in python:

    for x in range(10):
        print(x, end=' ')

The above prints the numbers 0 … 9 on the same line separated by a space.

### Fibonacci numbers

The following prints the 12th Fibonacci number:

    x, y = 0, 1
    
    for z in range(10):
    
        next = x + y
    
        x, y = y, next
    
    print('12th fib number = {}'.format(next))

  <pre>
>>> print('12th fib number = {}'.format(next))

12th fib number = 89
</pre>

## Creating functions in python
    

A function is a set of inputs that map to a set of outputs. You can create your own functions in python by using the def  keyword.

    def scale_number(num, amount):
    
        return num * amount

<pre>
>>> print(scale_number(10, 5))
</pre>
...
50

### Keyword arguments


    def area_triangle(height=11, width=7.5):
    
        return 1/2 * (height * width)

<pre>
>>> print(area_triangle())
</pre>
...

41.25
<pre>
>>> print(area_triangle(height=20, width=100))
</pre>
...
1000.0

### Accepting an arbitrary number of input

You can do this by appending an asterisk in front of the variable.

    def multiply(*args, y=1):
    
        for x in range(len(args)):
    
            y *= args[x]
    
        return y

<pre>
>>> print('multiply=', multiply(1, 2, 3, 4))
...
multiply= 24
</pre>

### Reading in an arbitrary number of keyword arguments

You can accomplish this by sticking two asterisks in front of the variable name.

    def key_value(**kwargs):
    
        for key, value in kwargs.items():
    
            print('{} {}'.format(key, value))

<pre>
>>> key_value(a=5, b=10, c=15)

a 5

b 10

c 15
</pre>

 ## Classes and Objects
    
Object oriented programming is a style of programming that involves the heavy use of classes and objects. Classes are typically described as blueprints, while objects are described as the templates that’s created from the classes. Below is a simple example of how to create a class in python:

    class Point:
        """Simple class in python. This is an example
        of a docstring, or a string that's used like a
        comment to document a segment of code."""
    
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
        def get_x(self):
            return self.x
    
        def get_y(self):
            return self.y
    
        def set_x(self, new_x):
            self.x = new_x
    
        def set_y(self, new_y):
            self.y = new_y
    
        def get_point(self):
            return self.x, self.y

<pre>
p = Point(5, 10)

print()

print(p.get_point())

p.set_x(100)

p.set_y(200)

print(p.get_point())

...

(5, 10)

(100, 200)
</pre>

## Exception handling
    
There’s at least two distinguishable types of errors: syntax and run time. Exceptions occur when the program is being ran and you can handle them by using try/except statements. Here’s a demo of a simple try/except statement in python:

    def divide(num, den):
        try:
            x = num / den
            print('{} / {} = {}'.format(num, den, num / den))
        except ZeroDivisionError:
            print("can't divide by zero.")

<pre>
>>> divide(10, 5)

>>> divide(0, 10)

>>> divide(10, 0)

10 / 5 = 2.0

0 / 10 = 0.0

can't divide by zero.
</pre>

The statements that wants to be executed are located within the try block. If an error occurs in the try block then the except block is executed. `ZeroDivisionError` is one of the many builtin exceptions in python3.

Below is another example of a try/except statement in python:

    def import_test():
        try:
            import math
            import operating
            import sys
            print(math.pi)
            print(sys.version_info)
        except ImportError:
            print("Couldn't import something")

<pre>
>>> import_test()
...

Couldn't import something
</pre>

The reason for this is because operating is not a builtin module in python and therefore an error was triggered while in the try block. You can also use the raise statement to force an exception to occur. Below is an example of this in action:

    try:
    
        a = input('Enter an integer ')
    
        raise Exception("Something strange happened")
    
    except ValueError:
    
        print("An exception happened.")

<pre>
>>> Enter an integer 10

Traceback (most recent call last):

File "<stdin>", line 3, in <module>

Exception: Something strange happened
</pre>

Below is an example of a try/except/finally statement:

    def divide(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("Can't divide by 0")
        else:
            print(result)
        finally:
            print('This is in the finally statement')

<pre>
>>> divide(10, 2)
...

5.0

This is in the finally statement
</pre>

The finally clause is executed before leaving the try statement. It's always executed, no exceptions (no pun).


## The best way to support this project is to [purchase a digital copy](https://www.amazon.com/Code-Cool-Stuff-Python-Purcell-ebook/dp/B081XJMNRB) on Amazon and leave a review. 

