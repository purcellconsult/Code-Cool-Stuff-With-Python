# Chapter III: How to Unlock The Power of Randomization to Create Intriguing Scripts in Python

_Coin flipping_ is the practice of throwing a coin in the air and checking which side it lands on; just think of the Batman antihero _Two-Face_. Coin flipping is an unbiased way to solve a dispute, and is a solid example of randomization. In this chapter we’ll build three scripts that relies heavily on randomization: A simple dice game, a random person generator, and a lottery simulator. 

Randomization is a phenomena that effects all humans regardless of what walk of life they’re from. Many things are randomly assigned to us such as such as our date of birth, nationally, family, height, and eye color. 

With it’s inherit nonpartisan attributes, randomization is heavily used in statistics, clinical trials, and shuffling cards. 

Randomization is a fascinating somewhat overlooked portion of life, so let’s get more familiar with it by writing some cool python programs.

# Project: A Game of Dice. Humans vs Randomization

An object that involves heavy randomization is a dice. This cubic device has a wide array of application such as tabletop games, board games, and of course gambling. A dice can easily be modeled computationally through the use of a _random_ module. Python has a built in one for this which is conveniently named _random_. We’ll create a simple yet elegant game that involved randomization called _A Game of Dice._

The user will start with a bank account of $1000 and can keep making wagers on which number the dice will roll on. If the dice falls on the number that the user guesses, then the user gets the money that they wagered, and vice-versa. The game play will continue until the user runs out of money or exits from the game. This is a truly simple game that displays the beauty and the volatile nature of randomness.

## Script Hint

Let’s breakdown the logic:

-   Who goes first? The first question is how to determine which player goes first, the human or the computer? One way is to simulate a coin flip of heads or tails. Both players are allowed to pick which side of the coin they want. If both players both pick the correct side then this process should be repeated until there’s a single winner.
    
-   How much money will each player start with? What happens when some edge cases arise like a player betting more money than they have, or enters an invalid input like a string?
    
-   What’s the minimum and maximum amount of rounds allowed?
    
-   What happens when the player has no more money to bet?
    

## Solution

There’s a couple of things to think about when you’re coding the script. For one, we need to generate a seed of numbers within the range of 1-6 that emulates the dice. We then need to figure out how many rounds we want the player to play. Here’s some code to get us started:

    from random import randint
    def game():
        print('Welcome! You\'re Playing:')
        human_bank = 1000
        while True:
            you = float(input("How much money do you want to wager? "
                            "Your bank has ${} ".format(human_bank)))

The first line simply imports the randint function from the random module. This allows us to generate the seed of numbers to mimic the effect of a dice. Next, a game function is created which holds the bulk of the logic. I’ve decided that I want to indiscriminately decide when to terminate the game-play. 

Therefore, a simple way to do this is to wrap our logic within an indefinite while loop and then include several conditional statements to control the progression of the program. 

Don’t worry about the while loop not having an exiting condition as there’s several ways in which we can address this later. The following code snippet shows the logic that’s needed to check if the player has enough money in the bank, simulates the rolling of the dice, and then asks the user for their guess:

    if you > 0 <= human_bank:
                    print("You're betting ${}".format(you))
                    dice_roll = randint(1, 6)
                    human_guess = float(input('What number you think the dice will roll on? '
                                              'Select numbers: 1-6 '))

Let’s analyze this portion:

    if you > 0 <= human_bank:

This condition ensures that the user didn’t enter in a negative number (that makes no sense) and also that the maximum amount of money that they’re wagering is all the money they got in their account; anything above that shouldn't be permissible as you can’t deduct more money than what’s in your bank account! 

