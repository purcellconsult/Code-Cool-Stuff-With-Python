###################################
# Tkinter pack example
# --------------------
#
# Example of the pack geometry manager
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
###################################


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

