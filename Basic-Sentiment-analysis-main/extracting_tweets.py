from cProfile import label
import tweepy
from tweepy import OAuthHandler
import pandas as pd

access_token = 'Enter API access_token'
access_token_secret = 'Enter API access_token_secret'
consumer_key = 'Enter consumer_key'
consumer_secret = 'Enter consumer_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = []

count = 1

for tweet in tweepy.Cursor(api.search_tweets,q="Nike", lang="en",until='2022-06-30').items(50000):
	
	print(count)
	count += 1
    
    

	try: 
		data = [tweet.created_at, tweet.id, tweet.text, tweet.user._json['screen_name'], tweet.user._json['name'], tweet.user._json['created_at'], tweet.entities['urls']]
		data = tuple(data)
		tweets.append(data)

	except tweepy.TweepError as e:
		print(e.reason)
		continue

	except StopIteration:
		break

df = pd.DataFrame(tweets, columns = ['created_at','tweet_id', 'tweet_text', 'screen_name', 'name', 'account_creation_date', 'urls'])

"""Add the path to the folder you want to save the CSV file in as well as what you want the CSV file to be named inside the single quotations"""
df.to_csv("raw_data.csv")