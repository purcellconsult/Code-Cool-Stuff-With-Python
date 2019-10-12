
## Chapter II: Crafting Small Scripts, Converters, and Practical Tools in Python

In this chapter we’ll learn how to build some simple yet cool python scripts that can be ran through the command line. We will learn how to make scripts that asks the user a series of questions and then process the input to do various tasks such as converting the temperature to different units, computing auto loans, and handy translators.

# **Project: Your Biography**

Let’s write a program that creates a biography for us. One way to do this is to ask a series of probing questions. Some questions that you may want to answer are things like:

-   first name
    
-   last name
    
-   nationally
    
-   birth place
    
-   age
    
-   height:
    
    -   feet
        
    -   inches
        
-   weight (in pounds)
    
-   favorite food
    
-   favorite city
    
We won’t use this for a dating app, we just want to use this exercise as a means to explore some of the possibilities of python ;). You can add on any additional questions you want.

## Script Hints

In order to create this script follow the steps:

1) In PyCharm go to the directory where you’ll place all of your programs. Right-click on the directory and select: New → Python File. Enter the name of the python file as _bio.py._

2) In the PyCharm editor add a function named questions. Inside the function is where all of the statements for your logic to go inside. You can use the input function to read in text form the terminal. If you need to read in an int or a float then you can pass the input function into the int or float functions. For example, the following will read in a float from the terminal:

    weight = float(input('Enter weight in lbs: '))

To view a list of the builtin functions in python check out this 				url: [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)

3) Include the following code snippet after the questions function:

    if __name__ == '__main__':
            # this is where your program starts
            questions()

This lets the python interpreter know where to start at. In every python file there’s a __name__ variable that’s set equal to __main__. Therefore, if your file explicitly includes this then it will tell the python interpreter to start here. Below is a template to how your python file will look:


    def questions():
        """This is the part of the program that prompts the user"""
        
    if __name__ == '__main__':
        # this is the entry point to the program
        questions()

One of the tricky things that you may want to look out for is how to read in multiple user input in a single statement. For example, reading in a single int or string is easy because you can do something like this:

<pre>

>>> temperature = int(input('Temp today:'))

...

Temp today:75

>>> color = input('The color:')
...

The color:blue
</pre>

However, what if you want the user to enter in two inputs so that you can store the data in feet and inches? One way to do that is to use the builtin string method called split. This will split the text around a certain character like a comma.

## Solution

Below is a sample solution. Your script may have more or less questions, it really depends on how you want to create it.
  

    def questions():
        """This is the part of the program that prompts the user
        for a bunch of questions."""
        first_name = input('Enter your first name: ').capitalize()
        last_name = input('Enter your last name: ').capitalize()
        nationality = input('Enter your nationality: ').capitalize()
        age = int(input('Enter your age: '))
        height = input('Enter feet and inches separated by commas: ')
        user_input = height.split(',')
        heights = user_input[0], user_input[1]
        weight = float(input('Enter weight in lbs: '))
        favorite_food = input('Enter your favorite food: ').capitalize()
        favorite_city = input('Enter in your favorite city: ').capitalize()
        print()
    
        print('First name: {}'.format(first_name))
        print('Last name: {}'.format(last_name))
        print('Nationality: {}'.format(nationality))
        print('Age: {}'.format(age))
        print('Height: {} ft {} in'.format(user_input[0], user_input[1]))
        print('Weight: {}'.format(weight))
        print('Favorite food: {}'.format(favorite_food))
        print('Favorite city: {}'.format(favorite_city))
    
    if __name__ == '__main__':
        # this is where your program starts
        questions()

<pre>

print('First name: {}'.format(first_name))

print('Last name: {}'.format(last_name))

print('Nationality: {}'.format(nationality))

print('Age: {}'.format(age))

print('Height: {} ft {} in'.format(user_input[0], user_input[1]))

print('Weight: {}'.format(weight))

print('Favorite food: {}'.format(favorite_food))

print('Favorite city: {}'.format(favorite_city))
</pre>


    if __name__ == '__main__':
    
    # this is where your program starts
    
        questions()

  <pre>
 
Sample input:

Enter your first name: danny

Enter your last name: hill

Enter your nationality: american

Enter your age: 47

Enter feet and inches separated by commas: 5, 5

Enter weight in lbs: 200

