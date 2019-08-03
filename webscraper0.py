import urllib.request as ur, re
import urllib.error
import xml
from bs4 import BeautifulSoup
import re


def url_provided():
    qpage = input("Enter your url: ")
    page = ur.urlopen(qpage)
    soup = BeautifulSoup(page, 'html.parser')
    name_box = str(soup.find_all('p'))

    #for idx, val in enumerate(name_box):
    #    if val == '<':
    #        y = idx
    #    if val == '>':
    #        x = idx
    #        final = name_box.replace(name_box[y:x], '')
    #        continue

    final = str(re.sub("<.*?>", "", name_box))
        

    print(final)
##def google_search(query):
##    for url in search(query, tld='es', lang='es', stop=20):
##        print(url)
##
##choice = input("""1) Provide your URL.
##2) Do a Google search.""")
##
##if choice == "1":
##    url_provided()
##elif choice == "2":
##    query = input("Search for: ")
##    google_search(query)
url_provided()
