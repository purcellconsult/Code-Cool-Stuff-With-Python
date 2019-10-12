import tkinter as tk

root = tk.Tk()  # starts a tcl/tk interpreter under the cover
root.title('Greetings App')
root.geometry('350x250')


def greeting():
    greetings = tk.Label(root, bg='tan', borderwidth=3.5, relief='groove', text="Hello {} :-)! Welcome to the wonderful\n"
                                    "world of programming. Enjoy your stay!".format(default_value.get()))
    greetings.pack()


default_value = tk.StringVar()
default_value.set('????')

first_name_label = tk.Label(root, text='What\'s your name?').pack()

first_name = tk.Entry(root, textvariable=default_value).pack()

button = tk.Button(text='Click Me!', command=greeting).pack()

tk.mainloop()