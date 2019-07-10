#########################################
# Tkinter Grid Example
# --------------------
# Lays out the various colors and their
# labels in a declining step like
# format.
#
# By Doug Purcell
# http://www.purcellconsult.com
#
##########################################

import tkinter as tk

root = tk.Tk()
root.title('Tkinter Grid Geometry Manager')
root.geometry('875x200')

colors = ['black', 'red', 'orange', 'blue', 'green',
          'yellow', 'brown', 'gold']

i = 0
for x in colors:
    tk.Label(text=x, width=15).grid(row=i+1, column=i)
    tk.Label(bg=x, width=15).grid(row=i, column=i)
    i += 1
tk.mainloop()