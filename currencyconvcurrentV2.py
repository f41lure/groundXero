#############################################################################################################################################################################################
# CURRENCY CONVERTER                                                                                                                                                                        #
# Version 1.5 BETA                                                                                                                                                                          #
# With tkinter-based GUI                                                                                                                                                                    #
# Uses BeautifulSoup                                                                                                                                                                        #
#                                                                                                                                                                                           #
### PROBLEMS:                                                                                                                                                                               #
#                                                                                                                                                                                           #
# > Slow and sluggish retrieval of data from net                                                                                                                                            #
# > GUI show_codes function crashs                                                                                                                                                          +
# > GUI lacking advancements like drop-down menus                                                                                                                                           #
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#                                                                                                                                                                                           #
# Coded by ___Ibrahim Adnan____                                                                                                                                                             #
# On 26/11/2017                                                                                                                                                                             #
# Sunday, November 2017                                                                                                                                                                     #
# At approximately 10:26 PM PST                                                                                                                                                             # 
#                                                                                                                                                                                           #
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#############################################################################################################################################################################################


# import libraries
from tkinter import * 

import urllib.request as ur, re
import urllib.error
from bs4 import BeautifulSoup

def show_codes():
    # Gets codes and stores in list "codes"
    codes = []
    currency = 'http://www.xe.com/iso4217.php'                  # Store website URL
    currency_p = ur.urlopen(currency)                           
    soup2 = BeautifulSoup(currency_p, 'html.parser')            # Parse site

    currencies = soup2.find('tbody')                            # Open code table
    rows = currencies.findAll('tr')

    for row in rows:                                            # Loop through rows of table
        x = [col.string for col in row.findAll('td')]
        print(x)
      # x.pop(1)                                                # Remove country name and leave code
        x = ','.join(map(str,x) )                               # Convert lists in "codes" to strings
        codes.append(x)                                         # Add to "codes"
    lsum = Label(top, text = 'Codes and Names:')
    lsum.grid(row=4, column=0, sticky=W, pady=4)
    lsum["text"] = "Codes and names: " + str(codes)


def main():
    url1 = e1.get()
    url2 = e2.get()
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
        lsum = Label(top, text = 'Converted:')
        lsum.grid(row=4, column=0, sticky=W, pady=4)
        lsum["text"] = "Converted: " + str(res)
    except urllib.error.URLError as e:                          # If the page does not exist
        ResponseData = e.read().decode("utf8", 'ignore')



top = Tk()
# Code to add widgets will go here...
Label(top, text="From which to convert: ").grid(row=0)
Label(top, text="To which to convert: ").grid(row=1)
Label(top, text="Amount: ").grid(row=2)

e1 = Entry(top)
e2 = Entry(top)
e3 = Entry(top)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)


Button(top, text='Convert', command=main).grid(row=3, column=0, sticky=W, pady=4)
Button(top, text='Show Currency Codes', command=show_codes).grid(row=3, column=1, sticky=W, pady=4)

top.mainloop()
