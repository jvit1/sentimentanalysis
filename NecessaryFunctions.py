import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import re
import emoji

'''
The following file defines functions and values that are used throughout the scraper before outputting the cleaned dataset.
'''


# Cleans the majority of the doo doo out of the tweet text
def CleanText(text):
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)  # no @s
    text = re.sub(r'#', '', text)  # no hashtag symbols
    text = re.sub(r'https?:\/\/\S+', '', text)  # Remove image links
    text = re.sub(r'\$[A-Z]+', '', text)  # Remove currency labels
    text = re.sub(r'\n', '', text)  # remove hyperlink
    return text


# Removes emojis
def remove_emoji(text):
    return emoji.get_emoji_regexp().sub(u'', text)


# Subjectivity
def Subjectivity(text):
    return TextBlob(text).sentiment.subjectivity


# Polarity
def Polarity(text):
    return TextBlob(text).sentiment.polarity


# Current Price
source = requests.get('https://www.coindesk.com/price/bitcoin').text
soup = BeautifulSoup(source, 'lxml')

current_price = str(soup.find('div', class_='price-large'))
current_price = current_price.split("$</span>")[1]
current_price = current_price.replace('</div>', '')
current_price = float(current_price.replace(',', ''))
