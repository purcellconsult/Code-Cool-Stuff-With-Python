###################################
# Tkinter pack example
# --------------------
#
#
#
#
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
###################################


import tkinter as tk

root = tk.Tk()
root.title('Tinker Pack Example')

colors = ['black', 'red', 'orange', 'blue', 'green',
          'yellow', 'brown', 'gold']

label_one = tk.Label(text='The Black Label').pack()
label_one_black = tk.Label(root, bg=colors[0]).pack(fill=tk.X)


root.mainloop()


