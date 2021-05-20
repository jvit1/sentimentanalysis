import tweepy
from Keys import *
import pandas as pd
import requests
from bs4 import BeautifulSoup

test

# Current Price
source = requests.get('https://www.coindesk.com/price/bitcoin').text
soup = BeautifulSoup(source, 'lxml')

price = str(soup.find('div', class_='price-large'))
price = price.split("$</span>")[1]
price = price.replace('</div>', '')

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Verified")
except:
    print("Error during authentication")

query = 'bitcoin'
n_tweets = 50

try:
    # Creation of query method using parameters
    tweets = tweepy.Cursor(api.search, q=query).items(n_tweets)

    # Pulling information from tweets iterable object
    tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
    tweets_df = pd.DataFrame(tweets_list)

except BaseException as e:
    print('failed on_status,', str(e))

df = tweets_df[~tweets_df[2].str.contains("RT")]
print(df)
# mode='a'
#df.to_csv("Scraped_Tweets.csv", header=False)
