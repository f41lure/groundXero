# import libraries
import urllib.request as ur
from bs4 import BeautifulSoup

quote_page = 'https://themoneyconverter.com/' + 'PKR' + '/USD' + '.aspx'

page = ur.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find('div', attrs={'class': 'cc-result'})

name = name_box.text.strip()
name = name[8:15]

converted = int(input("To convert: ")) / float(name)

print(converted)