Next, a random number within the range of 1-6 is generated, and then the user is asked for the amount that they’re wagering. The input is _cast_ or converted to a float which are just decimal point numbers. Most people don't bet $100.50, but I’ve included it just for those quirky individuals that do. The next step is to update the cash in the bank account contingent on the outcome as shown in the following code snippet: 

      if human_guess == dice_roll:
                        human_bank += you
                        print('Dice landed on {}'.format(dice_roll))
                        print("Congrats! You now have ${}".format(human_bank))
                    else:
                        human_bank -= you
                        print("Bummers! Dice landed on {}! Money gone...".format(dice_roll))
                        print("You have ${}".format(human_bank))
                    if human_bank == 0:
                        print("Game over! You're out of cash")
                        break

The above code snippet includes an if/else statement to check to see if the user guess right or hit a big fat 0. The last if statement checks to see if the player’s account is 0, and if it is then game over and breaks of the script. 

We also need to put in some logic to determine if the player wants to continue the game or exit. The following code snippet does this:

      play_again = input("Enter 'y' to play again or 'n' to stop" ).lower()
                    if play_again == 'y':
                        continue
                    elif play_again == 'n':
                        print("Game Over...")
                        if human_bank > 1000:
                            print("You're lucky! You won ${} ".format(human_bank - 1000))
                            break
                        elif human_bank < 1000:
                            print("Better luck next time! You loss ${} ".format(1000 - human_bank))
                            break
                        else:
                            print("You didn't win nor you didn't lose!")
                            break
                else:
                    print('Enter a valid amount. You have ${} to bet'.format(human_bank))
    game()

Note, if the user enters _n_ for no then the game terminates and tells them if they won or lost money along with the exact amount. If the user enters _y_ then the program will go on which is done through the continue statement which forces to the next cycle of the iteration. 

The _Game of Dice_ script is available on GitHub here: [insert link]

Get creative, you can extend this script if you’re motivated. You can make modifications such as emulating this game through a computer. In other words you can write a program in which the computer automatically wagers an amount, guess where the dice will roll on, and then simulate the dice rolling. The sequences will be quite odd but it will still be fun to watch the computer go through all of that madness. 


# Project: Random Person Generator

Have you ever seen those online name generators? I have, I’ve used them a couple of times for novels I was writing. Yes, I wrote novels under a pseudonym and occasionally had a difficult time creating names for fictitious characters! It may seem random (no pun) for a software engineer to do that, but there's actually quite a bit of parallels between writing code and writing stories. 

Anyhoo, to prevent from deviating let’s take the functionality of a simple random name generator a step or two further. Let’s write a script that allows us to randomly generate first names, last names, full names, emails, ages, telephone numbers, and email passwords. It will be a fun project to code and showcase!

## Script Hints

Let’s breakdown the script into individual functions so that it’s more modular. Here’s the functions that you can fill-in:

`first_name`: A function that allows us to generate male or female first names. By default we’ll let the program decide on the gendered pronoun.

`last_name`:  A function that allows us to generate surnames.

`full_name`: A function that allows us to generate first and last names. Like the first_name function it can be gendered or we can let the program decide this.

`age`: Generate a random age for the person. We can specify something like 1-100.

`phone_number`: Generate a random 10 digit phone number. For the sake of simplicity  we can decide on the region which in this example are North American phone numbers. The key here is that the first digit can’t be 0 or 1.

`email_password`: We can generate a random email address which uses the random person’s first and last names.

There’s some subtle decisions that we need to make. For one, the randomly generated full name is tied to the email that’s created. Since we’re creating separate functions for the first_name, last_name, and full_name  functions, how can we create the email so that it’s tied to the random name that’s generated? There’s a couple of ways to do this, for one we can call the first_name and last_name functions within the a function that creates the email.

Or, we can do the second approach which is the choice I decided to do which is to include a nested function within the outer function of full_name. Therefore, we can create the full name and within the function give the user the option of creating an email address that uses that randomly generated full name.

If they opt for no then the full name will just be generated, and if they opt for yes then a dictionary with randomly generated name and email will be created. By the way, there’s something else to think about. Where will we get the names from? You don’t have to download a massive file of names, instead I just did a couple of searches online looking for popular male and female names in the USA. 

You’re more than welcome to research popular names in any country you want. You can simply store the names in a list, and then you can use the choice function from the random module to randomly select a name as shown in the code snippet below:

