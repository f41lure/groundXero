#from passlib.apps import custom_app_context as pwd_context
from tkinter import *
import tkinter.filedialog
import time
import difflib

from tkinter import messagebox as pop_up

EMPTY_TITLE_ERROR_MESSAGE_OPEN = "Please write the name of the file you want to open in the given field."
FILE_NOT_FOUND_ERROR_MESSAGE = "No file with the given title was found, remember that this text editor can only read files in its directory."

root = tkinter.Tk()
##text=Text(root)
##text.grid(expand=True)

scrollb = Scrollbar(root)
text = Text(root)
scrollb.pack(side=RIGHT, fill=Y)
text.pack(side=LEFT, expand=True, fill=BOTH)
scrollb.config(command=text.yview)
text.config(yscrollcommand=scrollb.set)

##scrollb = Scrollbar(root, command=text.yview)
##scrollb.grid(row=0, column=1, sticky='nsew')
##text['yscrollcommand'] = scrollb.set

def help():
    root = tkinter.Tk()
    texta=Text(root)
    texta.grid()
    texta.insert(END,"""HELP\n\nThis is a bare-bones text-editor made in Python and the tkinter framework.
Type in the textbox. To save your text, click on Options and choose Save.
To open a file(In the same directory as this program), enter the filename in the entry box above the Options button.
Then click Options and choose Open.
To add the Date, click Options and choose Date.
To convert the text to leetspeak, click Options and choose Convert to LeetSpeak.
To hash the text, click Options and choose Hash.
To check the text for spelling mistakes, click Options and choose Check for Mistakes.
To change the font color, click Color and choose.
To change the the font, click Font and choose.""")


def saveas():                                                   #  Function to save file
    global text
    savelocation=tkinter.filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
#    text.insert("1.0", "\n")                                    # Insert a line at the start that contains the file's current
    text.insert("1.0", text.cget("font"))                       # font and color.
    text.insert("1.0", ",")                                     # --FORMAT--
    text.insert("1.0", text.cget("fg"))                         # [color],[font]\n[text]   
    t = text.get("1.0", "end-1c")
    file1.write(t)
    file1.close()

def leet():                                                     # Function to convert text to 1337speak
    t = text.get("1.0", "end-1c")
    getchar = lambda c: chars[c] if c in chars else c
    chars = {"a":"@","e":"3","i":"1","l":"1","o":"0","s":"5","t":"7"}
    data = ''.join(getchar(c) for c in t)
    text.delete("1.0", "end")
    text.insert(END,data)
##    text.after(1000, leet)

def hash():                                                     # Function to hash text
    t = text.get("1.0", "end-1c")
    data = pwd_context.hash(t)
    text.delete("1.0", "end")
    text.insert(END,data)
##    text.after(1000, hash)

def check():
    root = tkinter.Tk()                                         # Spell checker.
    text2=Text(root)                                            # Needs special dictionary
    text2.grid()
    text2.insert(END,"MISSPELLED WORDS:\n")
    global text
    t = text.get("1.0", "end-1c")
    words = open("dictionary.txt").readlines()
    words = [word.strip() for word in words]
    hash = {}
    for word in words:
        hash[word] = True
    for word in t.split():
        found = word in hash
        if found == False:
            if word.isalpha():
                foo = difflib.get_close_matches(word, words)
                text2.insert(END, word , " MIGHT BE CHANGED TO: ", foo , "\n")


def center_align():
    global text
    t = text.get("1.0", "end-1c")
    text.tag_configure("center", justify='center')
    text.insert("1.0", '')
    text.tag_add("center", "1.0", "end")

def right_align():
    global text
    t = text.get("1.0", "end-1c")
    text.tag_configure("right", justify='right')
    text.insert("1.0", '')
    text.tag_add("right", "1.0", "end")

def left_align():
    global text
    t = text.get("1.0", "end-1c")
    text.tag_configure("left", justify='left')
    text.insert("1.0", '')
    text.tag_add("left", "1.0", "end")


#Functions for fonts
def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

def FontMonaco():
    global text
    text.config(font="Monaco")

def FontArial():
    global text
    text.config(font="Arial")

def FontFutura():
    global text
    text.config(font="Futura")

def FontChiller():
    global text
    text.config(font="Chiller")

def FontCalibri():
    global text
    text.config(font="Calibri")

def FontConsolas():
    global text
    text.config(font="Consolas")
def Font8514oem():
    global text
    text.config(font="8514oem")
def FontLucida():
    global text
    text.config(font="Lucida")
def FontGeorgia():
    global text
    text.config(font="Georgia")
def FontEbrima():
    global text
    text.config(font="Ebrima")
def FontElephant():
    global text
    text.config(font="Elephant")
def FontMagneto():
    global text
    text.config(font="Magneto")
def FontRoman():
    global text
    text.config(font="Roman")
def FontPapyrus():
    global text
    text.config(font="Papyrus")
def FontOnyx():
    global text
    text.config(font="Onyx")
def FontPlaybill():
    global text
    text.config(font="Playbill")
def FontAlgerian():
    global text
    text.config(font="Algerian")

#Functions for colors
def ColorRed():
    global text
    text.config(fg="Red")

def ColorBlue():
    global text
    text.config(fg="Blue")

def ColorGreen():
    global text
    text.config(fg="Green")

def ColorBrown():
    global text
    text.config(fg="Brown")

def ColorYellow():
    global text
    text.config(fg="Yellow")

def ColorOrange():
    global text
    text.config(fg="Orange")

def ColorPurple():
    global text
    text.config(fg="Purple")

def Size12():
    global text
    text.config(fg="Purple")


