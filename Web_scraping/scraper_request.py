import requests, re
from bs4 import BeautifulSoup

page = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(page.content,'html.parser')
#
# print(soup.find('h1').string)
print(soup.select_one('head  title').string)