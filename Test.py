import datetime
import tweepy
import csv
from Keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Verified")
except:
  print("Error during authentication")

filename = 'twitter_data_analysis' + (datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")) + '.csv'
query = "donald"
linecount = 0

with open(filename, 'a+', encoding="utf-8", newline='') as csvFile:
    csvWriter = csv.writer(csvFile)

    for tweet in tweepy.Cursor(api.search, q=query, lang='en', count=2000).items():
        tweets_encoded = tweet.text.encode('utf-8')
        tweets_decoded = tweets_encoded.decode('utf-8')
        csvWriter.writerow([datetime.datetime.now().strftime("%Y-%m-%d  %H:%M"),
                            tweet.id, tweets_decoded, tweet.created_at,
                            tweet.geo, tweet.coordinates, tweet._json["user"]["location"]])
        print(linecount)
        linecount = linecount + 1
