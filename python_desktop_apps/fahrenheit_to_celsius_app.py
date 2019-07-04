##########################################
# A simple app that converts fahrenheit
# to celsius and vice versa.
#
# Features:
# --------
# Converts celsius to fahrenheit
# Converts fahrenheit to celsius
#
# By Doug Purcell
# http://www.purcellconsult.com
#
##########################################

import tkinter as tk


def fahrenheit_to_celsius():
    """
    Fahrenheit to Celsius formula is:
    (x - 32) * 5/ 9
    """
    try:
        celsius = float(get_fahren.get())

        result = (celsius - 32) * 5 / 9

        # rounds float to 3 places, then converts to string
        result = str(round(result, 3)) + '° C'

        get_fahren.set(result)

    except ValueError as e:
        get_fahren.set('ERROR!!!')


def celsius_to_fahrenheit():
    """
    Celsius to Fahrenheit formula is:
    F = (x x 9/5) + 32
    """
    try:
        fahrenheit = float(get_celsius.get())

        result = (fahrenheit * 9/5) + 32

        # rounds float to 3 places, then converts to string
        result = str(round(result, 3)) + '° F'

        get_celsius.set(result)

    except ValueError as e:
        get_celsius.set('ERROR!!!')


root = tk.Tk()
root.title('Temperature Converter')
root.geometry('500x150')
root.configure(bg='tan')


# fahrenheit to celsius label, widget, and button

fahrenheit_to_celsius_label = tk.Label(root, text='Temperature in Fahrenheit').place(x=0, y=0)

get_fahren = tk.StringVar(root)

fahrenheit_to_celsius_widget = tk.Entry(root, text='enter temperature', textvariable=get_fahren, bg='white smoke').place(x=200, y=0, width=225)

get_fahren.set('° F')
fahrenheit_to_celsius_button = tk.Button(root, text='convert', width=15, border=2, command=fahrenheit_to_celsius)

fahrenheit_to_celsius_button.place(x=200, y=25, width=150)


# celsius to fahrenheit label, widget, and button

celsius_to_fahrenheit_label = tk.Label(text='Temperature in Celsius').place(x=0, y=85)

get_celsius = tk.StringVar()

get_celsius.set('° C')

read_celsius_widget = tk.Entry(root, text='enter temperature', textvariable=get_celsius, bg='white smoke').place(x=200, y=85, width=225)


celsius_to_fahren_button = tk.Button(root, text='convert', width=15, border=2, command=celsius_to_fahrenheit)

celsius_to_fahren_button.place(x=200, y=115, width=150)


root.mainloop()
