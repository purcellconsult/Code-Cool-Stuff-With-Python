####################################
# Calculator app using Tkinter
# ------------------------------
#
# App Features:
# Add numbers
# Subtract numbers
# Divide numbers
# Multiply numbers
# Square root
# Modulus
# Square numbers
# Backspace
#
# By Doug Purcell
# http://www.purcellconsult.com
#
####################################

import tkinter as tk
from math import sqrt
from math import pow


class CalculatorApp(object):
    def __init__(self):
        pass


user_input = ''  # the contents the user types into the lcd screen


def press(num):
    """
    Method updates the text to be displayed
    to the lcd screen when pressed.
    """
    global user_input

    user_input = user_input + str(num)
    result.set(user_input)


def back():
    lcd_screen.delete(-1, last=1)


def equal():
    """
    Method that evaluates the final expression.
    """
    try:
        global user_input
        answer = str(eval(user_input))
        result.set(answer)
    except:
        result.set('ERROR')


def square_root():
    """
    Computes the square root. You must enter numbers
    first and then press the √ button.
    """

    x = lcd_screen.get()
    x = sqrt(eval(x))
    result.set(x)


def squared():
    """
    Squares any number or expression.
    """
    x = lcd_screen.get()
    x = pow(eval(x), 2)
    result.set(x)


def clear():
    """
    clears the contents of the lcd screen.
    """
    global user_input
    user_input = ''
    result.set(user_input)


if __name__ == '__main__':
    root = tk.Tk()
    result = tk.StringVar(root)  # the result of the user's actions

    root.configure(background='BurlyWood')

    root.title('Calculator App')
    root.geometry('300x225')

    lcd_screen = tk.Entry(root, textvariable=result, font="Courier 12 bold", fg='red', bg='black', border=2)
    lcd_screen.grid(row=0, columnspan=5, ipadx=10)
    lcd_screen.insert(0, '0.00000')

    # 7,8, 9, *, ←, and C buttons

    seven_button = tk.Button(root, text='7', command=lambda: press(7))
    seven_button.grid(row=10, column=0)

    eight_button = tk.Button(root, text='8', command=lambda: press(8))
    eight_button.grid(row=10, column=1)

    nine_button = tk.Button(root, text='9', command=lambda: press(9))
    nine_button.grid(row=10, column=2)

    divide_button = tk.Button(root, text='÷', command=lambda: press('/'))
    divide_button.grid(row=10, column=3)

    back_button = tk.Button(root, text='←', command=lambda : back())
    back_button.grid(row=10, column=4)

    clear_button = tk.Button(root, text='C', command=lambda: clear())
    clear_button.grid(row=10, column=5)

    # 4, 5, 6, x, (, and ) buttons

    four_button = tk.Button(root, text='4', command=lambda: press(4))
    four_button.grid(row=11, column=0)

    five_button = tk.Button(root, text='5', command=lambda: press(5))
    five_button.grid(row=11, column=1)

    six_button = tk.Button(root, text='6', command=lambda: press(6))
    six_button.grid(row=11, column=2)

    star_button = tk.Button(root, text='x', command=lambda: press('*'))
    star_button.grid(row=11, column=3)

    left_parentheses = tk.Button(root, text='(', command=lambda: press('('))
    left_parentheses.grid(row=11, column=4)

    right_parentheses = tk.Button(root, text=')', command=lambda: press(')'))
    right_parentheses.grid(row=11, column=5)

    # 1, 2, 3, -, x², and √ buttons

    one_button = tk.Button(root, text='1', command=lambda: press(1))
    one_button.grid(row=12, column=0)

    two_button = tk.Button(root, text='2', command=lambda: press(2))
    two_button.grid(row=12, column=1)

    three_button = tk.Button(root, text='3', command=lambda: press(3))
    three_button.grid(row=12, column=2)

    subtract_button = tk.Button(root, text='-', command=lambda: press('-'))
    subtract_button.grid(row=12, column=3)

    squared_button = tk.Button(root, text='x²', command=lambda: squared())
    squared_button.grid(row=12, column=4)

    square_root_button = tk.Button(root, text='√', command=lambda: square_root())
    square_root_button.grid(row=12, column=5)

    # 0, ., %, +,  and '=' buttons

    zero_button = tk.Button(root, text='0', command=lambda: press(0))
    zero_button.grid(row=13, column=0)

    decimal_button = tk.Button(root, text='.', command=lambda: press('.'))
    decimal_button.grid(row=13, column=1)

    percent_button = tk.Button(root, text='%', command=lambda: press('%'))
    percent_button.grid(row=13, column=2)

    addition_button = tk.Button(root, text='+', command=lambda: press('+'))
    addition_button.grid(row=13, column=3)

    equal_button = tk.Button(root, text='=', width=4, command=equal)
    equal_button.grid(row=13, column=4)

    root.mainloop()