<pre>
>>> from random import choice

>>> female_names = ['Molly', 'Sue', 'Angela']

>>> choice(female_names)

 ...

 'Angela'
 </pre>

To generate a random age is easy, you just need to generate a random number within a realistic interval:

<pre>
>>> from random import randint

>>> [randint(1, 100) for x in range(10)]

 ...

[2, 23, 99, 19, 96, 27, 61, 88, 53, 38]
</pre>

The above is simply a list comprehension that generates a list of 10 random numbers within the range of 1-100. To generate a random password here’s a hint, you should investigate the functions in the string module. You have some useful things available to you  in this module which are shown in the following code snippets:
<pre>
>>> from random import choice

>>> from string import ascii_letters

>>> from string import digits

>>> from string import punctuation

>>> ascii_letters

...

'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
</pre>

<pre>
>>> digits
...
 '0123456789'
 </pre>

<pre>
>>> punctuation
...

'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
</pre>

<pre>
>>> [ascii for ascii in ascii_letters]

 ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

>>> for x in range(5):
        print(choice(letters))

 ...

H

u

K

u

A
</pre>

## Solution

Below is what I cooked up:

    from random import randint
    from random import choice
    from string import ascii_letters
    
    def first_name(male=None, female=None):
    
        genders = ['m', 'f']
        male_first_names = ['Liam', 'Noah', 'William', 'Logan', 'Benjamin', 'Mason', 'Elijah', 'Oliver', 'Jacob', 'James']
        female_first_names = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Charlotte', 'Mia', 'Amelia', 'Harper', 'Evelyn']
        if male:
            name = choice(male_first_names)
            return name
        elif female:
            name = choice(female_first_names)
            return name
        elif male is None and female is None:
            pick_gender = choice(genders)
            if pick_gender == 'm':
                alias = choice(male_first_names)
                return alias
            elif pick_gender == 'f':
                alias = choice(female_first_names)
                return alias

The three functions from the import statement was previously discussed, and the first_name function contains the logic for randomly generating a first name. 

I decided to include a list named genders which holds the characters _m_ for male and _f_ for female. Contingent on if the user entered a keyword argument, the function would randomly select a male or female first name. If no keyword argument was entered then the program would randomly select a gendered first name by passing the genders list into the choice function. Let’s observe the function declaration:

    male=None, female=None

The keyword arguments are both set to None. Therefore, we can check if the user passed in a value for the keyword argument if it’s not equal to None. For example, let’s just look at the following snippet:

    if male:
            name = choice(male_first_names)
            return 

The variable male will be True if it’s not empty or None. If that’s the case then a random male name will be generated and vice versa. Moving along, let’s implement the code for generating the last name:

    def last_name():
     
        last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Martinez', 'Sanchez', 'Nguyen', 'Barnes']
        surname = choice(last_names)
        return surname

This is quite simple. I’ve just researched some popular surnames in the US on Wikipedia, added it to a list, and then implemented a random selection by using the `choice` function. Next, let’s cook up the logic for creating a full name. 

Now, bear in mind that the route I took was to include an inner function called `create_name`. I did this because I saw where more or less the same logic was being used in two separate parts of the function. Therefore, one idea is to wrap it inside of a function and then call it when needed. The inner function I created for this purpose is called `create_name`; below is the logic for the `full_name` function:

    def full_name(male=None, female=None):
      
        email_services = ['gmail', 'aol', 'yahoo', 'aol', 'yandex', 'mail']
        create_email = input("Do you want to create an email address? Enter 'y' for yes"
                             "or 'n' for no. ").lower()
        def create_name():
            if male:
                male_name = first_name(male='m')
                last = last_name()
                full = male_name + ' ' + last
                return full
            elif female:
                female_name = first_name(female='f')
                last = last_name()
                full = female_name + ' ' + last
                return full
            else:
                first = first_name()
                last = last_name()
                full = first + ' ' + last
                return full
        if create_email == 'y':
           email_id = {
               'name': None,
               'email': None
           }
           moniker = create_name()
           first, last = moniker.split(' ')
           e_address = (first + '.' + last + '@' + choice(email_services) + '.com').lower()
           email_id['name'] = moniker
           email_id['email'] = e_address
           return email_id
        elif create_email == 'n':
            name = create_name()
            return name

