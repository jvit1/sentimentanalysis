import tweepy
from Keys import *
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Current Price
source = requests.get('https://www.coindesk.com/price/bitcoin').text
soup = BeautifulSoup(source, 'lxml')

current_price = str(soup.find('div', class_='price-large'))
current_price = current_price.split("$</span>")[1]
current_price = current_price.replace('</div>', '')
current_price = float(current_price.replace(',', ''))

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Verified")
except:
    print("Error during authentication")

# Parameters to scrape from twitter
query = 'bitcoin'
n_tweets = 200

print('Tweets are now being scraped')
try:
    # Creation of query method using parameters
    tweets = tweepy.Cursor(api.search, q=query, lang="en", tweet_mode='extended').items(n_tweets)
    # Pulling information from tweets iterable object
    tweets_list = [[tweet.created_at, tweet.id, tweet.full_text,
                    tweet.place, tweet.user.followers_count,
                    tweet.user.friends_count, tweet.user.verified,
                    tweet.is_quote_status] for tweet in tweets]
    tweets_df = pd.DataFrame(tweets_list)

except BaseException as e:
    print('failed on_status,', str(e))

# Attempts to filter spam
print("Removing some spam")
df = tweets_df[~tweets_df[2].str.contains("RT")]
df = df[~(df[4] <= 100)]

# Adding current price to data frame
df.insert(3, "Price", current_price, True)

# Renaming Columns
df.columns = ['Date', 'Tweet ID', 'Text', 'BTC Price', 'User Location',
              'User follower count', 'User following count', 'User Verified',
              'Quote Status?']
print(df)
# mode='a' to append once ready for production
df.to_csv("Scraped_Tweets.csv", header=True)
