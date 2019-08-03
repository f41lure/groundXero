import pygame
import time
import os
from tkinter import *
from tkinter import ttk

pygame.mixer.init()
def main(song):
    pygame.mixer.init()
    print("Playing...")
    pygame.mixer.music.load("C:\\Users\\adnan zafar khan\\" + song)
    pygame.mixer.music.play()



directory_in_str = "C:\\Users\\adnan zafar khan"

directory = os.fsencode(directory_in_str)
list1 = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    list1.append(filename)


##master = Tk()
##
##variable = StringVar(master)
##
##variable.set(list1[0]) # default value
##
##w = OptionMenu(master, variable, *list1).grid(row=0, column=1)
##
##abc = str(variable.get())
##
####Button(master, text='Convert', command=main(abc)).grid(row=3, column=0, sticky=W, pady=4)
##
##def change_dropdown(*args):
##    main(abc)
##
##variable.trace('w', change_dropdown)
##
##p = input("pause")
##if p == "y":
##    pygame.mixer.music.pause()
##
##master.mainloop()


root = Tk()
root.title("Tk dropdown example")
 
# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)
 
# Create a Tkinter variable
tkvar = StringVar(root)
 
# Dictionary with options

tkvar.set(list1[0]) # set the default option
 
popupMenu = OptionMenu(mainframe, tkvar, *list1)
Label(mainframe, text="Choose a song").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

pause = Button(mainframe, text="Pause", command=pygame.mixer.music.pause).grid(row = 3, column = 1)

play = Button(mainframe, text="Play", command=pygame.mixer.music.unpause).grid(row = 3, column = 2)


 
# on change dropdown value
def change_dropdown(*args):
    main(str(tkvar.get()))
 
# link function to change dropdown
tkvar.trace('w', change_dropdown)
 
root.mainloop()
