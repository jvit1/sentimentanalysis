import tweepy
from Keys import *
import pandas as pd

'''
This code is used to scrape the tweets of a single user based on parameters.
It is incomplete and does not add to a csv quite yet.
'''
# Twitter Authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Verified")
except:
    print("Error during authentication")

n_tweets = 100
tweets = []
likes = []
time = []

# api.search, q='whatever'
for i in tweepy.Cursor(api.user_timeline, id='elonmusk', tweet_mode="extended").items(n_tweets):
    tweets.append(i.full_text)
    likes.append(i.favorite_count)
    time.append(i.created_at)

df = pd.DataFrame({'tweets': tweets, 'likes': likes, 'time': time})

# Removing Retweets
df = df[~df.tweets.str.contains("RT")]
