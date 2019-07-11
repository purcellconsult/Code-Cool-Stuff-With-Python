#################################
# Listbox Demo Tkinter
# --------------------
#
# Add a widget that allows the user
# to select multiple options. 
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#################################

import tkinter as tk

root = tk.Tk()
root.geometry('400x400')

list_box_1_var = tk.StringVar()

list_box_1 = tk.Listbox()
list_box_1.pack()
list_box_1.insert(tk.END, 'English')
list_box_1.insert(tk.END, 'Spanish')
list_box_1.insert(tk.END, 'French')
list_box_1.insert(tk.END, 'German')
list_box_1.insert(tk.END, 'Italian')

tk.mainloop()