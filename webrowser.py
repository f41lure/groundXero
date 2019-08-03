from tkinter import *
import webbrowser


master = Tk()

Label(text="Bare Browser").pack()

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

search = Entry(master)
search.pack()

search.focus_set()

def callback():
    s = search.get
    webbrowser.open(s)

b = Button(master, text="Go", width=10, command=callback)
b.pack()

mainloop()

mainloop()
