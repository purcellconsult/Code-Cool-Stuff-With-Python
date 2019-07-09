########################################
# Tkinter place example
# --------------------
#
# Example of the pack geometry manager
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#########################################


import tkinter as tk

root = tk.Tk()
root.title('Tinker Place Geometry Manager')
root.geometry('375x350')

colors = ['black', 'red', 'orange', 'blue', 'green',
          'yellow', 'brown', 'gold']

width, height = 0, 0
for x in range(len(colors)):
    tk.Label(text=colors[x], width=10).place(x=0, y=height)
    tk.Label(bg=colors[x], width=15).place(x=100, y=height)
    height += 15

tk.mainloop()