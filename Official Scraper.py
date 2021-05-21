import tweepy
from Keys import *
from NecessaryFunctions import *
import pandas as pd

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
    # Pulling information from tweets
    tweets_list = [[tweet.created_at, tweet.id, tweet.full_text,
                    tweet.user.location, tweet.user.followers_count,
                    tweet.user.friends_count, tweet.user.verified,
                    tweet.is_quote_status, tweet.user.created_at,
                    tweet.user.default_profile, tweet.user.default_profile_image,
                    tweet.user.friends_count] for tweet in tweets]
    tweets_df = pd.DataFrame(tweets_list)

except BaseException as e:
    print('failed on_status,', str(e))
    quit()

# Spam Filter - Currently not working
print("Removing some spam")
spam_filter(tweets_df)

# Calculating Sentiments


# Adding current price to data frame
tweets_df.insert(3, "Price", current_price, True)

# Renaming Columns
tweets_df.columns = ['Date', 'Tweet ID', 'Text', 'BTC Price', 'User Location',
              'User follower count', 'User following count', 'User Verified',
              'Quote Status?', 'Account Creation Date', 'Default Profile Theme?',
              'Default Profile Image?', 'Total Account Likes']

# mode='a' to append once ready for production
tweets_df.to_csv("Scraped_Tweetstest.csv", header=True)
print("All done, check out final csv")
