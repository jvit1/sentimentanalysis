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
n_tweets = 2000

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

# Adding current price to data frame
print('Adding Current BTC Price')
tweets_df.insert(3, "Price", current_price, True)

# Renaming Columns
tweets_df.columns = ['Date', 'TweetID', 'Text', 'BTC Price', 'User Location',
              'User follower count', 'UserFollowingCount', 'User Verified',
              'Quote Status?', 'AccountCreationDate', 'Default Profile Theme?',
              'DefaultProfileImage', 'TotalAccountLikes']



#spam_filter(tweets_df)
print("Removing some spam")
tweets_df['Text'] = tweets_df['Text'].apply(CleanText)  # Text Cleaner
tweets_df = tweets_df[~tweets_df.Text.astype(str).str.contains("RT")]  # Removing Retweets
tweets_df = tweets_df[~(tweets_df.UserFollowingCount <= 100)]  # Making sure total followers is greater than 100
tweets_df = tweets_df[~(tweets_df.TotalAccountLikes <= 100)]  # Making sure total account likes is greater than 100
tweets_df = tweets_df[(tweets_df.DefaultProfileImage == False)]  # Making sure there is a real profile pic
tweets_df = tweets_df[~tweets_df.AccountCreationDate.astype(str).str.contains("2021")]  # Removing New Accounts
tweets_df['Text'] = tweets_df['Text'].apply(remove_emoji)  # Removing Emojis

#Subjectivity (opinion[1]) and Polarity (positive [1] or negative [0])
tweets_df['Subjectivity'] = tweets_df['Text'].apply(Subjectivity)
tweets_df['Polarity'] = tweets_df['Text'].apply(Polarity)

tweets_df = tweets_df[(tweets_df.Polarity != 0)]  # Making sure polarity is not 0


# mode='a' to append once ready for production
tweets_df.to_csv("Scraped_Tweets.csv", header=False, mode='a')
print("All done, check out final csv")
