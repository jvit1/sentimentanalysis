import requests
from bs4 import BeautifulSoup
'''
The following file defines functions and values that are used throughout the scraper before outputting the cleaned dataset.
'''
# Spam Filter
def spam_filter(df):
    df = df[~df[2].str.contains("RT")]
    df = df[~(df[4] <= 100)]  # Making sure total followers is greater than 100
    df = df[~(df[11] <= 100)]  # Making sure total account likes is greater than 100
    df = df[(df[10] == False)]  # Making sure there is a real profile pic
    return df

# Current Price
source = requests.get('https://www.coindesk.com/price/bitcoin').text
soup = BeautifulSoup(source, 'lxml')

current_price = str(soup.find('div', class_='price-large'))
current_price = current_price.split("$</span>")[1]
current_price = current_price.replace('</div>', '')
current_price = float(current_price.replace(',', ''))