import tweepy
import json
import csv
from Keys import *

'''
This code is used to live stream tweets.
It will likely not be used for analysis.
'''

# csvFile = open('result.csv', 'a')
# csvWriter = csv.writer(csvFile)

# Streamlistener

class MaxListener(tweepy.StreamListener):

    def on_data(self, raw_data):
        self.process_data(raw_data)
        return True

    def process_data(self, raw_data):
        json.data = json.loads(raw_data)
        print(json.data['text'])

    def on_status(self, status):
        print(status.id_str)
        # if "retweeted_status" attribute exists, flag this tweet as a retweet.
        is_retweet = hasattr(status, "retweeted_status")

    def on_error(self, status_code):
        if status_code == 420:
            # returning F in on_data disconnects the stream
            return False


# Create the Stream

class MaxStream():

    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)

    def start(self, keyword_list):
        self.stream.filter(track=keyword_list, languages=['en'])


# Start the stream
if __name__ == "__main__":
    listener = MaxListener()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = MaxStream(auth, listener)
    stream.start(['bitcoin'])

