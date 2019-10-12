##################################
# Tkinter CheckButton Demo
# ------------------------
# A simple demo that shows how
# to use the checkbox in python.
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
###################################

import tkinter as tk

root = tk.Tk()
root.geometry('350x300')
root.title('Tkinter CheckButton Widget')

var_1 = tk.IntVar()
var_2 = tk.IntVar()
var_3 = tk.IntVar()
var_4 = tk.IntVar()
var_5 = tk.IntVar()


def fire():
    print(var_1.get())


check_button_a = tk.Checkbutton(text=' Choice a', variable=var_1, command=fire).pack()
check_button_b = tk.Checkbutton(text=' Choice b', variable=var_2, command=fire).pack()
check_button_c = tk.Checkbutton(text=' Choice c', variable=var_3, command=fire).pack()
check_button_d = tk.Checkbutton(text=' Choice d', variable=var_4, command=fire).pack()
check_button_e = tk.Checkbutton(text=' Choice e', variable=var_5, command=fire).pack()

tk.mainloop()