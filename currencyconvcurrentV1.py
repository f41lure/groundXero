# import libraries
import urllib.request as ur, re
import urllib.error
from bs4 import BeautifulSoup

# Gets codes and stores in list "codes"
codes = []
currency = 'http://www.xe.com/iso4217.php'                  # Codes website
currency_p = ur.urlopen(currency)                           
soup2 = BeautifulSoup(currency_p, 'html.parser')            # Parse site

currencies = soup2.find('tbody')                            # Open code table
rows = currencies.findAll('tr')

for row in rows:                                            # Loop through rows of table
    x = [col.string for col in row.findAll('td')]
    print(x)
    x.pop(1)                                                # Remove country name and leave code
    x = ','.join(map(str,x) )                               # Convert lists in "codes" to strings
    codes.append(x)                                         # Add to "codes"



url1 = input("Enter the code from which to convert: ")
url2 = input("Enter the code to which to convert: ")
amount = int(input("Amount: "))

try:
    qpage = 'https://themoneyconverter.com/' + url1 + '/' + url2 + '.aspx'
    page = ur.urlopen(qpage)
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    name_box = soup.find('div', attrs={'class': 'cc-result'})

    name = name_box.text.strip()
    name = name[8:15]
    res = amount * float(name)
    print(res)    
except urllib.error.URLError as e:                          # If the page does not exist
    ResponseData = e.read().decode("utf8", 'ignore')
