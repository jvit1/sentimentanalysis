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

# Removing Spam
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


# Fixing Country Location
print("Cleaning Locations")
# Australia
australia_cities = "Queensland|Sydney|Australia|Melbourne"
tweets_df.loc[tweets_df['User Location'].str.contains(australia_cities, case=False, na=False), 'User Location'] = 'Australia'
# Bangledesh
bangladesh_cities = "Satkhira|Bangladesh"
tweets_df.loc[tweets_df['User Location'].str.contains(bangladesh_cities, case=False, na=False), 'User Location'] = 'Bangladesh'
# Brazil
brazil_cities = "Goiânia|Janeiro|Brasil|Brazil|Sao Paulo"
tweets_df.loc[tweets_df['User Location'].str.contains(brazil_cities, case=False, na=False), 'User Location'] = 'Brazil'
# Canada
canada_cities = "Toronto|Ontario|Canada|Vancouver|Ottawa|Montréal|Québec|Alberta"
tweets_df.loc[tweets_df['User Location'].str.contains(canada_cities, case=False, na=False), 'User Location'] = 'Canada'
# Cyprus
cyprus_cities = "Ayia"
tweets_df.loc[tweets_df['User Location'].str.contains(cyprus_cities, case=False, na=False), 'User Location'] = 'Cyprus'
# France
france_cities = "France|Paris"
tweets_df.loc[tweets_df['User Location'].str.contains(france_cities, case=False, na=False), 'User Location'] = 'France'
# Indonesia
indonesia_cities = "Jakarta|Indonesia|Bekasi|Java|Jawa"
tweets_df.loc[tweets_df['User Location'].str.contains(indonesia_cities, case=False, na=False), 'User Location'] = 'Indonesia'
# India
india_cities = "Mumbai|India|bangalore|Nairobi|New Delhi"
tweets_df.loc[tweets_df['User Location'].str.contains(india_cities, case=False, na=False), 'User Location'] = 'India'
# Kenya
kenya_cities = "Kisumu"
tweets_df.loc[tweets_df['User Location'].str.contains(kenya_cities, case=False, na=False), 'User Location'] = 'Kenya'
# Malaysia
Malaysia_cities = "Malaysia|Kuala"
tweets_df.loc[tweets_df['User Location'].str.contains(Malaysia_cities, case=False, na=False), 'User Location'] = 'Malaysia'
# Nigeria
nigeria_cities = "Nigeria"
tweets_df.loc[tweets_df['User Location'].str.contains(nigeria_cities, case=False, na=False), 'User Location'] = 'Nigeria'
# Philippines
pilippines_cities = "Caloocan|Philippines"
tweets_df.loc[tweets_df['User Location'].str.contains(pilippines_cities, case=False, na=False), 'User Location'] = 'Philippines'
#South Africa
south_africancities = "Midrand|South Africa"
tweets_df.loc[tweets_df['User Location'].str.contains(south_africancities, case=False, na=False), 'User Location'] = 'South Africa'
# Thailand
thailand_cities = "Bangkok"
tweets_df.loc[tweets_df['User Location'].str.contains(thailand_cities, case=False, na=False), 'User Location'] = 'Thailand'
# United States
us_cities = "Angeles|York|Greenville|Michigan|Tampa|Fayetteville|Antonio|Manhattan|USA|Boston|Detroit|United States|" \
            "Dallas|Oklahoma|Jersey|Chicago|Albuquerque|Orlando|NYC|San Francisco|Leesburg|Ohio|Miami|Stamford|SEATTLE|" \
            "TX|Gainesville|Denver|Bay Area|Philly|Florida|KY|St Joseph|Vegas|Providence|Myrtle|Pennsylvania|Washington|Richmond|" \
            "Texas|Savannah|Salt Lake|New Orleans|Cary|Long Island|Concrete Jungle|united state|colorado|" \
            "grand rapids|Louisville|Charlotte|Atlanta|Jacksonville|Inglewood|Scottsdale|Palm Beach|Columbus|Kansas City|" \
            "California|Palo Alto|Columbus|Roanoke|Durham|Rochester|Beverly Hills|Utah|America|Madison|Philadelp|Hollywood|" \
            "Boca Raton|Portland|Nashville|Tacoma|Wellington|Bethesda|Roseville|Bristol|Lafayette|San Diego|Night City|" \
            "Lauderdale|Wildwood|NJ|San Jose|TN|Hawaii|Brooklyn|Bethlehem|Orange County|Birmingham|Virginia|FL|Victoria|" \
            "Silicon Valley|Brookline|Allentown|Pasadena|Queens|Nevada|Santa Clara|Lancaster|Bellevue|Marina del|Rockville|" \
            "Darien|Mesa|Oshkosh|Laguna|Baltimore|Rochelle|Ridgefield|Castle Rock|Lake Forest|St Louis|Tyson|Santa Rosa|" \
            "Alexandria|Sacramento|Raleigh|NY"
tweets_df.loc[tweets_df['User Location'].str.contains(us_cities, case=False, na=False), 'User Location'] = 'United States of America'
#United Kingdom
uk_cities = "London|Liverpool|England|Scotland|UK|Ireland|United Kingdom|Wales"
tweets_df.loc[tweets_df['User Location'].str.contains(uk_cities, case=False, na=False), 'User Location'] = 'United Kingdom'


# mode='a' to append once ready for production
tweets_df.to_csv("Scraped_Tweets.csv", header=False, mode='a')
print("All done, check out final csv")