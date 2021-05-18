import requests
from bs4 import BeautifulSoup
'''
This will be merged and modified into the official scraper. Returns the current price of bitcoin.
'''

source = requests.get('https://www.coindesk.com/price/bitcoin').text
soup = BeautifulSoup(source, 'lxml')

price = str(soup.find('div', class_='price-large'))
price = price.split("$</span>")[1]
price = price.replace('</div>', '')
print(price)