Inside of the `create_name` function is similar logic that you saw in the `first_name` function. The reason for this is that it too gives the user the option of specifying a gender first-name which will be combined with the last-name. In this function the user is asked if they want to create an email or not. If they entered _y_ then a dictionary will be created and returned that contains the name and email mapping pair; if not, then just the full name will be returned. 

The email service like gmail, yahoo, yandex, etc, is also generated by adding it to a list, randomly selecting an item from it with choice, and then affixing it to the end of the email string. The following code snippet shows how to randomly generate the age of a person which can be done in one line as shown below:

    def age():
    
        person_age = randint(1, 100)
        return person_age


That’s simple stuff, just randomly generate a sequence of numbers within the range of 1-100 and then return it. Let’s analyze the logic that’s needed to randomly create a North American phone number:

    def phone_number():
       
        number = ''
        for x in range(1, 11):
            if x == 1:
                num = randint(2, 9)
                number += str(num)
            elif x == 4:
                num = randint(2, 9)
                number += str(num)
            else:
                num = randint(0, 9)
                number += str(num)
            if x % 3 == 0 and x <= 6
                    number += '-'
        return number

The first thing that we need to think of is what exactly is a valid North American phone number? It’s a number that can be placed in the following format:

    XNN-XNN-NNNN

In the above syntax _X_ represents a number within the range of 2-9, while _N_ represents a number within the range of 0-9. 

Once we understand that we can create a loop that iterates over a range of 10 (the total digits in a phone number) and then randomly generate a number within the range of 0-9 EXCEPT when it’s the first or fourth digit. 

The reason for this is because the first and fourth digits can’t be within the range of 0-9, but instead within the range of 2-9; this can be accomplished with conditional checks. Also, there’s two more things to keep note of. One, we need to convert the integers to strings because we want to do concatenation not sum integers. Here’s an example on summing integers vs concatenation:

<pre>
>>> x = 5
>>> y = 10
>>> x + y
...
15

>>> str(x) + str(y)
...
'510'
</pre>

Two, we want to format the string using hyphens to separate them. This appears simple at first glance because the string has a pattern in which the dash appears every 3 digits. If we implement a potential solution using just modulus arithmetic then the problem with this is that we could end up with a phone number that looks like this:

    948-456-857-7

The reason for this is that the dash is added after every group of 3s. However, we can bypass this by adding a conditional check that says: _only add a hyphen if we are not past the sixth digit_

This ensures that the 3rd hyphen is NOT added. 

Last but not least, we must create a simple password of an arbitrary length. We can accomplish this in a single line using a list comprehension:

    def email_password(length=7):
       
        return ''.join([choice(ascii_letters) for x in range(length)])

We now have several functions coded so the next step is to test them. I’ve created a simple function for this:

    def run():
        for x in range(3):
            print(first_name())
        print()
        for x in range(3):
            print(last_name())
        print()
        for x in range(3):
            print(full_name())
        print()
        for x in range(3):
            print(age())
        print()
        for x in range(3):
            print(phone_number())
        print()
        for x in range(3):
            print(email_password())

Here’s some test output when the run function is ran through the shell assuming that the file is named `random_person.py`:

    $ python random_person.py
<pre>
Logan  
Ava  
Mia  
  
Jones  
Smith  
Nguyen  
  
Do you want to create an email address? Enter 'y' for yes or 'n' for no. y  
{'name': 'Charlotte Jones', 'email': 'charlotte.jones@gmail.com'}  
Do you want to create an email address? Enter 'y' for yes or 'n' for no. y  
{'name': 'Mia Smith', 'email': 'mia.smith@yahoo.com'}  
Do you want to create an email address? Enter 'y' for yes or 'n' for no. y  
{'name': 'Ava Miller', 'email': 'ava.miller@yahoo.com'}  
  
