import requests
from bs4 import BeautifulSoup
import pandas as pd
from textblob import TextBlob
import re
from nltk.corpus import stopwords

'''
The following file defines functions and values that are used throughout the scraper before outputting the cleaned dataset.
'''


def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  # no @s
    text = re.sub(r'#', '', text)  # no hashtag symbols
    text = re.sub(r'https?:\/\/\S+', '', text)  # remove hyperlink
    return text

# Spam Filter - Find way to apply this
def spam_filter(df):
    df = df[~df.Text.astype(str).str.contains("RT")]
    df = df[~(df.UserFollowingCount <= 100)]  # Making sure total followers is greater than 100
    df = df[~(df.TotalAccountLikes <= 100)]  # Making sure total account likes is greater than 100
    df = df[(df.DefaultProfileImage == False)]
    return df


# Current Price
source = requests.get('https://www.coindesk.com/price/bitcoin').text
soup = BeautifulSoup(source, 'lxml')

current_price = str(soup.find('div', class_='price-large'))
current_price = current_price.split("$</span>")[1]
current_price = current_price.replace('</div>', '')
current_price = float(current_price.replace(',', ''))