def add_date():
    full_date = time.localtime()
    day = str(full_date.tm_mday)
    month = str(full_date.tm_mon)
    year = str(full_date.tm_year)
    date = ("\n"+day+'/'+month+'/'+year)
    text.insert(tkinter.INSERT, date, "a")

def _open():
    filelocation=tkinter.filedialog
    if not file_title.get():
        pop_up.showerror("Title is empty.",EMPTY_TITLE_ERROR_MESSAGE_OPEN)
        return 1
    filename = file_title.get()
##    if not ".txt" in file_title.get():
##        filename = file_title.get() + ".txt"

    try:
        with open(filename) as f:
            first_line = f.readline()
            data = first_line.split(',')
            global text
            text.config(fg=data[0])                                         # Get the first line of the program, which contains the color and font,
            text.config(font=data[1])                                       # and set the rest of the text to it.
            text.delete("1.0",tkinter.END)                                  # Delete that line for the user
            text.insert(tkinter.INSERT, f.read(), "a")
            text.delete("1.0")
    except IOError:
        pop_up.showerror("File not found.",FILE_NOT_FOUND_ERROR_MESSAGE)


EMPTY_TITLE_ERROR_MESSAGE_OPEN = "Please write the name of the file you want to open in the given field."


top = tkinter.Frame(root)
temp = tkinter.Label(root,text="Title:")
temp.pack(in_ = top,side=tkinter.TOP)


file_title = tkinter.Entry(root)
file_title.pack()
file_title.insert(0, 'File to open')
file_title.bind("<FocusIn>", lambda args: file_title.delete('0', 'end'))
file_title.pack()

opt=Menubutton(root, text="Options")
opt.pack()
opt.menu=Menu(opt, tearoff=0)
opt["menu"]=opt.menu
opt.menu.add_command(label="Open", command=_open)
opt.menu.add_command(label="Save", command=saveas)
opt.menu.add_command(label="Add date",command=add_date)
opt.menu.add_command(label="Convert to LeetSpeak",command=leet)
opt.menu.add_command(label="Hash",command=hash)
opt.menu.add_command(label="Check for Mistakes",command=check)
opt.menu.add_command(label="Help",command=help)

color=Menubutton(root, text="Colour")
color.pack()
color.menu=Menu(color, tearoff=0)
color["menu"]=color.menu

font=Menubutton(root, text="Font")
font.pack()
font.menu=Menu(font, tearoff=0)
font["menu"]=font.menu


center = tkinter.Button(root, fg="red", text="Center Align", command=center_align)
center.pack()
right = tkinter.Button(root, fg="red", text="Right Align", command=right_align)
right.pack()
left = tkinter.Button(root, fg="red", text="Left Align", command=left_align)
left.pack()

Helvetica=IntVar()
Monaco=IntVar()
Arial=IntVar()
Courier=IntVar()
Futura=IntVar()
Note=IntVar()
Felt=IntVar()
Consolas=IntVar()
oem=IntVar()
Lucida=IntVar()
Georgia=IntVar()
Ebrima=IntVar()
Elephant=IntVar()
Magneto=IntVar()
Roman=IntVar()
Papyrus=IntVar()
Onyx=IntVar()
Playbill=IntVar()
Algerian=IntVar()

Red=IntVar()
Blue=IntVar()
Green=IntVar()
Brown=IntVar()
Yellow=IntVar()
Orange=IntVar()
Purple=IntVar()


font.menu.add_checkbutton(label="Courier", variable=Courier,
command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=Helvetica,
command=FontHelvetica)
font.menu.add_checkbutton(label="Monaco", variable=Monaco,
command=FontMonaco)
font.menu.add_checkbutton(label="Arial", variable=Arial,
command=FontArial)
font.menu.add_checkbutton(label="Futura", variable=Futura,
command=FontFutura)
font.menu.add_checkbutton(label="Chiller", variable=Note,
command=FontChiller)
font.menu.add_checkbutton(label="Calibri", variable=Felt,
command=FontCalibri)
font.menu.add_checkbutton(label="Consolas", variable=Consolas,
command=FontConsolas)
font.menu.add_checkbutton(label="8514oem", variable=oem,
command=Font8514oem)
font.menu.add_checkbutton(label="Lucida", variable=Lucida,
command=FontLucida)
font.menu.add_checkbutton(label="Georgia", variable=Georgia,
command=FontGeorgia)
font.menu.add_checkbutton(label="Ebrima", variable=Ebrima,
command=FontEbrima)
font.menu.add_checkbutton(label="Elephant", variable=Elephant,
command=FontElephant)
font.menu.add_checkbutton(label="Magneto", variable=Magneto,
command=FontMagneto)
font.menu.add_checkbutton(label="Roman", variable=Roman,
command=FontRoman)
font.menu.add_checkbutton(label="Papyrus", variable=Papyrus,
command=FontPapyrus)
font.menu.add_checkbutton(label="Onyx", variable=Onyx,
command=FontOnyx)
font.menu.add_checkbutton(label="Playbill", variable=Playbill,
command=FontPlaybill)
font.menu.add_checkbutton(label="Algerian", variable=Algerian,
command=FontAlgerian)

color.menu.add_checkbutton(label="Red", variable=Red,
command=ColorRed)
color.menu.add_checkbutton(label="Blue", variable=Blue,
command=ColorBlue)
color.menu.add_checkbutton(label="Green", variable=Green,
command=ColorGreen)
color.menu.add_checkbutton(label="Brown", variable=Brown,
command=ColorBrown)
color.menu.add_checkbutton(label="Yellow", variable=Yellow,
command=ColorYellow)
color.menu.add_checkbutton(label="Orange", variable=Orange,
command=ColorOrange)
color.menu.add_checkbutton(label="Purple", variable=Purple,
command=ColorPurple)

root.mainloop()