Enter your favorite food: pizza

Enter in your favorite city: philadelphia

Sample output:

First name: Danny

Last name: Hill

Nationality: American

Age: 47

Height: 5 ft 5 in

Weight: 200.0

Favorite food: Pizza

Favorite city: Philadelphia
</pre>

You can run the file by opening up the terminal or command prompt and typing in the following:

$ python bio.py

# **Project: Temperature Converter**

  
The world is not singular. There’s many different types to something and this can vary from country to even region. Let’s focus our attention on converters; there’s many of these online and Google has a massive amount that you can trigger by just entering specific queries into the search box: [https://support.google.com/websearch/answer/3284611?hl=en](https://support.google.com/websearch/answer/3284611?hl=en)

The advantage that you have as a python programmer is that you can also add new features, create updates, and write a new script for something you can’t find online. That’s the beauty about knowing how to code, _you now have a new world of possibilities_.

There’s three commonly used scales for measuring temperature: Celsius (°C), Fahrenheit (°F), and Kelvin (K). Celsius is used by all the countries except United States, Bahamas, Belize, Cayman Islands, and Liberia. Americans that travel abroad will probably have to go through a phase in which they have to adjust to reading temperature in Celsius… I know I did! 

Kelvin is the unit of measurement used in the International System of Units (SI). The Kelvin scale is also heavily used in science and technology. Let’s create a script that can convert all of the temperature units to each other and back. In order to do this we must need to know the mathematical formulas. Luckily, they’re simple:

-   F -> C = (F - 32) x 5/9
    
-   F -> K = (F - 32)/1.8 + 273.15
    
-   C -> F = (C x 9/5) + 32
    
-   C -> K = C + 273.15
    
-   K -> F = (K - 273.15) x 9/5 + 32
    
-   K -> C = K - 273.15
    

With the above knowledge you can proceed to write your temperature conversion script. Sometimes the first step is the most difficult one to take. Here’s some tips to get started.

## Script Hints
    

We can create the function names and just include the pass statement so that the code doesn’t do nothing yet. Here’s the name of the functions:

`fahrenheit_to_celsius`: Converts the user input from Fahrenheit to Celsius.

`fahrenheit_to_kelvin`: Converts the user input from Fahrenheit to Kelvin.

`celsius_to_fahrenheit`: Converts the user input from Celsius to Fahrenheit.

`celsius_to_kelvin`: Converts the user input from Celsius to Kelvin.

`kelvin_to_fahrenheit`: Converts the user input from Kelvin to Fahrenheit.

`kelvin_to_celsius`: Converts the user input from Kelvin to Celsius.

`fahrenheit_to_celsius`: Converts the user input from Fahrenheit to Celsius.
  
Here’s a template of how the script looks:

    def fahrenheit_to_celsius():
        pass
    def fahrenheit_to_kelvin():
        pass
    def celsius_to_fahrenheit():
        pass
    def celsius_to_kelvin():
        pass
    def kelvin_to_fahrenheit():
        pass
    def kelvin_to_celsius():
        pass
    
    if __name__ == '__main__':
        pass 


## Solution
    

Below is one solution:

    def fahrenheit_to_celsius():
        temp_in_fahren = float(input('Enter the temperature in Fahrenheit '))
        celsius = (temp_in_fahren - 32) * 5/9
        celsius = round(celsius, 4)
        print(celsius, '°C')
    def fahrenheit_to_kelvin():
        temp_in_fahren = float(input('Enter the temperature in Kelvin '))
        kelvin = (temp_in_fahren - 32) / 1.8 + 273.15
        print(kelvin, 'K')
    def celsius_to_fahrenheit():
        temp_in_celsius = float(input('Enter the temperature in Celsius '))
        celsius_to_fahren = (temp_in_celsius * 9/5) + 32
        print(celsius_to_fahren, '°F')
    def celsius_to_kelvin():
        temp_in_cel = float(input('Enter the temperature in Celsius '))
        celsius_to_kel = (temp_in_cel + 273.15)
        print(celsius_to_kel, 'K')
    def kelvin_to_fahrenheit():
        temp_in_kelvin = float(input('Enter the temperature in Kelvin '))
        kelvin_to_fahren = (temp_in_kelvin - 273.15) * 9/5 + 32
        kelvin_to_fahren = round(kelvin_to_fahren, 3)
        print(kelvin_to_fahren, '°F')
    def kelvin_to_celsius():
        temp_in_kelvin = float(input('Enter the temperature in Kelvin '))
        kelvin_to_cel = temp_in_kelvin - 273.15
        kelvin_to_cel = round(kelvin_to_cel, 3)
        print(kelvin_to_cel, '°C')
    
    if __name__ == '__main__':
        message = input("""Select one of the following options:
        
    Type 'fc' to convert from Fahrenheit to Celsius. 
    Type 'fk' to convert from Fahrenheit to Kelvin.
    Type 'cf' to convert from Celsius to Fahrenheit.
    Type 'ck' to convert from Celsius to Kelvin.
    Type 'kf' to convert from Kelvin to Fahrenheit.
    Type 'kc' to convert from Kelvin to Celsius.
        
    Enter input here: 
        """)
    
        # casefold is for case-insensitive comparisons
    
        message = message.casefold()
        if message == 'fc':
            fahrenheit_to_celsius()
        elif message == 'fk':
            fahrenheit_to_kelvin()
        elif message == 'cf':
            celsius_to_fahrenheit()
        elif message == 'ck':
            celsius_to_kelvin()
        elif message == 'kf':
            kelvin_to_fahrenheit()
        elif message == 'kc':
            kelvin_to_celsius()
        else:
            print('Not a valid option pal!')

You can download the script from GitHub: [https://github.com/purcellconsult/Build-Cool-Stuff-With-Python/blob/master/temp_converter.py](https://github.com/purcellconsult/Build-Cool-Stuff-With-Python/blob/master/temp_converter.py)

When the program runs it should display a message to show the user how to use the script. We’ve created a command line script so therefore some instructions on how to use it is a good start. To do this simply create a message in the form of a string and display it. 

We could of used single print statements, but I’ve opted to use a string that’s wrapped in triple quotes for this as this style of strings will make it so that we don’t have to worry about escaping characters like apostrophes. I’m referring to this segment of the code:

    if __name__ == '__main__':
        message = input("""Select one of the following options:
        
    Type 'fc' to convert from Fahrenheit to Celsius. 
    Type 'fk' to convert from Fahrenheit to Kelvin.
    Type 'cf' to convert from Celsius to Fahrenheit.
    Type 'ck' to convert from Celsius to Kelvin.
    Type 'kf' to convert from Kelvin to Fahrenheit.
    Type 'kc' to convert from Kelvin to Celsius.
        
    Enter input here: 
        """)

When writing command line scripts we always want to make it easy for the user to enter in text. For i.e, if the user entered FC then this will not match the condition if message == ‘fc’ and therefore the program will evaluate to False. However, with the assistance of the casefold method all of these cases are evaluated so it doesn’t matter what case the user enters.

# **Project: Auto loan Calculator**

Cars are incredible mechanical inventions. Something they can be driven for countless of miles and still function properly is quite amazing. Like many quality things in life it costs money so in this project we’re going to code a useful script that will help us make better purchasing decisions when deciding on a new car. The script will have two parts: one, how many months it will take to pay off the loan and two, what’s the total interest paid accumulated over that period of time. Here’s some formulas to get started:

    A = P x (1 + r) ^N / (1 + r)^N – 1

Formula for calculating the accrued interest:

    A = P(1 + rt)

The first formula looks tricky but it’s simple once you know what all of the variables represent. Here’s a quick overview:

-   P = Principal or the amount owned on a loan.
    
-   A = Total accrued amount (principal + interest).
    
-   r = Rate of interest per year as a decimal, or interest rate / 100.
    
-   N = Number of months in the loan period.
    

If you were to go into an auto company’s finance department then this is the same formula that they’ll use to determine your monthly car payments. In the second formula, p(1 + rt), _t_ represents the number of months on the loan like _n_, it’s just that by using _r_ and _n_ together (rn) that it would be more difficult to read.

 ## Script Hints
    
Create a function that calculates the monthly cost. You can break down the formula in order to minimize the chances of making a mistake. This reduces syntax errors and makes debugging potential arithmetic errors more straightforward.

## Solution
    

Below is one solution to the problem:

    def monthly_cost():
        print('Gotta couple of questions for you...')
        p = float(input('Enter loan amount '))
        r = float(input('Enter interest rate (%)'))
        n = int(input('Enter loan period (in months)'))
        # convert r to a decimal and divide by interest per year
        r = (r / 100) / 12
        # breaks formula down into 3 parts to reduce error
        # numerator
        top = r * (1 + r)**n
        # denominator
        bottom = ((1 + r)**n) - 1
        # putting it all together
        a = round(p * (top / bottom))
        # use simple interest formula
        # I = Prt
        # In this case, I = Prn
        total_interest = round(p * r * n, 3)
        print(f'Monthly costs = ${a}. Total interest = ${total_interest} ')
    if __name__ == '__main__':
        monthly_cost()

Here’s a quick breakdown of what’s happening:

1) The user input is requested and stored in the variables of p, n, and r.

2) Once the user input is collected, the mathematics is done on separate statements to minimize errors. For example, the value of r is calculated on one line, and instead of trying to translate the mathematical formula to python code on a single line, the numerator and denominator is calculated in separate statements and then combined in this statement:

    a = round(p * (top / bottom))

