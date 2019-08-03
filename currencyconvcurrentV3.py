#############################################################################################################################################################################################
# CURRENCY CONVERTER                                                                                                                                                                        #
# Version 1.5 BETA                                                                                                                                                                          #
# With tkinter-based GUI                                                                                                                                                                    #
# Uses BeautifulSoup                                                                                                                                                                        #
#                                                                                                                                                                                           #
### PROBLEMS:                                                                                                                                                                               #
#                                                                                                                                                                                           #
# > Slow and sluggish retrieval of data from net                                                                                                                                            #                                                                                                                                                          +
# > GUI lacking advancements.                                                                                                                                          #
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#                                                                                                                                                                                           #
# Coded by ___Ibrahim Adnan____                                                                                                                                                             #
# On 26/11/2017                                                                                                                                                                             #
# Sunday, November 2017                                                                                                                                                                     #
# At approximately 10:26 PM PST                                                                                                                                                             # 
#                                                                                                                                                                                           #
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
### USAGE:
#
# > Enter country currency codes with aid of drop-down menus
#############################################################################################################################################################################################


# import libraries
from tkinter import * 

import urllib.request as ur, re
import urllib.error
from bs4 import BeautifulSoup


"""To provide fodder for drop-downs"""

# Gets codes and stores in list "codes"
OPTIONS = []
currency = 'http://www.xe.com/iso4217.php'                  # Store website URL
currency_p = ur.urlopen(currency)                           
soup2 = BeautifulSoup(currency_p, 'html.parser')            # Parse site

currencies = soup2.find('tbody')                            # Open code table
rows = currencies.findAll('tr')

for row in rows:                                            # Loop through rows of table
    x = [col.string for col in row.findAll('td')]
    print(x)
    x.pop(1)                                                # Remove country name and leave code
    x = ','.join(map(str,x) )                               # Convert lists in "codes" to strings
    OPTIONS.append(x)                                         # Add to "codes"






# the constructor syntax is:
# OptionMenu(master, variable, *values)

"""GUI"""

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS).grid(row=0, column=1)


vvariable = StringVar(master)
vvariable.set(OPTIONS[0]) # default valu

v = OptionMenu(master, vvariable, *OPTIONS).grid(row=1, column=1)



Label(master, text="Amount: ").grid(row=2)

e3 = Entry(master)

e3.grid(row=2, column=1)


"""Conversion Stage"""

def main():
    url2 = str(vvariable.get())
    amount = int(e3.get())

    try:
        qpage = 'https://themoneyconverter.com/' + url1 + '/' + url2 + '.aspx'
        page = ur.urlopen(qpage)
        soup = BeautifulSoup(page, 'html.parser')

        # Take out the <div> of name and get its value
        name_box = soup.find('div', attrs={'class': 'cc-result'})

        name = name_box.text.strip()
        name = name[8:15]
        res = amount * float(name)
        lsum = Label(master, text = 'Converted:')
        lsum.grid(row=4, column=0, sticky=W, pady=4)
        lsum["text"] = "Converted: " + str(res)
    except urllib.error.URLError as e:                          # If the page does not exist
        ResponseData = e.read().decode("utf8", 'ignore')


Button(master, text='Convert', command=main).grid(row=3, column=0, sticky=W, pady=4)


master.mainloop()