87  
58  
62  
  
774-201-6881  
908-307-6702  
772-268-8114  
  
MgxpMRp  
kCtcLUp  
VrWMVgq 
</pre>

View the full source code for [Random Person Generator](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/sourcecode/ch_03/random_person_generator.py). 

## Project: The California State Lottery

Most states in the US allows denizens the ability to play the lottery. While I’m not advocating for folks to become chronic gamblers, I am advocating simulating the winning numbers through a python program. In this project we’re going to simulate the various lotteries that California makes available which are:

-   Daily 3: Pick any 3 numbers within the range of 0-9.
    
-   Daily 4: Pick any 4 numbers within the range of 0-9.
    
-   Fantasy 5: Pick any 5 numbers within the range of 1-39.
    
-   Super Lotto PLUS: Pick any five numbers within the range of 1-47, and then one mega number from 1-27.
    
-   Mega Millions: Select six numbers from two separate pool of numbers, five different numbers from 1-70, and one number from 1-25.
    
-   Powerball: Select 5 numbers between 1-69, and one Powerball number between 1-26.
    

There’s many ways to play the lottery. For simplicity’s sake we’ll give the user just one option to bet which is a straight bet, or a bet in which the player must select all of the winning numbers in the exact order in which they occur.


## Script Hints

An easy way to solve this is to create a function that represents each type of lottery, and then fill in the respective logic. Once you know how to code The Daily 3, then you’ll also know how to code the rest of them. The reason for this is because the logic is in essence the same, the only thing that changes are the amount of numbers to predict along with their ranges. Below are the functions to be coded:

  
-   daily_3
    
-   daily_4
    
-   fantasy_5
    
-   super_lotto_plus
    
-   mega_millions
    
-   powerball
  

## Solution

  
Let’s put the above hint into motion and code the `daily_3`. Here’s the start:

    from random import randint
    from time import sleep
    def daily_3():
        """
        emulates the daily 3
        lottery
        """
        print("Welcome! You're playing Daily 3.")
        lucky_one = randint(0, 9)
        lucky_two = randint(0, 9)
        lucky_three = randint(0, 9)
        guess_one = int(input('Guess your lucky number: 0 – 9 '))
        guess_two = int(input('Guess your lucky number: 0 – 9 '))
        guess_three = int(input('Guess your lucky number: 0 – 9 '))

We need to import the randint function to generate a range of random numbers, and then we could use the sleep function from the time module to pause the program for more theatricality. 

The program starts off with a cordial welcome message and then three separate random variables are generated. 

Next,  three consecutive prompts are generated which asks the user for their guess. Once done the program can then display the results of the randomly generated numbers:

        print("Here's the Daily 3 results...")
        sleep(3)
        print(lucky_one)
        sleep(2)
        print(lucky_two)
        sleep(2)
        print(lucky_three)
        print([lucky_one,lucky_two, lucky_three])

The first random variable is printed followed by a two-second pause, and then the other two variables follow the same steps; all of the random variables are then printed as a list. 

Last, the user input needs to be checked to see if it matches the randomly generated numbers. This can be easily accomplished with an if statement that checks each guess against the variable that holds the respective random number. If any of these evaluates to False then we know that the user did not win the lottery. Below is the logic for this:

     if guess_one == lucky_one and guess_two == lucky_two and guess_three == lucky_three:
            print("Congrats! You won $500")
        else:
            print("Today wasn't your day! Try again.")


That's all there is to it! Now, fill out the remaining functions and once done you can check them against the [solution here](https://github.com/purcellconsult/Code-Cool-Stuff-With-Python/blob/master/sourcecode/ch_03/california_lottery.py). 

## The best way to support this project is to [purchase a digital copy](https://www.amazon.com/Code-Cool-Stuff-Python-Purcell-ebook/dp/B081XJMNRB) on Amazon and leave a review. 