If you have lot’s of experience in python then doing everything in a single statement may be trivial. However, if you’re new to the language then the important thing is to get the script to work as you can refactor (restructure) the code later.

The auto loan calculator script on GitHub: [https://github.com/purcellconsult/Build-Cool-Stuff-With-Python/blob/master/auto_loan_calculator.py](https://github.com/purcellconsult/Build-Cool-Stuff-With-Python/blob/master/auto_loan_calculator.py)

# **Project: Mortgage Calculator**

  
Getting a house is the American dream, but to obtain a dream does cost. In this exercise we’re going to create a script that calculates the monthly payment that someone owes on a house. When one takes out a loan for a house this is known as a mortgage.

Mortgage calculators can get pretty complex, so in this exercise we’re going to _stupify_ the process so that we just calculate the monthly payments and total mortgage that one would owe contingent on some variables. These variables are:

-   **Mortgage period**: How long the mortgage will last in years.
    
-   **Principal**: The amount of money owed on the loan.
    
-   **Interest rate**: The percentage of principal charged by the lender for the use of their money.
    

## Script Hints

After digging around here’s the formula that you can use to calculate the monthly payments on a house:

-   p x r (1 + r) ^ N / (1 + r) ^ N - 1
    

Put together a python script that prompts the user for their name, principal, interest rate, and then outputs the monthly payment and the total interest a homeowner would pay.

## Solution:
    
    def mortgage():
        name = input('Enter your name ').capitalize()
        print(f"Time to calculate your mortgage payments {name}... ")
        principal = float(input('Enter in your principal '))
        interest_rate = float(input('Enter interest rate '))
        r = (interest_rate / 100) / 12
        n = int(input('Enter mortgage period (years) '))
        # get total number of months
        n = n * 12
        numerator = r * (1 + r) ** n
        deno = (1 + r) ** n - 1
        monthly_payment = principal * (numerator / deno)
        monthly_payment = round(monthly_payment)
        total_mortgage = monthly_payment * 30 * 12
        print(f'Monthly payment: ${monthly_payment}, total mortgage = ${total_mortgage}')
    
    if __name__ == '__main__':
        mortgage()

This script is very similar to the auto loan script except that the formula varies:

-   The variables of principal, interest rate, r, and n are prompted from the user.
    
-   The numerator and denominator of the function is calculated separately and then combined together at the end to emulate the formula: p x r (1 + r) ^ N / (1 + r) ^ N – 1
    
-   Once the total monthly payment is calculated, the total mortgage is computed by taking the monthly payment and multiplying it by 30 and 12. The reason for this is because there’s roughly 30 days in a month, and 12 months in a year.
    
Language translation is a complicated art. Even online translation tools created by teams of talented engineers at behemoth tech companies miss structural and linguistic elements in their translations. Therefore, to serve as a learning project we’re going to simplify the process and focus on a narrow domain of words and phases to transliterate.

Not only is this a good exercise to gain more familiarity with data structures, strings, and conditional statements, it’s also a good exercise for gaining more comfort with loops in python. So, to simplify the process create a python script that focuses on translating foods and general phrases.

## Script Hints

Here’s an outline of the script:
 

     def food():
        pass
    
    def general_phrases():
        pass
    
    if __name__ == '__main__':
    
        print('Bienvenidos! What phases would you like to translate?')
        print('1: Common foods ')
        print('2: General phases')
        your_choice = int(input("Enter your choice: '1' or '2'"))
        if your_choice == 1:
            food()
        elif your_choice == 2:
            general_phrases()
        else:
            print('Not a possible choice!')

  
The list of food items and general phrases that you want to translate is up to you. I would suggest using a dictionary to store the Spanish-to-English and vice-versa mappings, as this data structure is perfectly suited for this type of task.

Another thing that you may be pondering is how to create the script so that a user could easily use it? The strategy I took was that once the program runs it asks the user a question and then executes the appropriate function contingent on their feedback. Also, you may want to think about a way to normalize the text. 

For example, assume that the user wants to translate Barbacoa into English. What happens if they entered a variant spelling such as _BarBacoa_ or _barbacoa_? We need a way to modify the input so that any variant of the spelling is processed. We can accomplish this by using a builtin string method such as `capitalize` so that the user input is in the same case as the text stored in the dictionaries.

## Solution
    

The script contains two functions which are food and `general_phrases`. The food function contains popular Mexican food items written in Spanish, and if the user types that item into the shell then it’s respective English term will be printed. The `general_phrases` function contains a list of common conversation phrases which are translated into English when it’s typed into the shell. Let’s first breakdown the food function as shown below:
  

    def food():
        """Names for some popular mexican food items.
        Translate spanish food names to english.
        """
        print('\n')
        spanish_to_english = {
            'Birria': 'Spicy stew made with goat or mutton. ',
            'Quesadilla con carne': 'season steak strips. ',
            'Barbacoa': 'Slow cooked meat in soup. Beef, goat, or sheep.',
            'Burrito Banado': 'Wet Burrito.',
            'Huevos rancheros': '"Rancher\'s eggs." Corn tortillas, fried eggs, topped with warm salsa.',
            'Coctel de camarones': 'Shrimp cocktail served cold with tomato, onion, cucumber, and cilantro. ',
            'Huevos a la mexicana': 'Eggs, tomato, onion, and serrano chile. A classic.',
            'Huevo con Chorizo': 'Eggs and chorizo sausage.',
            'Burritos de Desayuno ': 'Breakfast burrito.',
            'Chilli con carne': 'Chili with meat.',
            'Lengua': 'Beef tongue, typically in tacos.',
            'Tripas': 'Small intestines of farm animals that\'s cleaned, boiled, and grilled. ',
            'Al pastor': 'Pork based taco based on shawarma',
            'Suadero': 'Tender slow cooked beef brisket. Typically served in tacos.',
            'Cabeza': 'Beef head/cheek meat. Served in soups or tacos.',
            'Sesos': 'Brains from either a goat or cow. Popular taco filling.'
        }
    
        print('Spanish phases available for translation:')
        for spanish, english in spanish_to_english.items():
            print(spanish)
    
        print()
        translate = input('Type in spanish phase you\'ll like to translate: ').capitalize() 
        for english, spanish in spanish_to_english.items():
            if translate == english:
                print(spanish_to_english.get(translate))
                break
        else:
            print('Word is not available for translation')

  
This code can be broken down into a couple of parts. The `spanish_to_english` dictionary contains a mapping of Mexican dishes and their explanation in English. The for loop iterates over the dictionary and then prints the Spanish words.

The user input is requested for the Mexican dish that they would like a to translate into English. A for loop is used that iterates over the dictionary and then a conditional check is utilized to see if the user input matches any of the items in the dictionary. If it is then the English explanation is printed, and if not then a default message is printed letting the user know that the word is not available for translation.

Identical logic is used for general_phrases  with the exception that the dictionary contains mappings of English to Spanish.

See the complete source code of the Spanish translator script: [https://github.com/purcellconsult/Build-Cool-Stuff-With-Python/blob/master/spanish_translator.py](https://github.com/purcellconsult/Build-Cool-Stuff-With-Python/blob/master/spanish_translator.py)

## Chapter II Recap
    
In this chapter we learned how to start building some real-world practical programs. Converters and calculators are some basic programs that you can start writing that allows you to start solving real world problems. If you’ve built a couple of these scripts then this is something that you can show your friends and family to showcase your evolving python programming prowess!

