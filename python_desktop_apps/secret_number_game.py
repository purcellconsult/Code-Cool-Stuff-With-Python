#####################################
# Secret number game written in
# python and Tkinter
# -----------------------------
#
# When ran gives the user a random
# amount of tries within the range
# of 1-15 to guess the secret number
# which will be in the range of 1-100.
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#######################################


import tkinter as tk
from random import randint


class SecretNumberGame:
    def __init__(self):
        self.root = tk.Tk()
        self.secret_number = randint(1, 100)
        self.tries = randint(1, 15)

        # a list of StringVars

        self.secret_num_str_var = tk.StringVar()
        self.secret_num_str_var.set('Secret Number is ?????')
        self.your_guess = tk.StringVar()
        self.hint = tk.StringVar()

        # Labels

        self.game_banner = tk.Label(text='The Secret Number Guessing Game!').place(x=0, y=0, width=500, height=50)
        self.guess_number_label = tk.Label(text='Guess Number').place(x=50, y=85, width=100)
        self.your_tries = tk.Label(text=f'You have {self.tries} tries').place(x=225, y=180, width=200)

        # Entry Widgets

        self.guess_number_widget = tk.Entry(textvariable=self.your_guess).place(x=225, y=75, height=40, width=150)
        self.the_secret_number = tk.Entry(textvariable=self.secret_num_str_var).place(x=225, y=250, width=175,
                                                                                      height=25)
        # Button

        self.guess_budget = tk.Button(text='Guess', command=self.guess).place(x=225, y=125, width=125)

    def guess(self):
        """
        method updates the GUI
        after each user guess.
        """
        your_guess = self.your_guess.get()
        your_guess = int(your_guess)

        if self.tries == 1:
            self.your_tries = tk.Label(text=f'Game Over!!!').place(x=225, y=180, width=200)
            self.secret_num_str_var.set(self.secret_number)
            tk.Label(text=f'{self.secret_number} is the secret number!').place(x=225, y=230, width=250)
            self.guess_number_widget = None
        elif your_guess == self.secret_number:
            self.your_tries = tk.Label(text='You Win!!!').place(x=225, y=180, width=200)
        elif your_guess > self.secret_number:
            self.tries -= 1
            tk.Label(text=f'{your_guess} is too big').place(x=225, y=160, width=200)
            self.your_tries = tk.Label(text=f'You have {self.tries} tries').place(x=225, y=180, width=200)
        elif your_guess < self.secret_number:
            self.tries -= 1
            tk.Label(text=f'{your_guess} is too small').place(x=225, y=160, width=200)
            self.your_tries = tk.Label(text=f'You have {self.tries} tries').place(x=225, y=180, width=200)

    def setup(self):
        """
        Setups the basics of the app.
        """

        self.root.title('Secret Number Game')
        self.root.config(bg='tan')
        self.root.geometry('500x500')
        self.root.mainloop()

    def run(self):
        """
        Fires the app.
        """
        self.setup()


if __name__ == '__main__':
    SecretNumberGame().run()
